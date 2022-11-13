class Farhad:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def sow(self):
        a1=pow(self.a,self.b)
        b1=pow(self.c,self.d)
        print(a1+b1)
farhad=Farhad(a=int(input()),b=int(input()),c=int(input()),d=int(input()))
farhad.sow()