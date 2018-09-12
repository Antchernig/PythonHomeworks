date = input('Enter the date in form 00.00.0000')
date_list = date.split('.')
text_date = []
day_dictionary = {'01': 'Первое', "02": "Второе", "03": "Третье", "04": "Четвертое", "05": "Пятое", "06": "Шестое",
                  "07": "Седьмое", "08": "Восьмое", "09": "Девятое", "10": "Десятое", "11": "Одинадцатое"}
days = day_dictionary.keys()
month_dictionary = {"01": "Января", "02": "Февраля", "03": "Марта", "04": "Апреля", "05": "Мая", "06": "Июня",
                    "07": "Июля", "08": "Августа", "09": "Сентября", "10": "Октября", "11": "Ноября", "12": "Декабря"}
for key in day_dictionary.keys():
    if date_list[0] == key:
        text_date.append(day_dictionary[key])
for key in month_dictionary.keys():
    if date_list[1] == key:
        text_date.append(month_dictionary[key])
text_date.append(date_list[2])
print('{0} {1} {2} года'.format(text_date[0], text_date[1], text_date[2]))