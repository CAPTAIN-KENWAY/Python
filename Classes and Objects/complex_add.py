class Complex:
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    def add(self,x):
        real= self.real + x.real
        imaginary= self.imaginary + x.imaginary
        return real,imaginary

n1=Complex(1,5)
n2=Complex(-2,8)
print(n2.add(n1))


