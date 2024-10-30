# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def count_bits(n):

    if n < 0:
        raise ValueError('Valor negativo')
    
    else:

        binary_n = ''
        result = 0

        while n >= 2:

            binary_n += str(n % 2)
            n = int(n/2)

        if n == 1:
            binary_n += '1'

        for i in binary_n:
            result += int(i)
        
        return result
