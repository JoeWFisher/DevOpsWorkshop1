def fizz(number):
    if number % 3 == 0:
        return True

def buzz(number):
    if number % 5 == 0:
        return True

def bang(number):
    if number % 7 == 0:
        return True

def bong(number):
    if number % 11 == 0:
        return True

def fuzz(number):
    if number % 13 == 0:
        return True    

i = [1,'']

end = int(input('Please input number to FizzBuzz up to: '))

for i[0] in range(1, end + 1):

    i[1] = str(i[0])
    
    if bong(i[0]):
        i[1] = 'Bong'
    elif fizz(i[0]) and buzz(i[0]):
        i[1] = 'FizzBuzz'
    elif fizz(i[0]):
        i[1] = 'Fizz'
    elif buzz(i[0]):
        i[1] = 'Buzz'

    if bang(i[0]):
        if i[1] in ['FizzBuzz', 'Fizz', 'Buzz']:
            i[1] = i[1] + 'Bang'
        elif i[1] == 'Bong':
            i[1] = 'Bong'
        else:
            i[1] = 'Bang'

    if fuzz(i[0]):
        if i[1] in ['FizzBuzz', 'Fizz', 'Buzz', 'Bong']:
            i[1] = 'Fuzz' + i[1]
        else:
            i[1] = 'Fuzz'

    print(i[1])
    i[0] + 1
