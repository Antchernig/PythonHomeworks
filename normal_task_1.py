number = int(input('Enter a number'))
while (number <= 0 or number >= 10):
    print('Please ener number in range from 0 to 10')
    number = int(input("Try again:"))
print('we get:', number*number)
