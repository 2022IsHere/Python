# File: a5.py
# Time: 23.3.2023 klo 18.24
# Author(s): Sebastian Sopola
# Description: Generate tickets of given array. Check how many of generated tickets are winning kind and how many are not

import itertools
import random
import math



# permutation generator / ticket generator
def getperm(symbols, id):
    # infinite loop
    while True:
        # loop through all permutations
        for ticket in itertools.permutations(symbols,6):
            yield (id, ticket)
            # increment id number
            id += 1
        # return tuple of id, ticket
        return (id, ticket)
    



# check ticket / permutation, is it winning ticket or not
def checkTickets(symbols, tickets):

    # keep track how many times different symbols appear in a ticket
    counter = [ 0, 0, 0, 0, 0, 0, 0 ]

    # winning and looser tickets and total amount of both
    totalWinners = 0
    winnerTickets = []
    totalLoosers = 0
    looserTickets = []

    # calculator to keep track that we initialize variables after 9 items ( ticket size of items )
    calculator = 1

    state = None


    # loop for every ticket
    for ticket in tickets:
        
        # loop for every element in a single ticket to check values and find winning ticket(s)
        for item in ticket:
            # check which item it is and increment counter list at same position as element appears in symbols list
            if item == symbols[0]:
                counter[0] += 1

            elif item == symbols[1]:
                counter[1] += 1

            elif item == symbols[2]:
                counter[2] += 1

            elif item == symbols[3]:
                counter[3] += 1

            elif item == symbols[4]:
                counter[4] += 1

            elif item == symbols[5]:
                counter[5] += 1

            elif item == symbols[6]:
                counter[6] += 1

            elif item == symbols[7]:
                counter[random.randint(0,6)] += 1       # special symbol which can represent  any symbol

            elif item == symbols[8]:                    # special symbol which can represent  any symbol
                counter[random.randint(0,6)] += 1


            calculator += 1

            # reset checking after 9 items ( size of ticket ), itnitialize variables back to base case
            if calculator >= 10:

                # check if one of the symbols appear at least 3 times. Then winning tickets total number is incremented by 1
                for value in counter:
                    if value >= 3:
                        totalWinners += 1
                        winnerTickets.append(ticket)
                        state = True
                        break
                    else:
                        totalLoosers += 1
                        looserTickets.append(ticket)
                        state = False
                        break
                calculator = 1
                counter = [ 0, 0, 0, 0, 0, 0, 0 ]
                
    return (totalWinners, winnerTickets, totalLoosers, looserTickets)


if __name__ == "__main__":
    symbols = '§', '@', '#', '£', '¤', '&', '€' 
    array = list(symbols) + [symbols[0],  symbols[0]]     
    id = 10000                                      #  id number to be passed to specify each ticket with id
    gen = getperm(array, id)                        #  create generator object
    gnumber = 500                                 #  number to decide how many tickets will be generated
    
    # list to save generated tickets
    tickets = []
    # loop ticket generator and append every ticket to list
    calculator = 1
    for ticket in gen:
        if calculator >= gnumber:
            break
        else:
            tickets.append(ticket[1])
            calculator += 1

    # pass list of tickets to algoritm which checks how many winning tickets there are and how many tickets in total
    totalLoosers, looserTickets, totalWinners, winnerTickets = checkTickets(symbols, tickets)
    print(f'Out of {totalWinners+totalLoosers} tickets {len(winnerTickets)} were winning tickets! Hurraa! And with rest {totalLoosers} tickets you would not win a thing. {round((totalWinners/(totalWinners+totalLoosers)),4)*100} % success rate isnt that nice :)')




























