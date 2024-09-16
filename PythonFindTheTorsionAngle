

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        vector = [d1 - d2 for d1,d2 in zip([self.x,self.y,self.z],[no.x,no.y,no.z])]
        return Points(*vector)

    def dot(self, no):
        sprod = sum([sp1*sp2 for sp1,sp2 in zip([self.x,self.y,self.z],[no.x,no.y,no.z])])
        return(sprod)

    def cross(self, no):
        vprod = [(self.y*no.z)-(self.z*no.y),(self.z*no.x)-(self.x*no.z),(self.x*no.y)-(self.y*no.x)]
        return Points(*vprod)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

