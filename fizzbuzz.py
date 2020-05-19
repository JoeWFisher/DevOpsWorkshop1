def fizz(number):
    if number % 3 == 0:
        return True

def buzz(number):
    if number % 5 == 0:
        return True

def bang(number):
    if number % 7 == 0:
        return True

i = [1,'']

for i[0] in range(1, 101):
    if fizz(i[0]) and buzz(i[0]) == True:
        i[1] = 'FizzBuzz'
    elif fizz(i[0]) == True:
        i[1] = 'Fizz'
    elif buzz(i[0]) == True:
        i[1] = 'Buzz'
    else:
       i[1] = str(i[0])
    print(i[1])
    i[0] + 1
