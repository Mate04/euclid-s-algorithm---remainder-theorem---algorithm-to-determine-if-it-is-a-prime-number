from algorithms import *    
def main():
    Option = -1
    while Option != 0:
        if Option == 1:
            euclideanAlgorithm(largestNumber1(int(input('First element: '))),largestNumber1(int(input('Seconds element: '))))
        elif Option == 2:
            remainderTheorem(largestNumber1(int(input('First element: '))),largestNumber1(int(input('Seconds element: '))))
        elif Option == 3:
            number =  largestNumber2(int(input('what number do you want to check if it is prime? ')))
            if not aPrimeNumber(number):
                print(f"The number {number} isn't prime")
            else:
                print(f"The number {number} is prime")
        Option = int(input('Option 1: MCD between two numbers\nOption 2: MCD applying remainder theorem\nOption 3: check if it is a prime number\nOption 0: Out\nOption: '))
main()
