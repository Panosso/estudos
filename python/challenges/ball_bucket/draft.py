string1 = 'ABCDE FGHI'

string_list = [x for x in string1]

print('\n')
print('\n')
print(string_list)
string_list[1] = 'R'
print(''.join(string_list))