file = open('in.txt', 'r')
line = file.readline()
color_list = ['green', 'blue', 'red']

total = 0
total_power = 0

while(line):
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    max_color_dict = {'green':0, 'red':0, 'blue':0}
    line = line.split(":")  
    game_num = int(line[0].replace("Game", ''))
    line = line[1].split(";")
    
    for game in line:
        color_count = game.split(',')
        for item in color_count:
            for color in color_list:
                if color in item:  
                    item = item.replace(f'{color}', '')
                    max_color_dict[color] = max(max_color_dict[color], int(item))
            
    if max_color_dict['red'] <= 12 and max_color_dict['green'] <= 13 and max_color_dict['blue'] <= 14:
        total += game_num
    sum = max_color_dict['green']*max_color_dict['red']*max_color_dict['blue']
    print(sum)
    total_power += sum
    line = file.readline()
print(total, total_power)


