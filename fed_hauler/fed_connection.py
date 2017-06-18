import telnetlib
from datetime import datetime
import time
import sys
import random
import re
import pytz

def buy_7_loads(commodity):
	return ['buy {commodity}'.format(commodity=commodity) for x in range(7)]

def sell_7_loads(commodity):
	return ['sell {commodity}'.format(commodity=commodity) for x in range(7)]

def is_exchange_output_line(line):
	commodity_line_pattern = '''\s+\w+:\s+value\s+\d+ig/ton\s+Spread:\s+\d+%\s+Stock:\s+current\s+-?\d+/min\s+\d+/max\s+\d+\s+Efficiency:\s+\d+%'''
	return not (re.match(commodity_line_pattern, line) is None)

class fed_connection:
	def __init__(self, user, password, start_loc):
		HOST = "fed2.ibgames.net"
		PORT = 30003
		self.tn = telnetlib.Telnet(HOST, PORT)
		self.start_loc = start_loc

		self.tn.read_until("Login:")
		self.tn.write(user + "\n")
		self.tn.read_until("Password:")
		self.tn.write(password + "\n")

		time.sleep(1)
		self.tn.read_very_eager()



	def get_deficits(self):
		exchange_output = self.send_command("di exchange")
		lines = exchange_output.splitlines()
		deficits = []
		for line in lines:
			if "-525" in line and is_exchange_output_line(line):
				deficits.append(line)
		return deficits

	def send_command(self, command):
		self.tn.write(command + "\n")
		time.sleep(1)
		output = self.read_next_output()
		if True:
			current_time = datetime.now(tz=pytz.timezone('Europe/London')).strftime("%Y-%m-%d %H:%M:%S")
			print """[{timestamp}]""".format(timestamp=current_time)
			print """{output}""".format(output=output)
		return output

	def send_command_list(self, command_list):
		for command in command_list:
			self.send_command(command)

	def read_next_output(self):
		return self.tn.read_very_eager()

	def interact(self):
		self.tn.interact()
	
	def handle_deficits(self):
		pass
	
	def verify_start_location(self):
		loc = self.send_command("look")
		if self.start_loc not in loc:
			print "Not on the right start location"
			return False
		else:
			print "On the right start location"
			return True

	def fill_deficits(self, system_planets, start_planet_index, commodity_sources):
		empty_planet_count = 0
		deficit_fill_count = 0
		current_planet_index = start_planet_index
		current_planet = system_planets[current_planet_index]
		while True:
			next_planet_index = (current_planet_index + 1) % len(system_planets)
			next_planet = system_planets[next_planet_index]

			deficits = self.get_deficits()

			if len(deficits) > 0:
				empty_planet_count = 0
				current_deficit = deficits[0].split()[0][:-1]
				self.send_command("say Bot filling {commodity}.".format(commodity=current_deficit))
				print "Filling {commodity}.".format(commodity=current_deficit)
				self.fill_deficit(current_planet, current_deficit, commodity_sources)

				self.send_command("say Filled {commodity}.".format(commodity=current_deficit))
				print "Filled {commodity}.".format(commodity=current_deficit)
				deficit_fill_count += 1
				self.check_time_and_sleep(5)
			else:
				self.send_command("say No more deficits at this exchange.  Moving to {planet}".format(planet=next_planet.name))
				print "No more deficits at this exchange.  Moving to {planet}".format(planet=next_planet.name)
				empty_planet_count += 1
				self.move_planets(current_planet, next_planet)
				current_planet = next_planet
				current_planet_index = next_planet_index
				if( len(system_planets) <= empty_planet_count ):
					self.check_time_and_sleep(900)
					empty_planet_count = 0
				deficit_fill_count = 0

	def fill_deficit(self, planet, deficit, commodity_sources):
		commodity_source_planet = self.get_commodity_source_planet(deficit, commodity_sources)
		self.move_planets(planet, commodity_source_planet)
		self.buy_commodity_on_current_planet(commodity_source_planet, deficit)
		self.move_planets(commodity_source_planet, planet)
		self.sell_commodity_on_current_planet(planet, deficit)
		self.buy_food(planet)
		self.buy_fuel()
		self.check_stamina()
		self.system_status_check()

	def get_commodity_source_planet(self, deficit, commodity_sources):
		commodity_source_planets = commodity_sources[deficit]
		if 1 == len(commodity_source_planets):
			return commodity_source_planets[0]
		random_index = random.randint(0,len(commodity_source_planets)-1)
		return commodity_source_planets[random_index]
		
	def buy_commodity_on_current_planet(self, planet, commodity):
		commands = list(planet.to_exchange)
		commands.extend(buy_7_loads(commodity))
		commands.extend(planet.from_exchange)
		self.send_command_list(commands)

	def sell_commodity_on_current_planet(self, planet, commodity):
		commands = list(planet.to_exchange)
		commands.extend(sell_7_loads(commodity))
		commands.extend(planet.from_exchange)
		self.send_command_list(commands)

	def move_planets(self, current_planet, next_planet):
		if( current_planet == next_planet ):
			return
		else:
			move_commands = ['board']
			move_commands.extend(current_planet.to_link)
			if current_planet.cartel != next_planet.cartel:
				if current_planet.cartel != current_planet.system:
					move_commands.append('j {cartel}'.format(cartel=current_planet.cartel))
				move_commands.append('j {cartel}'.format(cartel=next_planet.cartel))
			# If either the system is a non-cartel system in another cartel, or it is another system in the same cartel, jump to that system
			if (current_planet.system != next_planet.system and next_planet.system != next_planet.cartel) or (current_planet.cartel == next_planet.cartel and current_planet.system != next_planet.system):
				move_commands.append('j {system}'.format(system=next_planet.system))
			move_commands.extend(next_planet.from_link)
			move_commands.append('board')
			self.send_command_list(move_commands)
			self.buy_fuel()
		return

	def buy_food(self, planet):
		commands = list(planet.to_bar)
		commands.append('buy food')
		commands.extend(planet.from_bar)
		self.send_command_list(commands)

	def buy_fuel(self):
		self.send_command('buy fuel')

	def check_stamina(self):
		self.send_command("st")
		score_output = self.send_command('sc')
		score_output_lines = score_output.splitlines()
		for line in score_output_lines:
			if "Stamina" in line:
				current_stamina = int(line[(line.find("current:")+9):].strip())
				if current_stamina < 25:
					self.send_command("say STAMINA IS BELOW ACCEPTABLE LEVEL!  INITIATING INTERACTIVE MODE...")
					self.interact()
				else:
					self.send_command("say Current stamina is okay at {}".format(current_stamina))

	def system_status_check(self):
		self.send_command("di system")

	def check_time_and_sleep(self, sleep_seconds):
		# If we're too close to reset then don't bother sleeping; just go to interactive mode and wait for reset.
		current_time = datetime.now(tz=pytz.timezone('Europe/London'))
		current_hour = current_time.hour
		current_minute = current_time.minute
		if 12 == current_hour and current_minute > 35:
			self.send_command("say Close to reset; going to interactive mode to wait it out until the connection is killed.")
			self.interact()
			sys.exit()

		# If we're not too close, then go ahead and do the sleep
		sleep_time = sleep_seconds
		sleep_time_increment = "seconds"
		if sleep_seconds > 60:
			sleep_time = sleep_seconds / 60
			sleep_time_increment = "minutes"
		print "Sleeping for {time} {increment}...".format(time=sleep_time, increment=sleep_time_increment)
		time.sleep(sleep_seconds)

