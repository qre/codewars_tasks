def maskify(cc):
    mask = ''
    for i in cc:
        mask += '#'
        if len(cc) <= 4:
            mask += str(i)
    return mask
wrong

def maskify(cc):
  
  word = list(cc)
  #loop through the list except the last 4 index's this will also prevent
  #the loop from running for anything less than 5 index's long
  for i in range(len(word) - 4):
    word[i] = '#'
  # join and return the list
  return ''.join(word)
  pass