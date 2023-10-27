import numpy as np

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
    