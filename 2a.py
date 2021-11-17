massalhangzok =['g', 'q', 'h', 'v', 't', 'y', 'c', 'n', 'z', 'l', 'k', 'm', 'r', 'p', 'b', 's', 'x', 'd', 'f', 'j', 'w']
with open('input.txt') as f:
    lines = f.readlines()
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
    for char in line:
        if char.lower() in massalhangzok:
            count[massalhangzok.index(char.lower())] += 1;
print(max(count))