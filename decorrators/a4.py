# File: a4.py
# Time: 12.3.2023 klo 19.00
# Author(s): Sebastian Sopola
# Description: check whether arguments' types are correct and there's at least 3 arguments



def magazine_info(min_number,types):
    def wrapper(magazine):
          def inner(*args,**kwargs):
                if len(kwargs) < min_number:
                    raise ValueError
                
                # if price is not float, we place that value with string 'faulty value'
                if ( type(kwargs['price']) != float ):
                    raise ValueError(": argument 2 : Not of type float")
                elif ( type(kwargs['year']) != int ):
                    raise ValueError(": argument 1 : Not of type int")
                elif ( type(kwargs['name']) != str ):
                     raise ValueError(": argument 3 : Not of type str")

                return magazine(*args, **kwargs)  
          return inner 
    return wrapper

@magazine_info(min_number=3, types=(int, float,str))
def magazine(*,year: int, price: float, name: str='Donald Duck', **kwargs)-> str:
    start = f"The first {name} solf {year} in Finland with  {price} (old) marks."
    l = []
    for key, value in kwargs.items():
        l.append(f"{key}: {value}")
    return f"{start}\n {''.join(l)}"

if __name__ == "__main__":
    try:
        print(magazine(year=1951, price=50.0, name='Aku Ankka'))
        print(magazine(year=1951, price=50.0, name='Aku Ankka', circulation=34017))
        print(magazine(year=1951, price=50, name='Aku Ankka', circulation=34017))
    except Exception as error:
        print("There was an error", error)

























