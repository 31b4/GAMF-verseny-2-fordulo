t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
convertIt = "program"
new =convertIt[0]
for i in range(1,len(convertIt)):
    newI = (t.index(convertIt[i-1])+1) + (t.index(convertIt[i])+1)
    if newI>26:
        newI %= 26
    new+=t[(newI)-1]
print(new)