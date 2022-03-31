def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

def friend(x):
    return [f for f in x if len(f) == 4]

