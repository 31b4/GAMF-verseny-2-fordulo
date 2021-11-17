t = ['g', 'q', 'h', 'v', 't', 'y', 'a', 'c', 'n', 'z', 'l', 'k', 'm', 'i', 'r', 'p', 'b', 'o', 's', 'u', 'x', 'd', 'e', 'f', 'j', 'w']
convertIt = "tutgabjbavhwnoqfecvxbqvbddkpsqlw"
new = convertIt[0]
for i in range(1,len(convertIt)):
    newI = (26 - t.index(new[len(new)-1])) + t.index(convertIt[i])
    if newI>26:
        newI %= 26
    new+=t[newI-1]
print(new)