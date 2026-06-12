word = input("Enter a word: ")

# Convert to lowercase for fair comparison (Madam == madam)
word_lower = word.lower()

# Reverse the lowercased word
reversed_word = word_lower[::-1]

# Compare original (lowercase) with reversed
if word_lower == reversed_word:
    print(f"'{word}' is a Palindrome ✓")
else:
    print(f"'{word}' is NOT a Palindrome ✗")