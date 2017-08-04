import planets_list as pl


shell_commodity_sources = {
		'Alloys': [pl.all_planets['terminus'], pl.all_planets['anacreon']],  # , pl.all_planets['new street glide']],
		'AntiMatter': [pl.all_planets['doubtful'], pl.all_planets['unlikely'], pl.all_planets['wreck']],
		'Artifacts': [pl.all_planets['wreck'], pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['demolish']],
		'BioChips': [pl.all_planets['crash'], pl.all_planets['anacreon'], pl.all_planets['anacreon'], pl.all_planets['vivid']],
		'BioComponents': [pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Cereals': [pl.all_planets['santanni'], pl.all_planets['terminus']],
		'Clays': [pl.all_planets['doubtful'], pl.all_planets['eos'], pl.all_planets['anacreon']],
		'Clinics': [pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Controllers': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Crystals': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['crash'], pl.all_planets['bilk'], pl.all_planets['crash']],
		'Droids': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Electros': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['unlikely'], pl.all_planets['wreck'], pl.all_planets['demolish']],
		'Explosives': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Firewalls': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['demolish']],
		'Fruit': [pl.all_planets['santanni'], pl.all_planets['helicon'], pl.all_planets['bilk'], pl.all_planets['herringbone'], pl.all_planets['fisticuffs'], pl.all_planets['zaldrizes']], # pl.all_planets['new street glide']],
		'Furs': [pl.all_planets['terminus']], # pl.all_planets['new street glide']],
		'Games': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['demolish']],
		'GAsChips': [pl.all_planets['demolish'], pl.all_planets['wreck'], pl.all_planets['unlikely'], pl.all_planets['crash'], pl.all_planets['doubtful']],
		'Generators': [pl.all_planets['unlikely'], pl.all_planets['doubtful'], pl.all_planets['herringbone']],
		'Gold': [pl.all_planets['doubtful'], pl.all_planets['divide'], pl.all_planets['bilk'], pl.all_planets['welch']],
		'Hides': [pl.all_planets['santanni'], pl.all_planets['herringbone'], pl.all_planets['fisticuffs'], pl.all_planets['bilk'], pl.all_planets['implausible']],
		'Holos': [pl.all_planets['doubtful'], pl.all_planets['unlikely'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Hypnotapes': [pl.all_planets['demolish'], pl.all_planets['doubtful'], pl.all_planets['unlikely'], pl.all_planets['crash']],
		'Katydidics': [pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['demolish'], pl.all_planets['wreck'], pl.all_planets['crash']],
		'Laboratories': [pl.all_planets['crash'], pl.all_planets['anacreon'], pl.all_planets['viand'], pl.all_planets['newsgroup']],
		'LanzariK': [pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Lasers': [pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Libraries': [pl.all_planets['anacreon'], pl.all_planets['unlikely'], pl.all_planets['crash']],
		'Livestock': [pl.all_planets['santanni']], # pl.all_planets['new street glide']],
		'LubOils': [pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Meats': [pl.all_planets['implausible'], pl.all_planets['divide'], pl.all_planets['bilk'], pl.all_planets['fisticuffs'], pl.all_planets['vantek']],
		'Mechparts': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['crash']],
		'MicroScalpels': [pl.all_planets['doubtful'], pl.all_planets['poveglia']],
		'Monopoles': [pl.all_planets['santanni'], pl.all_planets['terminus']],
		'Munitions': [pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Musiks': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful'], pl.all_planets['wreck']],
		'NanoFabrics': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['demolish']],
		'Nanos': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Nickel': [pl.all_planets['helicon'], pl.all_planets['doubtful'], pl.all_planets['demolish'], pl.all_planets['crash'], pl.all_planets['welch']],
		'Nitros': [pl.all_planets['improbable'], pl.all_planets['wreck'], pl.all_planets['crash']],
		'Petrochemicals': [pl.all_planets['eos'], pl.all_planets['terminus'], pl.all_planets['crash']],
		'Pharmaceuticals': [pl.all_planets['eos'], pl.all_planets['smyrno'], pl.all_planets['doubtful'], pl.all_planets['crash']],
		'Polymers': [pl.all_planets['anacreon'], pl.all_planets['crash']],
		'Powerpacks': [pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['demolish']],
		'Probes': [pl.all_planets['doubtful']],
		'Propellants': [pl.all_planets['doubtful'], pl.all_planets['demolish'], pl.all_planets['wreck']], # pl.all_planets['new street glide']],
		'Proteins': [pl.all_planets['viand'], pl.all_planets['poveglia'], pl.all_planets['kittygarden'], pl.all_planets['gervais']],
		'Radioactives': [pl.all_planets['doubtful'], pl.all_planets['demolish'], pl.all_planets['welch'], pl.all_planets['divide']], # , pl.all_planets['new street glide']
		'RNA': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Semiconductors': [pl.all_planets['terminus'], pl.all_planets['doubtful'], pl.all_planets['fisticuffs'], pl.all_planets['implausible'], pl.all_planets['welch'], pl.all_planets['divide']],
		'Sensamps': [pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Sensors': [pl.all_planets['anacreon'], pl.all_planets['doubtful'], pl.all_planets['newsgroup']],
		'Simulations': [pl.all_planets['cinna'], pl.all_planets['eos'], pl.all_planets['wreck']],
		'Soya': [pl.all_planets['santanni']], # pl.all_planets['new street glide']],
		'Spices': [pl.all_planets['terminus']],
		'Studios': [pl.all_planets['doubtful'], pl.all_planets['unlikely'], pl.all_planets['wreck']],
		'Synths': [pl.all_planets['doubtful']],
		'Textiles': [pl.all_planets['santanni'], pl.all_planets['implausible'], pl.all_planets['bilk'], pl.all_planets['divide'], pl.all_planets['fisticuffs'], pl.all_planets['email']],
		'Tools': [pl.all_planets['doubtful'], pl.all_planets['improbable'], pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'ToxicMunchers': [pl.all_planets['doubtful'], pl.all_planets['poveglia']],
		'TQuarks': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['demolish']],
		'Tracers': [pl.all_planets['viand'], pl.all_planets['crash']],
		'Univators': [pl.all_planets['doubtful'], pl.all_planets['wreck'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Vidicasters': [pl.all_planets['unlikely'], pl.all_planets['improbable'], pl.all_planets['doubtful']],
		'Weapons': [pl.all_planets['improbable'], pl.all_planets['doubtful'], pl.all_planets['demolish'], pl.all_planets['crash']],
		'Woods': [pl.all_planets['bilk'], pl.all_planets['herringbone'], pl.all_planets['wreck'], pl.all_planets['crash']],
		'Xmetals': [pl.all_planets['demolish'], pl.all_planets['bilk'], pl.all_planets['herringbone'], pl.all_planets['implausible'], pl.all_planets['zaldrizes']],
}



system_owners = {'shell': 'idiotjones',
		'total': 'johngradycole',
		'default': 'billyparham', 
		'chevron': 'jimmyblevins', 
		'gulf': 'toadvine',}


system_planets = {'shell': [pl.all_planets['improbable'], pl.all_planets['unlikely'], pl.all_planets['doubtful'], pl.all_planets['implausible'], pl.all_planets['dubious']],
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
