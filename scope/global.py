x  = 5

def get_global(num: int):
    global x
    print(x)
    x = num
    print(x)

get_global(7)