#operator over loading
class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,o):
        return self.a +o.a,self.b+o.b

class Compare:
    def __init__(self,a):
        self.a = a
    def __eq__(self,o):
        if(self.a<o.a):
            return "First is less than Second"
        elif self.a>o.a:
            return "Second is less than First"
        else:
            return "Both are equal"

    
f = Complex(8,9)
s = Complex(10,11)
print(f+s)
fi = Compare(20)
se = Compare(24)
print(fi == se)
