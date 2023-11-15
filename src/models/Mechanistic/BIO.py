import numpy as np 

class IKM:
    def __init__(self,a=0.02,
                 b = 0.2,
                 c = -65,
                 d = 8):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.v = c 
        self.u = b*c 
        
    def update_var(self,I,dt=0.1):
        dv = (0.04 * self.v**2 + 5 * self.v + 140 - self.u + I) * dt
        du = (self.a * (self.b * self.v - self.u)) * dt 
        
        self.v += dv 
        self.u += du 

        if self.v >=30:
            self.v =self.c
            self.u += self.d 
    
    def simulate(self,I, dt= 0.1):
        v_val = []
        u_val = []

        for i in I:
            self.update_var(i,dt)
            v_val.append(self.v)
            u_val.append(self.u)
        
        return v_val, u_val
    

class FNM:
    def __init__(self, a=0.7, b=0.8, c=10, I=0):
        self.a = a
        self.b = b
        self.c = c
        self.I = I

        self.v = -1.0
        self.w = 0.0

    def update_variables(self, dt=0.01):
        dv = self.c * (self.v - (1/3) * self.v**3 - self.w + self.I) * dt
        dw = (1/self.c) * (self.v - self.a + self.b * self.w) * dt

        self.v += dv
        self.w += dw

    def simulate(self, time_steps=100, dt=0.01):
        num_steps = int(time_steps / dt)

        v_values = np.zeros(num_steps)
        w_values = np.zeros(num_steps)

        for i in range(num_steps):
            self.update_variables(dt)
            v_values[i] = self.v
            w_values[i] = self.w

        return v_values, w_values

    