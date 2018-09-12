import random

n = int(input('Enter the length of random list'))
random_list = []
i = 0
while i < n:
    random_list.append(random.randint(-100, 100))
    i = i + 1
print(random_list)