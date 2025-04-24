# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

# Codewars solution: n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):

    string_n = str(n)
    sum = 0

    for i in range(0, len(string_n)):
        sum += int(string_n[i])

    if sum > 9:
        sum = digital_root(sum)

    return sum
