import numpy as np
from decimal import Decimal, getcontext
class WCM():
    def __init__(self,a=1.,
                 b=2.,
                 t_e=1.,
                 t_i=2.,
                 dt =0.01):
        self.a = a
        self.b = b
        self.t_e = t_e
        self.t_i = t_i
        self.dt = dt
        self.re = []
        self.ri = []
        self.time = []
    
    def initialize(self,r_e,r_i):
        self.r_e = r_e
        self.r_i = r_i 

    def simulate(self,T = 10.0):
        n_steps = int(T/self.dt)
        for t in range(n_steps):
            dr_e = (-self.r_e + self.a * (1 - self.r_e - self.b * self.r_i)) / self.t_e
            dr_i = (-self.r_i + self.a * (1 - self.r_i - self.b * self.r_e)) / self.t_i
            self.r_e += dr_e * self.dt 
            self.r_i += dr_i * self.dt

            self.re.append(self.r_e) 
            self.ri.append(self.r_i)
            self.time.append(t*self.dt)
        
        return self.re,self.ri,self.time
    
class Amari:
    def __init__(self, a=Decimal('0.1'), b=Decimal('0.2'), c=Decimal('-65.0')):
        self.a = a
        self.b = b
        self.c = c
        self.dt = Decimal('0.001')
        self.V_ = []
        self.W_ = []
    
    def initialize(self, V=Decimal('-10.0'), W=Decimal('-14.0')):
        self.V = V
        self.W = W

    def step(self, Int):
        dv = (-self.V + self.V**3/Decimal('3.0') - self.W + Int) * self.dt
        dw = (self.a * (self.b * (self.V - self.c) - self.W)) * self.dt
        self.V += dv
        self.W += dw

    def simulate(self, Int, T=Decimal('10.0')):
        getcontext().prec = 1000 
        getcontext().Emax = 999999  
        steps = int(T / self.dt)

        for _ in range(steps):
            self.step(Int)
            self.V_.append(self.V)
            self.W_.append(self.W)

        return self.V_, self.W_


     



