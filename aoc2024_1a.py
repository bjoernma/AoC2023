def read_in(filename):
	content_list_a: list = []
	content_list_b: list = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			content_list_a.append(int(line.split()[0]))
			content_list_b.append(int(line.split()[1]))
	return content_list_a, content_list_b

def iterate_pairs(list_a, list_b) -> int:
	list_a.sort()
	list_b.sort()
	cumulated: int = 0
	diff: int = 0
	for entry_a, entry_b in zip(list_a, list_b):
		diff = abs(entry_a - entry_b)
		cumulated += diff
	return cumulated

def similarity_score(list_a, list_b) -> int:
	similarity_cumulated: int = 0
	similarity: int = 0
	for left_entry in list_a:
		similarity = int(left_entry) * int(list_b.count(int(left_entry)))
		similarity_cumulated += similarity
	return similarity_cumulated


list_a, list_b = read_in('aoc2024_1a.input')
print('total difference: ', iterate_pairs(list_a, list_b))
list_a, list_b = read_in('aoc2024_1a.input')
print('similarity: ', similarity_score(list_a, list_b))
