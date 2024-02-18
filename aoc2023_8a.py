def read_rl():
	with open('aoc2023_8a.input', 'r') as f:
		for line in f:
			string = line.strip()
			return string

def read_azmap():
	azmap = {}
	with open('aoc2023_8a.input', 'r') as f:
		for line in f:
			if '=' in line:
				label = line.split('=')[0].strip()
				first = line.split('(')[1].strip().split(',')[0].strip()
				second = line.split('(')[1].strip().split(',')[1].strip(')\s').strip()
				l = [first, second]
				azmap[label] = l
	return azmap

#rllist = 'RL'
#azmap = {'AAA': ['BBB','CCC'],
#				'BBB': ['DDD','EEE'],
#				'CCC': ['ZZZ','GGG'],
#				'DDD': ['DDD','DDD'],
#				'EEE': ['EEE','EEE'],
#				'GGG': ['GGG','GGG'],
#				'ZZZ': ['ZZZ','ZZZ'],
#				}

rllist = 'LLR'
azmap = {
'AAA': ['BBB', 'BBB'],
'BBB': ['AAA', 'ZZZ'],
'ZZZ': ['ZZZ', 'ZZZ'],
}

rllist = read_rl()
azmap = read_azmap()
print(f'{rllist=} {azmap=}')

rllist = rllist.replace('R', '1').replace('L', '0')
current = 'AAA'
current_idx_list = 0
counter = 0
while current != 'ZZZ':
	print(f'{current=} {current_idx_list=} {rllist[current_idx_list]=} {azmap[current]=}')
	current = azmap[current][int(rllist[current_idx_list])]
	if current_idx_list >= len(rllist) - 1:
		current_idx_list = 0
	else:
		current_idx_list += 1
	print(current)
	counter += 1
print(counter)
