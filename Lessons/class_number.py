import numbers
class Number:
    def __init__(self,value):
        self.value=value

    def __repr__(self):
        return "Number {}".format(self.value)

    def __add__(self,other):
        #для сложение с другими числами
        if isinstance(other,numbers.Number):
            return Number(self.value+other)
        return Number(self.value+other.value)
#сложение в обратную сторону т.е ччисло идет первым
    def __radd__(self,other):
        return self.__add__(other)

    def __iadd__(self,other):
        return self.__add__(other)

    
