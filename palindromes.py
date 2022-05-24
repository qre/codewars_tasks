word = 'Deleveled'
def is_palindrome(word):
    if (word.lower() == word[::-1].lower()):
        return 'Its a palindrome'
    else:
        return 'its not a palindrome'
print(is_palindrome(word))