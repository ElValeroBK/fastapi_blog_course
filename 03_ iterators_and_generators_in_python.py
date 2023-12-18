
lista = [1,2,3,7,8,9]

num_iter = lista.__iter__()

print(num_iter.__next__())
print(num_iter.__next__())

while True :
    try:
        print(num_iter.__next__())

    except StopIteration :
        break

########



class Infinite_Iter_Number():
    def __init__(self) -> None:
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        self.num += 1
        return num
    

value = iter(Infinite_Iter_Number())

print (next(value))
print (next(value))

#######


def return_value():
    yield 1
    yield 2
    yield "three"

value=return_value()

print(value.__next__())
print(value.__next__())
print(value.__next__())

########   

def even_numbers(range_number):

    for even in range(1,range_number):
        if even % 2 == 0:
            yield even


def even_number_generator(amount):
    even = even_numbers(amount)
    while True :
     try:
        print(even.__next__())
     except StopIteration :
        break

even_number_generator(20)
 
######

def even_numbers():
    num = 0
    while (num<20):
        yield num
        num += 2
        
evel = even_numbers()
print(evel.__next__())
