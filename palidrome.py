# A palidrome is a word, phrase. number or sequence of characters that reads the same forward and backward.

# e.g "madam", "racecar", "12321"

# The function char.isalnum() returns True if all the characters are alphanumeric, meaning alphabet letter(a-z) and numbers(0-9).
# "A".isalnum() returns True
# "!".isalnum() returns False
# " ".isalnum() returns False
# "Hello123".isalnum() returns True
# "Hello 123".isalnum() returns False

import streamlit as st 

def is_palindrome(word):
    cleaned_word = "".join(char.lower() for char in word if char.isalnum()).lower()
    return cleaned_word == cleaned_word[::-1]

st.title("Palindrome Checker")

word = st.text_input("Enter a word or phrase to check if it is a palindrome")

if st.button("Check"):
    if word:
        if is_palindrome(word):
            st.success(f"{word} is a palindrome")
        else:
            st.write(f"{word} is not a palindrome")
