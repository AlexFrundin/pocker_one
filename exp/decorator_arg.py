def decorator(x,y):
    def decor1(f):
        def wrapper():
            return (x+y)
        return wrapper
    return decor1
