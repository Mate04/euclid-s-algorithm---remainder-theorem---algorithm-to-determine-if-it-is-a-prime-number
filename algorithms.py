import math

def largestNumber1(num:int):
    while num < 1:
        num = int(input('Please, choose a number greater than 0: '))
    return num
def largestNumber2(num:int):
    while num <= 1:
        num = int(input('Please, choose a number greater than 1: '))
    return num
def checkAgreaterB(a:int,b:int):
    while a < b:
        b = int(input(f'Please, choose a number less than {a}: '))
    return a,b
def euclideanAlgorithm(a:int,b:int):
    a, b = checkAgreaterB(a,b)
    AuxA, AuxB = a,b
    mod = a%b
    while mod != 0:
        a = b
        b = mod
        mod = a%b
    print(f'mcd({AuxA},{AuxB}): {b}')
    print('Calculated with euclidean algorithm by Mateo MALDONADO')

def remainderTheorem(a:int,b:int):
    a, b = checkAgreaterB(a,b)
    AuxA, AuxB = a,b
    c = a//b
    r = a - (c*b)
    while r != 0:
        a = b
        b = r
        c = a//b
        r = a - (c*b)
    print(f'el MCD({AuxA},{AuxB}) es {b}')

def aPrimeNumber(num:int):
    k = int(math.sqrt(num))
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    while k != 1:
        if num % k == 0:
            return False
        k -= 1
    return True