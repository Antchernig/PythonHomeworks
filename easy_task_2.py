first_list = [1, 2, 2, 4, 7, 3, 5, 6]
second_list = [2, 8, 3, 9]
i = 0
j = 0
while i < len(first_list):
    while j < len(second_list):
        if first_list[i] == second_list[j]:
            first_list.pop(i)
            j = -1
        j = j + 1
    j = 0
    i = i + 1
print(first_list)