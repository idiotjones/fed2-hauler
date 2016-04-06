from planet import planet
all_planets = {
	'improbable': planet('improbable', 'shell', 'darkness', 'Improbable Landing Pad', ['out'], ['in'], ['w'], ['e'], [], []),
	'unlikely': planet('unlikely', 'shell', 'darkness', 'Unlikely Landing Pad', ['se', 'out'], ['in', 'nw'], ['w'], ['e'], [], []),
	'doubtful': planet('doubtful', 'shell', 'darkness', 'Doubtful Landing Pad', ['sw'], ['ne'], ['w'], ['e'], [], []),
	'wreck': planet('wreck', 'total', 'sol', 'Wreck currently has the layout', [], [], ['n'], ['s'], ['e'], ['w']),
	'welch': planet('welch', 'default', 'sol', 'This is the hub of Welch;', [], [], ['e'], ['w'], ['sw'], ['ne']),
	'herringbone': planet('herringbone', 'chevron', 'sol', 'Ice planet Herringbone', [], [], ['sw'], ['ne'], ['s'], ['n']),

	'viand': planet('viand', 'darkness', 'darkness', '...', ['w'], ['e'], ['e', 'n'], ['s', 'w'], [], []),
	'vivid': planet('vivid', 'darkness', 'darkness', '...', ['n', 'n'], ['s', 's'], ['in', 'wear sunglasses', 'w'], ['e', 's', 'out'], [], []),
	'disco ball': planet('disco ball', 'disco', 'darkness', '...', [], [], ['s', 'w'], ['e', 'n'], [], []),
	'zaldrizes': planet('zaldrizes', 'dragon', 'darkness', '...', [], [], ['e'], ['w'], [], []),

	'anacreon': planet('anacreon', 'far star', 'far star', '...', ['w'], ['e'], ['e'], ['w'], [], []),
	'santanni': planet('santanni', 'far star', 'far star', '...', ['sw'], ['ne'], ['e'], ['w'], [], []),
	'smyrno': planet('smyrno', 'far star', 'far star', '...', [], [], ['e'], ['w'], [], []),
	'terminus': planet('terminus', 'far star', 'far star', '...', ['s'], ['n'], ['e'], ['w'], ['ne'], ['sw']),

	'helicon': planet('helicon', 'stars end', 'far star', '...', ['s'], ['n'], ['e'], ['w'], [], []),
	'cinna': planet('cinna', 'stars end', 'far star', '...', [], [], ['e'], ['w'], [], []),
	}
