def unique_in_order(sequence):

    unique_order = []
    for i in range(0, len(sequence)):

        if i == 0:
            unique_order.append(sequence[i])
        elif i != 0 and sequence[i] != sequence[i-1]:
                unique_order.append(sequence[i])

    return unique_order
    
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
unique_in_order('AAAABBBCCDAABBB') == ["A", "B", "C", "D", "A", "B"]
