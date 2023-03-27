# File: a3.py
# Time: 22.3.2023 klo 22.11
# Author(s): Sebastian Sopola
# Description: Modify a2 so that prime number generator gets parameter max with default None. 
# Let Generator loop through numbers up to integer argument given and give informative output whether integer argument is or isn't prime number.
# When no interger argument, generator loops infinetly



# prime number generator
def primegen(max = None) -> int:
    k = 7
    # loop till max value
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
            # check is max argument given and correct type
            if type(max) == int:
                # check is k greater or equal to interger argument
                if k >= max:
                    raise StopIteration(f'Loop reached the argument {max} and therefore was terminated')

if __name__ =="__main__":
     g = primegen(1000)
     for i in g:
        print(i)