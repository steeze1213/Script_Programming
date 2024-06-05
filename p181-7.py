def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("factorial(5) =", factorial(5))
print("factorial(7) =", factorial(7))
print("factorial(10) =", factorial(10))
