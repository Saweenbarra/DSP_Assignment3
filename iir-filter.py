class IIR2Filter:
    def __init__(self,_num,_den):
        self.numerator = _num
        self.denominator = _den
        self.buffer1 = 0
        self.buffer2 = 0
    
    def filter(self,v):
        input=0.0
        output=0.0
        input=v
        output=(self.numerator[1]*self.buffer1)
        input=input-(self.denominator[1]*self.buffer1)
        output=output+(self.numerator[2]*self.buffer2)
        input=input-(self.denominator[2]*self.buffer2)
        output=output+input*self.numerator[0]
        self.buffer2=self.buffer1
        self.buffer1=input
        return output