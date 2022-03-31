def get_count(sentence):
    count = 0
    for i in sentence:
        if str(i) = 'a':
            count += 1
        if sentence(i) = 'e':
            count += 1
        if sentence(i) = 'i':
            count += 1
        if sentence(i) = 'o':
            count += 1
        if sentence(i) = 'u':
            count += 1
    return count
Wrong

def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

