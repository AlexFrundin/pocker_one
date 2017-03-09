class Furniture:
    def __init__(self,**kwargs):
        pass

class FurnitureWithBox:
    def __init__(self, **kwargs):
        self.state=kwargs['state']
        super().__init__(**kwargs)

class Table(Furniture):
    def __init__(self,**kwargs):
        self.h=kwargs['h']
        super().__init__(**kwargs)

class Shelf:
    def __init__(self,**kwargs):
        self.color=kwargs('color')

class TableWithBox(Table, FurnitureWithBox):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

f=TableWithBox(h=123,state=True)
