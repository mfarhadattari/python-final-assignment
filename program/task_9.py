# Write a python function that takes a number as input and returns whether it's a prime number or not.

def is_prime(n):
    try:
        n = int(n)
        if n <= 1:
            return False
        elif n == 2:
            return True
        else: 
            for i in range(2, n):
                if(n % i == 0):
                    return False
            return True
    except ValueError:
        return "Invalid input. Please enter an integer."


# Example usage
n = input("n = ")
print(is_prime(n))
