f = open("output.txt", 'r')
lines = f.readlines()
i = 0
for line in lines:
    i = i +1
    if i == 50:
        print(line)

    elif i == 51:
        print(line)

    elif i == 52:
        print(line)
    
    f.close()