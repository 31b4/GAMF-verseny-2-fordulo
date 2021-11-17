t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
convertIt = "xrvzibtwzzsduvpygpziluequciojomx"
new = convertIt[0]
for i in range(1,len(convertIt)):
    newI = (26 - t.index(new[len(new)-1])) + t.index(convertIt[i])
    if newI>26:
        newI %= 26
    new+=t[newI-1]
print(new)