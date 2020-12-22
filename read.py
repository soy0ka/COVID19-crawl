with open("output.txt") as f:
    lines = f.readlines()

i = 0
for line in lines:
    i += 1
    if 49 < i and i< 53:
        print(line)
    
