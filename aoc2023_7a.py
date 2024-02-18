import pandas as pd
import re
pd.set_option('display.max_rows', 1000)
def inp():
	l2 = []
	#with open('aoc2023_7a.test', 'r') as f:
	with open('aoc2023_7a.input', 'r') as f:
# first answer 250093275 is too low
# though 250049986 wont fit either > replace AKQJT by A-E
# though 249450228 wont fit either > have the sorting better
# 251550272 doesnt fit either..
# there was a wrong twopair condition. 250957639 is correct for 7a.
		for line in f:
			#print(line)
			hand = line.split()[0].strip().replace('A','E').replace('K','D').replace('Q','C').replace('J','1').replace('T','A')
			bid = line.split()[1].strip()
			l1 = [hand, bid]
			l2.append(l1)
			#print(l2)
	#AKQJT98765432
	return pd.DataFrame(l2, columns=['hand','bid'])
#pd.DataFrame([['32T3K','765'],['T55J5','684'],['KK677','28'],['KTJJT','220'],['QQQJA','483']], columns=['hand','bid'])

def get_type(entry):
	oldcounter = dict()
	for i in entry:
		oldcounter[i] = oldcounter.get(i, 0) + 1
	counter = dict()
	for i in entry:
		counter[i] = counter.get(i, 0) + 1
	
	#print(counter)
	#print(len(counter))
	#print(counter[list(counter.keys())[0]])
	if counter[list(counter.keys())[0]] == 5:
		typestr = 'five'
		prio = 7
	elif counter[list(counter.keys())[0]] == 4 or counter[list(counter.keys())[1]] == 4:
		if '1' in entry:
			typestr = 'five'
			prio = 7
		else:
			typestr = 'four'
			prio = 6
	elif (counter[list(counter.keys())[0]] == 3 and counter[list(counter.keys())[1]] == 2) or (counter[list(counter.keys())[0]] == 2 and counter[list(counter.keys())[1]] == 3):
		if '1' in entry:
			if entry.count('1') == 3:
				typestr = 'five'
				prio = 7
			elif entry.count('1') == 2:
				typestr = 'five'
				prio = 7
			else:
				print('ERROR FULLHOUSE')
		else:
			typestr = 'fullhouse'
			prio = 5
	elif counter[list(counter.keys())[0]] == 3 or counter[list(counter.keys())[1]] == 3 or counter[list(counter.keys())[2]] == 3:
		if '1' in entry:
			if entry.count('1') == 2:
				typestr = 'five'
				prio = 7
			else:
				typestr = 'four'
				prio = 6
		else:
			typestr = 'three'
			prio = 4
	elif (
		(counter[list(counter.keys())[0]] == 2 and counter[list(counter.keys())[1]] == 2) 
		or (counter[list(counter.keys())[0]] == 2 and counter[list(counter.keys())[2]] == 2) 
		or (counter[list(counter.keys())[1]] == 2 and counter[list(counter.keys())[2]] == 2)
		):
		if '1' in entry:
			if entry.count('1') == 2:
				typestr = 'four'
				prio = 6
			else:
				typestr = 'fullhouse'
				prio = 5
		else:
			typestr = 'twopair'
			prio = 3
	elif counter[list(counter.keys())[0]] == 2 or counter[list(counter.keys())[1]] == 2 or counter[list(counter.keys())[2]] == 2 or counter[list(counter.keys())[3]] == 2:
		if '1' in entry:
			typestr = 'three'
			prio = 4
		else:
			typestr = 'pair'
			prio = 2
	else:
		if '1' in entry:
			typestr = 'pair'
			prio = 2
		else:
			typestr = 'high'
			prio = 1
	#print(typestr)
	return typestr, prio, counter 

def get_rank(idx, bid):
	return (int(idx) + 1 ) * int(bid)

data = inp()
data['type'] = data.apply(lambda row: get_type(row.hand)[0], axis=1)
data['typeprio'] = data.apply(lambda row: get_type(row.hand)[1], axis=1)
data['counter'] = data.apply(lambda row: get_type(row.hand)[2], axis=1)
data['firstcard'] = data.apply(lambda row: row.hand[0], axis=1)
data['secondcard'] = data.apply(lambda row: row.hand[1], axis=1)
data['thirdcard'] = data.apply(lambda row: row.hand[2], axis=1)
data['fourthcard'] = data.apply(lambda row: row.hand[3], axis=1)
data['fifthcard'] = data.apply(lambda row: row.hand[4], axis=1)
#print(data)
sortdata = data.sort_values(by=['typeprio', 'firstcard', 'secondcard', 'thirdcard', 'fourthcard', 'fifthcard'], axis=0, ignore_index=True, ascending=True)
print(sortdata[['hand','counter', 'type']])
sortdata['idx'] = sortdata.index
sortdata['rank'] = sortdata.apply(lambda row: get_rank(row.idx, row.bid), axis=1)

print(sortdata['rank'].sum())
