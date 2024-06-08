# Write a python program to display the multiplication table.

def multiplication_table(n):
    try:
        n = int(n)
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Example usage
n = input("n = ")
multiplication_table(n)
