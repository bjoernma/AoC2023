def read_line(filename: str):
    for line in open(filename, 'r'):
        line = line.strip()
        winning_numbers = line.split('|')[0].strip().split(':')[1].strip()
        have_numbers = line.split('|')[1].strip()
        win_list = winning_numbers.split(' ')
        have_list = have_numbers.split(' ')
        yield (win_list, have_list)

def count_winning():
    total: int = 0
    card_counting:dict = dict()
    line_count: int = 0
    counter_per_line_list:list = list()
    for (winning_numbers, have_numbers) in read_line('aoc2023_4a.input'):
    #for (winning_numbers, have_numbers) in read_line('aoc2023_4a.test'):
        card_counting[line_count] = 1
        print(f'{winning_numbers=}')
        print(f'{have_numbers=}')
        counter_per_line: int = 0
        for number in have_numbers:
            if number in winning_numbers and number != '':
                counter_per_line += 1
        counter_per_line_list.append(counter_per_line)
        print(counter_per_line_list)
        line_count += 1
    return counter_per_line_list

def count_total(l: dict):
    total: int = 0
    for i in l:
        total += l[i]
    return total

def iterate_card_count(card_input: list):
    length = len(card_input)
    card_count: dict = {i: 1 for i,val in enumerate(card_input)}
    print(card_count)
    for i in range(length):
        print(f'{i=},{card_input[i]=}')
        for j in range(i+1, i+1+card_input[i]):
            print(i,j)
            card_count[j] += card_count[i]
            print(card_count)
        print(card_count)
    print(card_count)
    return card_count

l=count_winning()
print('-----')
card_count = iterate_card_count(l)
print(count_total(card_count))
