import sys
from fed_connection import fed_connection
import system_config

def main(argv=None):
	if argv is None:
		argv = sys.argv

	if len(argv) == 2:
		system_name = argv[1]
	else:
		print "Please provide a system name"
		sys.exit()

	user = system_config.system_owners[system_name]
	password = system_config.passwords[user]

	system_planets = system_config.system_planets[system_name]
	start_planet_index = 0
	start_planet = system_planets[start_planet_index]
	start_loc = start_planet.start_loc
	commodity_sources = system_config.system_commodity_sources[start_planet.system]

	fc = fed_connection(user, password, start_loc)

	if fc.verify_start_location():
		fc.fill_deficits(system_planets, start_planet_index, commodity_sources)
	else:
		print "Could not verify start location"
		sys.exit(1)

if '__main__' == __name__:
	main()
