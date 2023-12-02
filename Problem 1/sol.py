file = open('in.txt', 'r')
line = file.readline()
total = 0
num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
while(line):
    first_index = 10000
    last_index = -1
    first_number = 0
    last_number = 0
    
    sub = line[0]
    sub_index = 0
    
    while (sub_index != len(line)):
        for element in num_dict:
            index = sub.find(element)
            if index < first_index and index != -1:
                first_index = index
                first_number = num_dict[element]
                
            if index > last_index:
                last_index = index
                last_number = num_dict[element]  
        sub_index += 1
        sub = line[:sub_index]
            
    sum = first_number * 10 + last_number
    total += sum
    line = file.readline()

print(total)