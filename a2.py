# FIle: A2.py
# Time: 8.3.2023 klo 15.23
# Author(s): Sebastian Sopola
# Description: decorated function takes parameters

# decorator function
def copyright(foo):
    def inner(a,b):             # parameters of decorated function are given to wrapper 
        return foo(a,b)
    return inner



# decorated function
@copyright
def foo(a,b,c='Donald Duck'):
    print("copyright - Sebastian Sopola")
    return (a,b,c)

if __name__ == "__main__":
    x = foo('Aku Ankka', 'Kalle Ankka')
    print(*x)























