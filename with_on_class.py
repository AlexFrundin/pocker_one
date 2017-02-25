class A:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, *args,**kwargs):
        print("Exit")
with A():
    pass

with A() as a:
    a.x=1
    print(a.x)
