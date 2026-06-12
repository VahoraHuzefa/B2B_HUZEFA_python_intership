word = input("Enter a word: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for char in word:
    if char in vowels:
        vowel_count += 1

print(f"Vowels = {vowel_count}")
