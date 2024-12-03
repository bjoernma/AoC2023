import re

def read_file(filename: str):
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			yield line


def search_matches(line: str) -> list[str]:
	return re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)


def calc_mul(single_match: str):
	a = single_match.split('(')[1].split(',')[0]
	b = single_match.split('(')[1].split(',')[1].split(')')[0]
	return int(a)*int(b)


def main():
	total: int = 0
	for line in read_file('aoc2024_3a.input'):
		for single_match in search_matches(line):
			total += calc_mul(single_match)
	print(f'Total is {total=}')

main()
