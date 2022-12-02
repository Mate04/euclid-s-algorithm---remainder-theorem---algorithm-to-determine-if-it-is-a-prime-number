from algorithms import *    
def main():
    Option = -1
    while Option != 0:
        if Option == 1:
            euclideanAlgorithm(largestNumber1(int(input('First element: '))),largestNumber1(int(input('Seconds element: '))))
        elif Option == 2:
            remainderTheorem(largestNumber1(int(input('First element: '))),largestNumber1(int(input('Seconds element: '))))
        Option = int(input('Option 1: MCD between two numbers\nOption 2: MCD applying remainder theorem\nOption 0: Out\nOption: '))
main()
