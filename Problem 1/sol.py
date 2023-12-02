file = open('in.txt', 'r')
line = file.readline()
num = ['1', '2']
total = 0
while(line):
    index = 0
    for character in line:
        if 48 <= ord(character) <= 57:
            num[index] = character
            index = 1
    total += int(f'{num[0]}{num[1]}')
    line = file.readline()
    
print(total)

