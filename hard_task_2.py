date = input('Enter the date in form xx.xx.xxxx: ')
date_list = date.split('.')
day = int(date_list[0])
month = int(date_list[1])
year = int(date_list[2])
if (day < 1 or day > 31):
    print('Wrong date')
else:
    if (month < 1 or month > 12):
        print('Wrong date!')
    else:
        if (year < 1 or year > 9999):
            print('Wrong date!')
        else:
            print('Right date')