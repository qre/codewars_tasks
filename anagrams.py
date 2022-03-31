word = 'word'
words = ['wdor', 'owrd', 'wdwdsa', 'drow']
def anagrams(word, words):
    anagr = []
    #s_word = ["".join(sorted(word))]
    s_word = sorted(word)
    s_word2 = ''.join(map(str, s_word))
    print(s_word2)
    #new_words = [','.join(sorted(x.split(','))) for x in words]
    for i in range(len(words)):
            if words.count(s_word2) > 0:
                anagr.append(words[i])
            else:
                pass
    return anagr
#anagrams(word,words)

     #if sorted(word) in new_words:
wrd = ['sdaknad', 'owgokeew', 'sddrgcsg']
def join_bs(wrd):
    word = [sorted(x.split(',')) for x in wrd]
    words = [','.join(sorted(x.split(','))) for x in wrd]
    words2 = [','.join((x.split(','))) for x in wrd]
    print(word)
    print(words)
    print(words2)
#join_bs(wrd)

def words_sorting(words):
    x=[]
    for i in words:
        x.append(sorted(words[i]))
    return x
words_sorting(words)

