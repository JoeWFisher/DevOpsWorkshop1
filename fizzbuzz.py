def fizz(number):
    if number % 3 == 0:
        return True

def buzz(number):
    if number % 5 == 0:
        return True

def bang(number):
    if number % 7 == 0:
        return True

for i in range(1, 101):
    if fizz(i) and buzz(i) == True:
        print('FizzBuzz')
    elif fizz(i) == True:
        print('Fizz')
    elif buzz(i) == True:
        print('Buzz')
    else:
       print(i)
    i + 1
