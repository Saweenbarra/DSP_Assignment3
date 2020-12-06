#2nd order, form II, IIR filter class
class IIR2Filter:
    def __init__(self,_b0,_b1,_b2,_a0,_a1,_a2):
        self.b0 = _b0
        self.b1 = _b1
        self.b2 = _b2
        self.a0 = _a0
        self.a1 = _a1
        self.a2 = _a2
        self.buffer1 = 0
        self.buffer2 = 0
    
    def filter(self,v):
        inp=0.0
        out=0.0
        inp=v
        out=(self.b1*self.buffer1)
        inp=inp-(self.a1*self.buffer1)
        out=out+(self.b2*self.buffer2)
        inp=inp-(self.a2*self.buffer2)
        out=out+inp*self.b0
        self.buffer2=self.buffer1
        self.buffer1=inp
        return out

#Chain of 2nd order, form II, IIR filter objects
class IIRFilter:
    def __init__(self, sos):
        self.IIR2filters = []
        for row in sos:
            self.IIR2filters.append(IIR2Filter(row[0],row[1],row[2],row[3],row[4],row[5]))
    
    def filter(self,v):
        intermediateOutput = v
        for f in self.IIR2filters:
            intermediateOutput = f.filter(intermediateOutput)
        return intermediateOutput


