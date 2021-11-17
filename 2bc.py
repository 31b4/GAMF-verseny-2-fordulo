with open('input.txt') as f:
    lines = f.readlines()
szavak = []
szavakCounter = []
for line in lines:
    for word in line.split(' '):
        if len(word)<6:
            continue
        if word in szavak:
            szavakCounter[szavak.index(word)] +=1
        else:
            szavak.insert(len(szavak), word)
            szavakCounter.insert(len(szavakCounter), 1)
print(szavak[szavakCounter.index(max(szavakCounter))])
print(max(szavakCounter))