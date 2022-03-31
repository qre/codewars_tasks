# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

#1: 
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

#2: - does that even work?
text = '1312kjbfkdsskfdjshddf37834fhu34fn34489398398c39m3x'

def duplicate_count(text):
    seen = set()
    dupes = set()
    print(seen)
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
        print(seen)
    print(len(dupes))
    return len(dupes)

#3:
def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
#4:
def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for i in text:
        if text.count(i) > 1 and i not in duplicates:
            duplicates.append(i)    
    return len(duplicates)