import re

def read_file(filename: str):
    for line in open(filename, 'r'):
        line = line.strip()
        yield line


translation: dict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9',}
summe: int = 0
for line in read_file('aoc2023_1b.test'):
#for line in read_file('aoc2023_1a.input'):
    index_a: dict = {}
    index_b: dict = {}
    for key in translation:
        index_a[key] = line.find(key)
        index_b[key] = line.rfind(key)
    pos_b = index_b[max(index_b, key=index_b.get)]
    for idx in index_a:
        if index_a[idx] == -1:
            index_a[idx] = 99
    pos_a = index_a[min(index_a, key=index_a.get)]
    if pos_b == -1 and pos_a == 99: # no replacements
        newline = line
    else:
        last = max(index_b, key=index_b.get)
        first = min(index_a, key=index_a.get)
        newline = line[:pos_a] + translation[first] + line[pos_a+len(first):pos_b] + translation[last] + line[pos_b+len(last):]
    number = re.sub(r'[a-zA-Z]+', '', newline)
    summe += int(number[0])*10 + int(number[-1])# 1a

print('result: ', summe) # a.test should result in 142 b.testt should result in 281

# 54154 is to low for 1b
# problem is that the replacement is in the order of the translation-dict, but should be in order of the input string, e.g. eightwo should become 8wo
# Ich kann nicht einfach nur die erste und letzte ausgeschriebene Ziffer nehmen. Da können ja auch echte Ziffern vor/hinter kommen...
# summe += int(first)*10 + int(last)
# 54637 is too low: vorne/hinten selbe Ziffer funktioniert noch nicht
# 54691 is not right: wenn nur 1 Ziffer da ist, wird Output merkwürdig.
