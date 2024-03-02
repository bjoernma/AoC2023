import itertools


def main():
	galaxies: list = []
	non_empty_rows: list = []
	non_empty_lines: list = []
	#with open('aoc2023_11a.test', 'r') as f:
	with open('aoc2023_11a.input', 'r') as f:
		for linenumber, line in enumerate(f):
			for rownumber, character in enumerate(line):
				if character == '#':
					galaxies.append((linenumber, rownumber))
					non_empty_rows.append(rownumber)
					non_empty_lines.append(linenumber)
		len_lines = linenumber
		len_rows = rownumber
	non_empty_rows = set(non_empty_rows)
	non_empty_lines = set(non_empty_lines)
	print(f'{galaxies=}')
	print(f'{non_empty_rows=}')
	print(f'{non_empty_lines=}')
	empty_rows = invert_list(non_empty_rows, len_rows)
	empty_lines = invert_list(non_empty_lines, len_lines)
	print(f'{empty_rows=}')
	print(f'{empty_lines=}')
	print(f'{len_rows=}')
	print(f'{len_lines=}')
	total_length = 0
	for pair in generate_pairs(galaxies):
		for i in pair:
			length = calculate_diff(i, empty_rows, empty_lines)
			total_length += length
			print(f'{i=}: {length=}')
	print(f'{total_length=}')



def invert_list(data, len_a):
	out: list = []
	for i in range(len_a):
		if i not in data:
			out.append(i)
	return out

def generate_pairs(galaxies):
	print(len(galaxies))
	yield itertools.combinations(galaxies, 2)

def calculate_diff(j, ignore_row, ignore_line):
	cnt_expansion = 0
#	print(j)
	a1 = j[0][0]
	a2 = j[0][1]
	b1 = j[1][0]
	b2 = j[1][1]
	cnt_row = 0
	cnt_line = 0
	
	for i in range(min(a1,b1), max(a1,b1)+1):
#		print(f'range {a1=} to {b1=}. now at {i=}')
		cnt_line += 1
		if i in ignore_line:
			cnt_expansion += 1
#			print(f'expanded on line {i=}')
	for i in range(min(a2,b2), max(a2,b2)+1):
		cnt_row += 1
#		print(f'range {a2=} to {b2=}. now at {i=}')
		if i in ignore_row:
			cnt_expansion += 1
#			print(f'Expanded on row {i=}')
	#return abs(b1-a1+1) + abs(b2-a2+1) + cnt_expansion
	return cnt_row + cnt_line + cnt_expansion - 2

main()
