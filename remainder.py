# Write a program to read two numbers and print their quotient and remainder.

# dividend / divisor = quotient

def QuotientRemainder(n, x):
    quotient = int(n / x)
    remainder = int(n % x)
    return quotient, remainder


result = QuotientRemainder(6, 4)
print(result)
