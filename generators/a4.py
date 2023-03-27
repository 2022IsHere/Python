# File: a4.py
# Time: 23.3.2023 klo 13.10
# Author(s): Sebastian Sopola
# Description: Generate all possible permutations of lottery strikes with 7 different symbols and 2 special symbols. 
# Each lottery ticket has id-code number specifying which specific ticket is at hand

import itertools
import math

# permutation generator
def getperm(symbols, id):
    # infinite loop
    while True:
        # loop through all permutations
        for ticket in itertools.permutations(symbols):
            yield (id, ticket)
            # increment id number
            id += 1
        # return tuple of id, ticket
        return (id, ticket)


if __name__ == "__main__":
    
    marks = '§', '@', '#', '£', '¤', '&', '€' 
    array = list(marks) + [marks[0],  marks[0]] #  winning combination
    id = 10000 #  each generated ticket (array permutation) will add 1 to the id
    gen = getperm(array, id) #  use your generator function
    print(getperm(marks,id), type(getperm))
    print(gen, type(gen))
    printed = 0
    for i in range(math.factorial(len(array))): #  9!
        id, ticket = next(gen) #  generator return a tuple of id and ticket
        if id%1000 == 0: #  print every 1000th ticket
            print(f'{id}: {ticket}')
            printed += 1

    print(printed-1 , ' tickets printed')  #  the test will print 362 tickets out of 362880 generated.



















