a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_ten(array):
    for i in array:
        if i < 10:
            print(i)
less_than_ten(a)

def construct_less_than_ten(array):
    newArray = []
    for i in array:
        if i < 10:
            newArray.append(i)
    print(newArray)
construct_less_than_ten(a)

def construct_less_than_custom(array, limit):
    newArray = []
    for i in array:
        if i < limit:
            newArray.append(i)
    print(newArray)
construct_less_than_custom(a, int( input("Gimme a number baby")))
