# File: a1.py
# Time: 22.3.2023 klo 20.54
# Author(s): Sebastian Sopola
# Description: Generate numbers 1 up infinetly and return all prime numbers. Allow user to ask if specific number is prime or not

import time

# prime number generator
def primegen():
    k  = 7
    # infinite loop
    while True:
            prime = True
            # check numbers from 2 to k-1
            for number in range(2, k):
                # if there is one number that devides k with remainder 0
                if k % number == 0:
                    # k is not prime and prime 'status' is set to false and no other numbers is needed to check with k
                    # we jump to check next number
                    prime = False
                    break
            # if no error arose during devisions, number is yield because it is prime number
            if prime:
                yield k
            k += 1
            time.sleep(0.25)        


if __name__ == "__main__":
     # create generator object
     g = primegen()
while True:
    # use next method to get next item from prime number generator 
    p = next(g)
    # loop to 1000
    if p >= 1000:
        break
    # print each new prime number
    print(p)












