class Gains:
    p = 0
    i = 0
    d = 0
    f = 0
    ff = 0

    def __init__(self, p, i, d, f, ff):
        self.p = p
        self.i = i
        self.d = d
        self.f = f
        self.ff = ff

    def getP(self):
        return self.p

    def getI(self):
        return self.i

    def getD(self):
        return self.d

    def getF(self):
        return self.f

    def getFF(self):
        return self.ff
