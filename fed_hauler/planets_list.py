from planet import planet
all_planets = {
	'improbable': planet('improbable', 'shell', 'shell', 'Improbable Landing Pad', ['out'], ['in'], ['w'], ['e'], [], []),
	'unlikely': planet('unlikely', 'shell', 'shell', 'Unlikely Landing Pad', ['se', 'out'], ['in', 'nw'], ['w'], ['e'], [], []),
	'doubtful': planet('doubtful', 'shell', 'shell', 'Doubtful Landing Pad', ['sw'], ['ne'], ['w'], ['e'], [], []),
	'dubious': planet('dubious', 'shell', 'shell', 'Doubtful Landing Pad', ['nw'], ['se'], ['w'], ['e'], [], []),
	'implausible': planet('implausible', 'shell', 'shell', 'Unlikely Landing Pad', ['ne', 'out'], ['in', 'sw'], ['w'], ['e'], [], []),

	'welch': planet('welch', 'default', 'shell', 'This is the hub of Welch;', [], [], ['e'], ['w'], ['sw'], ['ne']),
	'bilk': planet('bilk', 'default', 'shell', '', ['w'], ['e'], ['e'], ['w'], ['sw'], ['ne']),

	'herringbone': planet('herringbone', 'chevron', 'shell', 'Ice planet Herringbone', [], [], ['sw'], ['ne'], ['s'], ['n']),

	'wreck': planet('wreck', 'total', 'shell', 'Wreck currently has the layout', [], [], ['n'], ['s'], ['e'], ['w']),
	'demolish': planet('demolish', 'total', 'shell', '...', ['w'], ['e'], ['n'], ['s'], ['e'], ['w']),
	'crash': planet('crash', 'total', 'shell', '...', ['sw'], ['ne'], ['sw'], ['ne'], [''], ['']),

	'divide': planet('divide', 'gulf', 'shell', 'Divide is currently just another Magrathea-built rock', [], [], ['s', 'w'], ['e', 'n'], ['s', 's'], ['n', 'n']),

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
	'eos': planet('eos', 'stars end', 'far star', '...', ['w'], ['e'], ['e'], ['w'], [], []),

	'email': planet('email', 'internet', 'internet', '...', ['w'], ['e'], ['e'], ['w'], ['s'], ['n']),
	'newsgroup': planet('newsgroup', 'internet', 'internet', '...', ['s'], ['n'], ['e'], ['w'], ['sw'], ['ne']),
	
	'maminar': planet('maminar', 'hof', 'ice', '...', ['e'], ['w'], ['s', 's', 's'], ['n', 'n', 'n'], ['s', 's', 's'], ['n', 'n', 'n']),
	'vantek': planet('vantek', 'hof', 'ice', '...', ['sw'], ['ne'], ['d', 'in', 'out', 'u'], ['d', 'in', 'out', 'u'], ['d', 'in', 'out', 'u'], ['d', 'in', 'out', 'u']),

	'new street glide': planet('new street glide', 'bikes', 'ice', 'New Street Glide', [], [], ['n'], ['s'], ['e'], ['w']),
	'ultra limited': planet('ultra limited', 'bikes', 'ice', 'Ultra Limited', ['s'], ['n'], ['sw'], ['ne'], ['s'], ['n']),

	'valisk': planet('valisk', 'ombey', 'havefun', '...', [], [], ['s', 'e'], ['w', 'n'], ['w'], ['e']),

	'poveglia':  planet('poveglia', 'meadows', 'havefun', '...', ['s', 'e', 'e'], ['w', 'w', 'n'], ['w'], ['e'], ['n', 'n'], ['s', 's']),
	'goldenshoe':  planet('goldenshoe', 'meadows', 'havefun', '...', ['s', 'e'], ['w', 'n'], ['w'], ['e'], ['n', 'w', 'w', 'nw', 'n', 'n', 'n', 'e'], ['w', 's', 's', 's', 'se', 'e', 'e', 's']),
	'fisticuffs':  planet('fisticuffs', 'meadows', 'havefun', '...', ['n', 'e'], ['w', 's'], ['w'], ['e'], [], []),
	}
