# Write a python program to find the largest of three numbers.
def largest_of_three(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
a, b, c = input("A= "), input("B= ") ,input("C= ")
print(largest_of_three(a, b, c))
