f = open("output.txt", 'r')
lines = f.readlines()
i = 0
for line in lines:
    i = i +1
    if i == 46:
        print(line)

    elif i == 47:
        print(line)

    elif i == 48:
        print(line)
    
    f.close()