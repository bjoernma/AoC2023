import re

def read_file(filename: str):
    for line in open(filename, 'r'):
        yield line


summe: int = 0
for line in read_file('aoc2023_1a.input'):
    number = re.sub(r'[a-zA-Z]+', '', line).strip()
    summe += int(number[0])*10 + int(number[-1])

print(summe) # aoc2023_1a.test should result in 142
