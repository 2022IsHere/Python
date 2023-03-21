#File: A3.py
#Time: 8.3.2023 klo 16.21
# Author(s): Sebastian Sopola
# Description: Use decorator for function and keyword arguments to original function. Check argument types.


# decotarot function
def magazine_info(magazine):
    def inner(*args, **kwargs):
        if ( type(kwargs['year']) != int or type(kwargs['price']) != float or type(kwargs['name']) != str ):
            raise ValueError
        else:
            return magazine(*args, **kwargs)
    return inner


# decorated function
@magazine_info
def magazine(*,year: int, price: float, name: str='Donalt Duck')-> str:
    return f"The first {name} sold {year} in Finland with {price} (old) marks."


if __name__ == "__main__":
    try:
        print(magazine(year=1951, price=50.0, name='Aku Ankka'))
        print(magazine(year=1951, price= 50, name='Aku Ankka'))
    except Exception as error:
        print("There was an error", error)


    



















