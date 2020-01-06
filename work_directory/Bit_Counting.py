# Write a function that takes an integer as input, and returns the number of bits
# that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010,
# so the function should return 5 in this case

n = 1234

def countBits(n):
    sums = 0
    numb = bin(n)[2:]
    for num in numb:
        if num == '1':
            sums += 1
    return sums

print(countBits(n))

# CODEWARS
# def countBits(n):
#     return bin(n).count("1")