#3LAB10ARC

#function for the palindrome
def is_palindrome(string_input, start=0, end=-1):
    
    if start >= end:
        return True

    #while loop ignoring non-alphabetic characters and case
    while not string_input[start].isalpha():
        start += 1
    while not string_input[end].isalpha():
        end -= 1

    if string_input[start].lower() != string_input[end].lower():
        return False

    return is_palindrome(string_input, start + 1, end - 1)

#function to count the vowels and consonants
def count_vowels_consonants(string_input, index=0, vowel_count=0, consonant_count=0):
  
    if index == len(string_input):
        return vowel_count, consonant_count

    if string_input[index].isalpha():
        if string_input[index].lower() in 'aeiou':
            vowel_count += 1
        else:
            consonant_count += 1

    return count_vowels_consonants(string_input, index + 1, vowel_count, consonant_count)

#main function with the input and the display
def main():
    string_input = input("Enter a string: ")

    if is_palindrome(string_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    vowels, consonants = count_vowels_consonants(string_input)
    if vowels > consonants:
        print("The string has more vowels than consonants.")
    else:
        print("The string has more or equal consonants than vowels.")

main()