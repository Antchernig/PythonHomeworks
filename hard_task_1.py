name = input("Enter your name and surname")
name.title()
age = int(input('Enter your age'))
weight = int(input('Enter your weight'))
if (age <= 30 and 50 <= weight <= 120 ):
    print('{0}, age {1}, weight {2}kg - normal state'.format(name, age, weight))
elif (age >= 30 and (weight <= 50 or weight >= 120)):
    print('{0}, age {1}, weight {2}kg - need a survey'.format(name, age, weight))
elif (age >= 40 and (weight <= 50 or weight >= 120)):
    print('{0}, age {1}, weight {2}kg - warning!!!'.format(name, age, weight))
else:
    print('{0}, age {1}, weight {2}kg - warning!!!'.format(name, age, weight))