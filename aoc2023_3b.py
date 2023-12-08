import numpy as np

def find_symbol(data:np.full, line_counter: int, start_index:int, end_index:int, max_line_counter, max_char_counter):
    start_index = int(start_index)
    end_index = int(end_index)
    line_counter = int(line_counter)
    max_line_counter = int(max_line_counter) - 1
    max_char_counter = int(max_char_counter) - 1
    print(f'{max_line_counter=}, {max_char_counter=}')
    print(f'{line_counter=}, {start_index_current_number=}, {end_index_current_number=}')
    not_symbol_tuple: tuple = ('0','1','2','3','4','5','6','7','8','9','','.')

    # rund um start_index
    print(f'{line_counter=}, {start_index=}')
    print(data)
    if ((line_counter > 0) and (data[line_counter-1][start_index] not in not_symbol_tuple)):
        print('opt 1a')
        return True
    if ((line_counter < max_line_counter) and (data[line_counter+1][start_index] not in not_symbol_tuple)):
        print('opt 1')
        return True
    if start_index > 0:
        if (line_counter > 0 and data[line_counter-1][start_index-1] not in not_symbol_tuple):
            print('opt 2a')
            return True
        if (data[line_counter][start_index-1] not in not_symbol_tuple):
            print('opt 2b')
            return True
        if (line_counter < max_line_counter and data[line_counter+1][start_index-1] not in not_symbol_tuple):
            print('opt 2c')
            return True


    # rund um end_index
    print(f'around end index. {line_counter=}, {end_index=}, {data[line_counter-1][end_index]=}')
    if (line_counter > 0 and data[line_counter-1][end_index] not in not_symbol_tuple):
        print('opt 3a')
        return True
    if (line_counter < max_line_counter and data[line_counter+1][end_index] not in not_symbol_tuple):
        print('opt 3b')
        return True
#    print(f'around end index. {line_counter=}, {end_index=}, {max_char_counter=}, {data[line_counter+1][end_index+1]=}')
    if end_index < max_char_counter:
        if ((line_counter > 0) and (data[line_counter-1][end_index+1] not in not_symbol_tuple)):
            print('opt 4a')
            return True
        if (data[line_counter][end_index+1] not in not_symbol_tuple):
            print('opt 4b')
            return True
        if (line_counter < max_line_counter and data[line_counter+1][end_index+1] not in not_symbol_tuple):
            print('opt 4')
            return True



    # Mitte
    if abs(end_index - start_index) > 1:
        for i in range(start_index, end_index+1):
            if line_counter > 0 and data[line_counter-1][i] not in not_symbol_tuple:
                print('opt 5')
                return True
            if line_counter < max_line_counter and data[line_counter+1][i] not in not_symbol_tuple:
                print('opt 6')
                return True
    print('opt 7')
    return False
    
filename: str = 'aoc2023_3a.test'
filename: str = 'aoc2023_3a.input'  # 408025 is too low, 421765 is too low, 506727 is too low. 509115 somehow works now.
max_line_counter: int = 0
max_char_counter: int = 0
for line in open(filename, 'r'):
    line = line.strip('\n')
    max_line_counter += 1
    if max_char_counter == 0:
        for char in line:
            max_char_counter += 1

print(max_line_counter, '  ', max_char_counter)
data = np.full(shape=(max_line_counter, max_char_counter), fill_value='', dtype='str')

line_counter = 0
for line in open(filename, 'r'):
    line = line.strip()
    line_counter += 1
    char_counter = 0
    for char in line:
        char_counter += 1
        if char == '.':
            continue
        else:
            data[line_counter-1][char_counter-1] = char



summe: int = 0
current_number: str = ''
start_index_current_number = None
end_index_current_number = None
line_counter = 0

for line in data:
    char_counter = 0
    for char in line:
        if char_counter == 0:  # erster Buchstabe in Reihe
            if char in ('0','1','2','3','4','5','6','7','8','9'):
                current_number = str(char)
                start_index_current_number = 0
                end_index_current_number = 0
            else:
               current_number = ''
        else:  # nicht der erste Buchstabe
            if char in ('0','1','2','3','4','5','6','7','8','9'):
                current_number += str(char)
                if data[line_counter][char_counter-1] not in ('0','1','2','3','4','5','6','7','8','9'):
                    print('in symbol')
                    start_index_current_number = char_counter 
                    end_index_current_number = char_counter
                else:
                    end_index_current_number = char_counter
                if char_counter == max_char_counter-1:
                    print('last char number')
                    has_symbol = False
                    has_symbol:bool = find_symbol(data, line_counter, start_index_current_number, end_index_current_number, max_line_counter, max_char_counter)
                    if has_symbol:
                        print('has symbol')
                        summe += int(current_number)
                    else:
                        print('no symbol')
                    current_number = ''
            else:  # aktuell ist keine Ziffer
                if data[line_counter][char_counter-1] in ('0','1','2','3','4','5','6','7','8','9'):
                    print(f'{line_counter=}, {char_counter=}, {start_index_current_number=}, {end_index_current_number=}')
                    has_symbol = False
                    has_symbol:bool = find_symbol(data, line_counter, start_index_current_number, end_index_current_number, max_line_counter, max_char_counter)
                    if has_symbol:
                        print('has symbol')
                        summe += int(current_number)
                    else:
                        print('no symbol')
                    current_number = ''
                else: # thats a symbol
                    start_index_current_number = char_counter
                    end_index_current_number = char_counter
                    current_number = ''
        char_counter += 1
        print(f'{current_number=}. {summe=}.')
    line_counter += 1


print(data)
print(summe)

