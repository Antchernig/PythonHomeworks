import math

origin_list = [2, -3, 1, 9, -27, 4, 0]
new_list = []
i = 0
while i < len(origin_list):
    if origin_list[i] >= 0:
        if math.sqrt(origin_list[i]) % 1 == 0:
            new_list.append(math.sqrt(origin_list[i]))
    i = i + 1
print(new_list)