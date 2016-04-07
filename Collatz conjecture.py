'''
Given any natural number, you will always arrive at 1 if you:
* Divide by two for any even number  OR
* Multiply by three and add 1 if the number is odd
'''

def collatz(n):
    while n != 1:
        if n%2==0:
            n = n/2
            print n
        else:
            n = n*3+1
            print n
    return n
