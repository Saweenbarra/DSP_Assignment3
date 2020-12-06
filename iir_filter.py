#2nd order, form II, IIR filter class
class IIR2Filter:
    def __init__(self,_firCoeff,_iirCoeff):
        self.firCoeff = _firCoeff
        self.iirCoeff = _iirCoeff
        self.buffer1 = 0
        self.buffer2 = 0
    
    def filter(self,v):
        inp=0.0
        out=0.0
        inp=v

        #The IIR Feedback (Buffered feedback multiplied with IIR coefficients) is summed with the input
        inp=inp-(self.iirCoeff[1]*self.buffer1)
        inp=inp-(self.iirCoeff[2]*self.buffer2)

        out=(self.firCoeff[1]*self.buffer1)
        out=out+(self.firCoeff[2]*self.buffer2)
        out=out+inp*self.firCoeff[0]

        self.buffer2=self.buffer1
        self.buffer1=inp
        return out

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


