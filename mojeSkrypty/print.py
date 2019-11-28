print('TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV')
print('TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=';')
print('I like computers', 'TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=' but better is ')

programName = 'BBC'
item = 'News'
time = '18.00'

print('I like watching', item, 'at', time, 'on', programName, '.') #here's a space after programName
print('I like watching', item, 'at', time, 'on', programName + '.') #here's no space after programName