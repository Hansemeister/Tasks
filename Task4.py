#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def printDivisors(input : int) : #input forced to be integer
    returnlist = []
    for i in range(2, input+1):
        if input % i == 0: returnlist.append(i)
    print(returnlist)
    return returnlist
printDivisors(int(input("Select a number: ")))
