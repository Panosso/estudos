# In this challenge you need to create a function that return a list with 1 character from a list.
# for example:
#   ['AAAABBBBCCCCccDDEEEeAA'] = ['A', 'B', 'C', 'c', 'D', 'E', 'e', 'A']

def unique_in_order(sequence):

    unique_order = []
    for i in range(0, len(sequence)):

        if i == 0:
            unique_order.append(sequence[i])
        elif i != 0 and sequence[i] != sequence[i-1]:
                unique_order.append(sequence[i])

    return unique_order
    
print(unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
print(unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3])
print(unique_in_order('AAAABBBCCDAABBB') == ["A", "B", "C", "D", "A", "B"])
