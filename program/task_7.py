# Write a python program to find the factorial of a number using function.

def factorial(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    except ValueError as ve:
        return str(ve)

# Example usage
n = input("n = ")
print(factorial(n))
