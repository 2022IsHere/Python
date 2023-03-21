# File: a5.py
# Time: 12.3.2023 klo XX.XX
# Author(s): Sebastian Sopola
# Description: Create decorator class to handle function argument types

class MagazineDecorator(object):
    def __init__(self, min_number, types):
        self.min_number = min_number
        self.types = types
     

    # en nyt ihan tajua miksi tuossa pitää olla (self, inner). Miksi se inner pitää olla tuossa?????
    # ja sitten se ku palautetaan niin se palauttaa 

    def __call__(self, magazine):
        def inner(*args, **kwargs):

            if ( len(kwargs) < self.min_number ):
                raise ValueError("Arguments must be at least 3")
                
            if ( type(kwargs['price']) != float ):
                raise ValueError(": argument 2: Not of type float")
            elif ( type(kwargs['year']) != int ):
                raise ValueError(": argument 1: Not of type int")
            elif ( type(kwargs['name']) != str ):
                raise ValueError(": argument 3: Not of type str")
            
            return magazine(*args, **kwargs)
        return inner


@MagazineDecorator(min_number=3, types=(int, float, str))
def magazine(*,year: int, price: float, name: str='Donald Duck', **kwargs) -> str:
    start = f"The first {name} sold {year} in Finland with {price} (old) marks."
    l = []
    for key, value in kwargs.items():
        l.append( f"{key}: {value}" )
    return f"{start}\n {''.join(l)}"

if __name__ == "__main__":
    try:
        print(magazine(year=1951, price=50.0, name='Aku Ankka'))
        print(magazine(year=1951, price=50.0, name='Aku Ankka'))
        print(magazine(year=1951, price=50, name='Aku Ankka'))
    
    except Exception as error:
        print("There was an error:", error)




