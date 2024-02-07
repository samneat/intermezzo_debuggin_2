def factorial(n):
    product = 1
    while n >= 2:
        product *= n
        n -= 1
    return product

print(factorial(5))

