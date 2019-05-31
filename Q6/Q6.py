import sys
import sympy as sp
import math
#####################class ######################
class PGaussSolver:
    def __init__(self,pf,a, b, n):
        self.m_Pf = pf
        self.m_A=a
        self.m_B=b
        self.m_N=n
        print(" CGaussSolver object created ! ")



    def legendre(self ,m_N, x):
        return help(self.m_N ,x)


    def dLegendre(self ,m_N, x):
        dLegendr = (1.0 * self.m_N / (x * x - 1)) * ((x * self.legendre(self.m_N, x)) - self.legendre(self.m_N - 1, x))
        print(f" dLegendre is {dLegendr}")
        return dLegendr


    def legendreZeroes(self ,m_N, i):
        xnew1 =0
        xold1= 0
        pi = 3.141592655;
        xold1 = math.cos(pi * (i - 1 / 4.0) / (self.m_N + 1 / 2.0));
        iteration =  1
        while True:
            if (iteration != 1):
                xold1 = xnew1
                xnew1 = xold1 - self.legendre(self.m_N, xold1) / self.dLegendre(self.m_N, xold1)
                iteration += 1
            if (1 + abs((xnew1 - xold1)) > 1.):
                break
        print(" legendreZeroes !")
        return xnew1

    def weight(self ,m_N, x):
        weightI = 0
        weightI = 2 / ((1 - (x** 2)) * (self.dLegendre(self.m_N, x)** 2))
        print(f" weight !  {weightI}")
        return weightI


    def exec(self):
        integral = 0
        iteration = 1
        iteration += 1
        #print(" going to loop ")
        print(self.m_N)
        for i in range(int(self.m_N)):
            #print(f"i is {i}")
            integral = integral + self.m_Pf(self.legendreZeroes(self.m_N, i)) * self.weight(self.m_N,self.legendreZeroes(self.m_N, i))
            print(integral)

        self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral
        print(f" exec !{self.m_Result} , {integral}")


    def getResult(self):
        print(f" getresualt !   {self.m_Result}")
        return self.m_Result

###############3afunction################
def aFunction(x):
    xN = 0.5 * x + 0.5
    print("a function ")
    l =((xN** 3) / (xN + 1))*(math.cos(xN** 2))
    return l

def help(n,x):
    if (n == 0):
        return 1
    elif (n == 1):
        return x
    else:
        return ((2.0 * n - 1) / n) * x * help(n - 1, x) - ((1.0 * n - 1) / n) * help(n - 2, x)

############### main ########################
a = 0
b = 1
n = int(sys.argv[1])
aSolver = PGaussSolver(aFunction, a, b, n)
aSolver.exec()
print(f"Result of Python code (n = {n}    {aSolver.getResult()})")
