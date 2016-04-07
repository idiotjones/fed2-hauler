import planets_list as pl


shell_commodity_sources = {
		'Alloys': [pl.all_planets['improbable']],
		'AntiMatter': [pl.all_planets['improbable']],
		'Artifacts': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'BioChips': [pl.all_planets['anacreon'], pl.all_planets['vivid']],
		'BioComponents': [pl.all_planets['doubtful']],
		'Cereals': [pl.all_planets['unlikely'], pl.all_planets['improbable'], pl.all_planets['santanni']],
		'Clays': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'Clinics': [pl.all_planets['doubtful']],
		'Controllers': [pl.all_planets['improbable']],
		'Crystals': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Droids': [pl.all_planets['improbable']],
		'Electros': [pl.all_planets['doubtful']],
		'Explosives': [pl.all_planets['improbable']],
		'Firewalls': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Fruit': [pl.all_planets['improbable']],
		'Furs': [pl.all_planets['unlikely']],
		'Games': [pl.all_planets['doubtful']],
		'GAsChips': [pl.all_planets['doubtful'], pl.all_planets['unlikely'], pl.all_planets['anacreon']],
		'Generators': [pl.all_planets['improbable']],
		'Gold': [pl.all_planets['doubtful']],
		'Hides': [pl.all_planets['santanni'], pl.all_planets['improbable']],
		'Holos': [pl.all_planets['doubtful']],
		'Hypnotapes': [pl.all_planets['smyrno'], pl.all_planets['doubtful']],
		'Katydidics': [pl.all_planets['doubtful'], pl.all_planets['anacreon']],
		'Laboratories': [pl.all_planets['anacreon'], pl.all_planets['viand']],
		'LanzariK': [pl.all_planets['improbable']],
		'Lasers': [pl.all_planets['doubtful']],
		'Libraries': [pl.all_planets['vivid'], pl.all_planets['anacreon']], 
		'Livestock': [pl.all_planets['unlikely']],
		'LubOils': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'Meats': [pl.all_planets['helicon'], pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'Mechparts': [pl.all_planets['unlikely'], pl.all_planets['smyrno']],
		'MicroScalpels': [pl.all_planets['doubtful']],
		'Monopoles': [pl.all_planets['improbable']],
		'Munitions': [pl.all_planets['doubtful']],
		'Musiks': [pl.all_planets['doubtful'], pl.all_planets['smyrno']],
		'NanoFabrics': [pl.all_planets['improbable']],
		'Nanos': [pl.all_planets['helicon'], pl.all_planets['unlikely']],
		'Nickel': [pl.all_planets['doubtful']],
		'Nitros': [pl.all_planets['doubtful']],
		'Petrochemicals': [pl.all_planets['unlikely'], pl.all_planets['terminus']],
		'Pharmaceuticals': [pl.all_planets['improbable']],
		'Polymers': [pl.all_planets['improbable']],
		'Powerpacks': [pl.all_planets['doubtful']],
		'Probes': [pl.all_planets['doubtful']],
		'Propellants': [pl.all_planets['unlikely']],
		'Proteins': [pl.all_planets['viand']],
		'Radioactives': [pl.all_planets['doubtful']],
		'RNA': [pl.all_planets['improbable']],
		'Semiconductors': [pl.all_planets['doubtful'], pl.all_planets['terminus']],
		'Sensamps': [pl.all_planets['doubtful']],
		'Sensors': [pl.all_planets['anacreon'], pl.all_planets['doubtful']],
		'Simulations': [pl.all_planets['improbable']],
		'Soya': [pl.all_planets['unlikely'], pl.all_planets['santanni']],
		'Spices': [pl.all_planets['improbable']],
		'Studios': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Synths': [pl.all_planets['improbable']],
		'Textiles': [pl.all_planets['santanni'], pl.all_planets['unlikely'], pl.all_planets['improbable']],
		'Tools': [pl.all_planets['doubtful']],
		'ToxicMunchers': [pl.all_planets['doubtful']],
		'TQuarks': [pl.all_planets['improbable']],
		'Tracers': [pl.all_planets['viand']],
		'Univators': [pl.all_planets['doubtful'], pl.all_planets['cinna']],
		'Vidicasters': [pl.all_planets['improbable']],
		'Weapons': [pl.all_planets['improbable']],
		'Woods': [pl.all_planets['zaldrizes']],
		'Xmetals': [pl.all_planets['doubtful']],
}



system_owners = {'shell': 'idiotjones',
		'total': 'johngradycole',
		'default': 'billyparham', 
		'chevron': 'jimmyblevins', }


system_planets = {'shell': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful']],
		'total': [pl.all_planets['wreck']],
		'default': [pl.all_planets['welch']],
		'chevron': [pl.all_planets['herringbone']], }



system_commodity_sources = {'shell': shell_commodity_sources,
		'total': shell_commodity_sources,
		'default': shell_commodity_sources,
		'chevron': shell_commodity_sources, }


passwords = {'idiotjones': 'idiotpassword',
		'johngradycole':  'johnpassword',
		'billyparham': 'billypassword',
		'jimmyblevins':  'jimmypassword',
		}
