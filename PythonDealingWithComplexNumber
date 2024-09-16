

class Complex(object):
    def __init__(self, real, imaginary):
         self.real = real
         self.imaginary = imaginary
         #print("self.real:",self.real)
         #print("self.imaginary:",self.imaginary)
    def __add__(self, no):
         #print("no:%s",no)
         #print("no.real:",no.real)
         #print("no.imaginary",no.imaginary)
         return Complex(self.real+no.real,self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real - no.real,self.imaginary - no.imaginary)
    def __mul__(self, no):
         mreal = self.real * no.real - self.imaginary * no.imaginary
         mimag = self.real * no.imaginary + self.imaginary * no.real
         return Complex(mreal,mimag)
    def __truediv__(self, no):
         dreal = ((self.real*no.real)+(self.imaginary * no.imaginary)) / (pow(no.real,2)+pow(no.imaginary,2))
         dimag = ((self.imaginary * no.real) - (self.real * no.imaginary)) / (pow(no.real,2)+pow(no.imaginary,2))
         return Complex(dreal,dimag)
    def mod(self):
         mdreal =  math.sqrt(self.real**2 + self.imaginary**2)
         mdimag = 0.00
         return Complex(mdreal,mdimag)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

