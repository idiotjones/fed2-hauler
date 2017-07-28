import planets_list as pl


shell_commodity_sources = {
		'Alloys': [pl.all_planets['terminus'], pl.all_planets['anacreon']],  # , pl.all_planets['new street glide']],
		'AntiMatter': [pl.all_planets['doubtful'], pl.all_planets['unlikely']],
		'Artifacts': [pl.all_planets['smyrno']], #, pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['unlikely']],
		'BioChips': [pl.all_planets['anacreon'], pl.all_planets['anacreon'], pl.all_planets['anacreon'], pl.all_planets['vivid']],
		'BioComponents': [pl.all_planets['doubtful']],
		'Cereals': [pl.all_planets['santanni'], pl.all_planets['terminus']],
		'Clays': [pl.all_planets['doubtful'], pl.all_planets['eos'], pl.all_planets['anacreon']],
		'Clinics': [pl.all_planets['doubtful']],
		'Controllers': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Crystals': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['crash'], pl.all_planets['bilk']],
		'Droids': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Electros': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['unlikely']],
		'Explosives': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Firewalls': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful']],
		'Fruit': [pl.all_planets['santanni'], pl.all_planets['helicon']], # pl.all_planets['new street glide']], 
		'Furs': [pl.all_planets['terminus']], # pl.all_planets['new street glide']], 
		'Games': [pl.all_planets['doubtful'], pl.all_planets['wreck']],
		'GAsChips': [pl.all_planets['anacreon'], pl.all_planets['cinna'], pl.all_planets['unlikely'], pl.all_planets['unlikely'], pl.all_planets['doubtful']],
		'Generators': [pl.all_planets['unlikely'], pl.all_planets['doubtful'], pl.all_planets['herringbone']],
		'Gold': [pl.all_planets['doubtful'], pl.all_planets['divide'], pl.all_planets['bilk']],
		'Hides': [pl.all_planets['santanni'], pl.all_planets['herringbone']],
		'Holos': [pl.all_planets['doubtful'], pl.all_planets['unlikely']],
		'Hypnotapes': [pl.all_planets['smyrno'], pl.all_planets['doubtful'], pl.all_planets['unlikely']],
		'Katydidics': [pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['cinna'], pl.all_planets['anacreon']],
		'Laboratories': [pl.all_planets['anacreon'], pl.all_planets['viand'], pl.all_planets['newsgroup']],
		'LanzariK': [pl.all_planets['doubtful']],
		'Lasers': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'Libraries': [pl.all_planets['vivid'], pl.all_planets['anacreon'], pl.all_planets['unlikely'], pl.all_planets['unlikely']], 
		'Livestock': [pl.all_planets['santanni']], # pl.all_planets['new street glide']], 
		'LubOils': [pl.all_planets['doubtful']],
		'Meats': [pl.all_planets['helicon'], pl.all_planets['maminar'], pl.all_planets['maminar'], pl.all_planets['vantek'], pl.all_planets['vantek']],
		'Mechparts': [pl.all_planets['doubtful'], pl.all_planets['smyrno']],
		'MicroScalpels': [pl.all_planets['doubtful']],
		'Monopoles': [pl.all_planets['santanni'], pl.all_planets['terminus']],
		'Munitions': [pl.all_planets['doubtful']],
		'Musiks': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful'], pl.all_planets['smyrno']],
		'NanoFabrics': [pl.all_planets['doubtful'], pl.all_planets['anacreon'], pl.all_planets['cinna']],
		'Nanos': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['cinna'], pl.all_planets['helicon']],
		'Nickel': [pl.all_planets['helicon'], pl.all_planets['doubtful'], pl.all_planets['demolish']],
		'Nitros': [pl.all_planets['improbable'], pl.all_planets['terminus'], pl.all_planets['anacreon']],
		'Petrochemicals': [pl.all_planets['eos'], pl.all_planets['terminus']],
		'Pharmaceuticals': [pl.all_planets['eos'], pl.all_planets['smyrno']], # pl.all_planets['doubtful']], 
		'Polymers': [pl.all_planets['anacreon']],
		'Powerpacks': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'Probes': [pl.all_planets['doubtful']],
		'Propellants': [pl.all_planets['doubtful'], pl.all_planets['anacreon']], # pl.all_planets['new street glide']],
		'Proteins': [pl.all_planets['viand']],
		'Radioactives': [pl.all_planets['doubtful'], pl.all_planets['valisk'], pl.all_planets['welch'], pl.all_planets['divide']], # , pl.all_planets['new street glide']
		'RNA': [pl.all_planets['doubtful']],
		'Semiconductors': [pl.all_planets['terminus'], pl.all_planets['doubtful']],
		'Sensamps': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'Sensors': [pl.all_planets['anacreon'], pl.all_planets['doubtful'], pl.all_planets['newsgroup']],
		'Simulations': [pl.all_planets['cinna'], pl.all_planets['eos']],
		'Soya': [pl.all_planets['santanni']], # pl.all_planets['new street glide']], 
		'Spices': [pl.all_planets['terminus']],
		'Studios': [pl.all_planets['doubtful'], pl.all_planets['unlikely']],
		'Synths': [pl.all_planets['doubtful']],
		'Textiles': [pl.all_planets['santanni']], # pl.all_planets['new street glide']],
		'Tools': [pl.all_planets['doubtful'], pl.all_planets['improbable']],
		'ToxicMunchers': [pl.all_planets['doubtful']],
		'TQuarks': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Tracers': [pl.all_planets['viand']],
		'Univators': [pl.all_planets['doubtful'], pl.all_planets['newsgroup'], pl.all_planets['cinna']],
		'Vidicasters': [pl.all_planets['unlikely'], pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Weapons': [pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Woods': [pl.all_planets['bilk'], pl.all_planets['herringbone']],
		'Xmetals': [pl.all_planets['demolish'], pl.all_planets['bilk'], pl.all_planets['herringbone']],
}



system_owners = {'shell': 'idiotjones',
		'total': 'johngradycole',
		'default': 'billyparham', 
		'chevron': 'jimmyblevins', 
		'gulf': 'toadvine',}


system_planets = {'shell': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful']],
		'total': [pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'default': [pl.all_planets['welch'], pl.all_planets['bilk']],
		'chevron': [pl.all_planets['herringbone']],
		'gulf': [pl.all_planets['divide']],}



system_commodity_sources = {'shell': shell_commodity_sources,
		'total': shell_commodity_sources,
		'default': shell_commodity_sources,
		'chevron': shell_commodity_sources, 
		'gulf': shell_commodity_sources, }


passwords = {'idiotjones': 'idiotpassword',
        'johngradycole':  'johnpassword',
        'billyparham': 'billypassword',
        'jimmyblevins':  'jimmypassword',
        }
