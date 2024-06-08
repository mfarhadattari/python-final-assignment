# Write a python program to find out which word is vowel or consonant using function.

def is_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    return False

def is_vowel_or_consonant(word):
    try:
        if not isinstance(word, str):
            raise ValueError("Input must be a string.")
        result = {}
        for char in word:
            if char.isalpha():
                result[char] = 'Vowel' if is_vowel(char) else 'Consonant'
        return result
    except ValueError as ve:
        return str(ve)

# Example usage
value = input("Input: ")
print(is_vowel_or_consonant(value))
