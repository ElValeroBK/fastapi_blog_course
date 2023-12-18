from typing import Callable

def smart_divide(func:Callable[[int,int],float]) -> float: 
    def inner(a,b):
        if b == 0:
            print("woops! division by o")
            return None
        return func(a,b)
    return inner




@smart_divide
def divide(a,b):
    print(a/b)


divide(9,8)