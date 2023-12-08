def read_line(filename: str):
    for line in open(filename, 'r'):
        line = line.strip()
        winning_numbers = line.split('|')[0].strip().split(':')[1].strip()
        have_numbers = line.split('|')[1].strip()
        win_list = winning_numbers.split(' ')
        have_list = have_numbers.split(' ')
        yield (win_list, have_list)


total: int = 0
#for (winning_numbers, have_numbers) in read_line('aoc2023_4a.test'):
for (winning_numbers, have_numbers) in read_line('aoc2023_4a.input'): # 126642 is too high
    print(f'{winning_numbers=}')
    print(f'{have_numbers=}')
    counter_per_line: int = 0
    for number in have_numbers:
        if number in winning_numbers and number != '':
            counter_per_line += 1
    if counter_per_line > 0:
        total += 2 ** (counter_per_line-1)

print(total)
