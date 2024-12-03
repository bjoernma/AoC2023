import re

def read_file(filename: str):
	with open(filename, 'r', encoding='utf-8') as f:
		linenumber = 0
		for line in f:
			yield line
#			if linenumber == 0:
#				newline = 'do()' + line
#				linenumber += 1
#			else:
#				newline += line
##		return newline
##		print(f'{newline=}')
#		dont_do_split: list = re.split(r'don\'t\(\)|do\(\)', newline)
#		only_active_strings: list = [x for idx, x in enumerate(dont_do_split) if idx % 2 == 1]
#		return only_active_strings
#		for string in only_active_strings:
#			print(f'yield {string=}')
#			yield string
# import re;re.split(r'don\'t\(\)|do\(\)', test)


def search_matches(line: str) -> list[str]:
	return re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)


def calc_mul(single_match: str):
	a = single_match.split('(')[1].split(',')[0]
	b = single_match.split('(')[1].split(',')[1].split(')')[0]
	return int(a)*int(b)


def main():
	total: int = 0
	active: bool = True
	for string in read_file('aoc2024_3a.input'):
		for single_match in search_matches(string):
			if single_match == 'don\'t()':
				active = False
			elif single_match == 'do()':
				active = True
			else:
				if active:
					total += calc_mul(single_match)
			print(f'{single_match=}')
#			total += calc_mul(single_match)
			print(f'new {total=}')
	print(f'Total is {total=}')

main()
