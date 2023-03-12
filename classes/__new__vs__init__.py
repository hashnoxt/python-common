
class A:

    def __new__(cls, *args, **kwargs): # spposed to return something
        print('new', cls, args, kwargs)
        return super().__new__(cls)
    
    def __init__(self, *args, **kwargs): #initialize values. doesn't return anything
        print('init', self, args, kwargs)

def how_object_construction_works():

    x = A(1,2,3,x=4)

    x = A.__new__(A, *args, **kwargs)  

    if isinstance(x, A):
        type(x).__init__(x, *args, **kwargs)

def main():
    how_object_construction_works()

main()