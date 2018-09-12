first_list = [1, 3, 3, 5, 6, 3, 8, 1]
second_list = []
i = 0
j = 0
k = 0
while i < len(first_list):
    while j < (len(first_list) - 1):
        if first_list[i] == first_list[j+1]:
            second_list.pop()
        else:
            if len(second_list) > 0:
                while k < len(second_list):
                    if first_list[i] != second_list[k]:
                        second_list.append(first_list[i])
                    k = k + 1
                k = 0
            else:
                second_list.append(first_list[i])
        j = j + 1
    i = i + 1
print(second_list)