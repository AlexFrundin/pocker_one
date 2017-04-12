

class Square():
    def __init__(self,w,h):
        self.W=w
        self.H=h

    def whatsup(self):
        if self.H==self.W:
            return("Square")
        else:
            return ("Rectangle")



a=Square(30,40)
b=Square(20, 20)

print(b.whatsup())
