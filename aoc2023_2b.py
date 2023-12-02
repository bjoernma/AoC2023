def readline(filename: str):
    for line in open(filename, 'r'):
        line.strip()
        yield line

id_summe: int = 0
color_limit: dict = {'red': 12, 'green': 13, 'blue': 14}
#for line in readline('aoc2023_2a.test'):
for line in readline('aoc2023_2a.input'):
    print('------- NEW LINE ----------')
    game_id = int(line.split(':')[0].split(' ')[-1])
    print(f'{game_id=}')
    break_switch: bool = False
    for game_set in line.split(':')[1].split(';'):
        print('------- NEW SET ----------')
        color_count: dict = {'red': 0, 'green': 0, 'blue': 0}
        print(f'{game_set=}')
        for color in game_set.split(','):
            color = color.strip()
            print(f'{color=}')
            color_count[color.split(' ')[-1]] += int(color.split(' ')[0])
            
        print(f'{color_count=}')
        # for each set check whether its numbers are too high
        for val, idx in enumerate(color_count):
            print(f'{idx=}, {val=}')
            if color_count[idx] > color_limit[idx]:
                print(f'Numbers too high: {color_count=}')
                break_switch = True
                break
    if not break_switch:
        print(f'{color_count=}')
        id_summe += game_id
    print(f'{id_summe=}')
print(f'{id_summe=}')
