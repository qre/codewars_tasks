people = 'gap'

def wave(people):
    arr = []
    for i in range(len(people)):
        new_word = list(people)
        if new_word[i] == ' ':
            continue
        new_word[i] = people[i].upper()
        arr.append("".join(new_word))
    return arr
print(wave(people))
