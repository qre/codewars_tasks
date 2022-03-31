#my solution:
def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

#best voted solutions:
def friend(x):
    return [f for f in x if len(f) == 4]

