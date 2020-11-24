#2nd order, form II, IIR filter class
class IIR2Filter:
    def __init__(self,_num,_den):
        self.numerator = _num
        self.denominator = _den
        self.buffer1 = 0
        self.buffer2 = 0
    
    def filter(self,v):
        inp=0.0
        output=0.0
        inp=v
        output=(self.numerator[1]*self.buffer1)
        inp=inp-(self.denominator[1]*self.buffer1)
        output=output+(self.numerator[2]*self.buffer2)
        inp=inp-(self.denominator[2]*self.buffer2)
        output=output+inp*self.numerator[0]
        self.buffer2=self.buffer1
        self.buffer1=inp
        return output

#Chain of 2nd order, form II, IIR filter objects
class IIRFilter:
    def __init__(self, sos):
        self.IIR2filters = []
        for row in sos:
            self.IIR2filters.append(IIR2Filter(row[:3],row[3:]))
    
    def filter(self,v):
        intermediateOutput = v
        for f in self.IIR2filters:
            intermediateOutput = f.filter(intermediateOutput)
        return intermediateOutput


