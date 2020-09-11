def haveFun(amount):
    for i in range(amount):
        print(":)")

haveFun(100)

import operator
operation = {"+":operator.add,
             "-":operator.sub,
             "*":operator.mul,
             "/":operator.truediv,
             "%":operator.mod}
def calculate(sign, a, b):
    return operation[sign](a,b)

print(calculate("%",45,5))

import winsound

    winsound.Beep(600, 50)

    
