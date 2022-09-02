import csv

with open('/home/user/users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            f'{", ".join(row)}'
            line_count += 1
        else:
            line_count += 1
    print('В базе', line_count - 1, 'пользователей.')               # 1. Количество пользователей в базе


