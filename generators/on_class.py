""" On class examples """
""" yeild frees memory when we go out of the function and then continue actions if there is some left"""


"""
# how to use yield
def foo(data):
    data *= 10 # 1. this is done
    yield data # 2. then return data as it is
    data /= 10 # 3. calc this with data as before it was yielded( returned )
    return data # 4. then return data as it is after division
    # every yield return variable as it is in that point then it continues with actions 
# iterate over generator to get multiple values
for _ in range(10):
    for y in foo(7):
        print(y)
print(y, 'final')
"""

"""
# how to create generator function
def fibonacci():
    numbers = []
    while True:
        if not numbers:
            numbers.append(0)
            yield numbers[-1]
        elif len(numbers) == 1:
            numbers.append(1)
            yield numbers[-1]
        else:
            #print(numbers)
            numbers.append(sum(numbers))
            numbers.pop(0)
            yield numbers[-1]
print(fibonacci, type(fibonacci))
gen = fibonacci()
print(gen, type(gen))

# how to use next
for i in fibonacci():
    print(i)
    if i >= 1000:
        print(next(gen), 'calling next1')
        print(next(gen), 'calling next2')
        print(next(gen), 'calling next3')
        print(next(gen), 'calling next4')
        break

    # can you show again next and how to use it?????
"""

"""
# recursive fibonacci sequence
def fibonacci(num1, num2, max):
    if num1 >= max: # base case where recursion stops and starts to move back up
        return num1 # return base number
    yield num1      # return every value from bottom to top
    yield from fibonacci(num2, num1+ num2, max) # recursive of fibonacci function
"""
"""
for i in fibonacci(0,1,400):
    print(i)
"""
"""

def readfibo(f):
    yield from f

wrap = readfibo(fibonacci(0,1,200))
print(wrap, type(wrap))
for i in wrap:
    print(i)
"""
"""
# how to use send
def fibonacci():
    numbers = []
    while True:
        if not numbers:
            numbers.append(0)
        elif len(numbers) == 1:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        res = yield numbers[-1]
        if res:
            numbers.append(res)
            numbers.pop(0)
            yield numbers[-1]
gen = fibonacci()
for i in gen:
    print(i)
    if i >= 100:
        print(next(gen))
        num = 150
        print(f'sending 150 to sequence')
        gen.send(num)
        print(next(gen))
        print(next(gen))
        print(next(gen))
        break
        
"""
# 1: infinite loop
# 2: raise iterationerror when max value reached
# 3: 
# 4: factorial of different options of winning combinations
# 5: some modification to Ex4






