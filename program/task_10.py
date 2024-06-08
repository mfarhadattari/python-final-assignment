# Write python program to swap two numbers using function.

def swap(a, b):
    try:
        a, b = float(a), float(b)
        return b, a
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
a, b = input("a = "), input("b = ") 
print(swap(a, b))
