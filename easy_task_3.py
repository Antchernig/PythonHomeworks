number_list = [1, 3, 3, 6, 8, 5, 3]
new_list = []
i = 0
while i < len(number_list):
    if number_list[i] % 2 == 0:
        new_list.append(number_list[i] / 4)
    else:
        new_list.append(number_list[i] * 2)
    i = i + 1
print(new_list)