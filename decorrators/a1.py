# File: A1.py
# Time: 8.3.2023 klo 15.01
# Author(s): Sebastian Sopola
# Description: make decorator for foo function

def copyright(foo):
    print("copyright- Sebastian Sopola")
    def inner():            # Wrapper
        # foo()             # if foo doesnt return anything
        return foo()        # returns original argument function if original functio return something 
    return inner


@copyright                  # decorator function
def foo():                  # original function
    print("This is a decorated function")
if __name__ == "__main__":
    foo()










