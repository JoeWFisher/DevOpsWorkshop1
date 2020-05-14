def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mult(number1, number2):
   return number1 * number2

def div(number1, number2):
    return number1 / number2

with open("step_2.txt", 'r') as f:
    text_list = f.read().splitlines()
    for line in text_list:
        split = line.split()
        op = split[1]
        paraA = int(split[2])
        paraB = int(split[3])

        if op == '+':
            print(add(paraA, paraB))
        elif op == '-':
            print(sub(paraA, paraB))
        elif op == 'x':
            print(mult(paraA, paraB))
        elif op == '/':
            print(div(paraA, paraB))
        else:
            print('Please use "x", "+", "-", or "/"')





