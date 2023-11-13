import numpy as np 

class LIF():
    def __init__(self, tm=10.0, R=10.0, V_rest=-70.0, V_threshold=-50.0):
        self.tm = tm
        self.R = R
        self.V_rest = V_rest
        self.V_threshold = V_threshold
        self.dt = 0.1 

    def simulate(self,I):
        time = np.arange(0,len(I) * self.dt, self.dt)
        mem_pot = np.zeros_like(time)
        spikes = []

        for i in range(1,len(time)):
            dV = (-(mem_pot[i-1] - self.V_rest) + self.R * I[i-1]) / self.tm * self.dt 
            mem_pot[i] = mem_pot[i-1] + dV
            if mem_pot[i] >= self.V_threshold:
                mem_pot[i] = self.V_rest
                spikes.append(i)
        return time, mem_pot, spikes
    
class AdEx():
    def __init__(self,C,gL,V_rest,DT,V_threshold, a, tw):
        self.C = C 
        self.gL = gL
        self.V_rest = V_rest
        self.DT = DT
        self.V_threshold = V_threshold
        self.a = a
        self.tw = tw
        self.dt = 0.1 

    def simulate(self,I):
        time = np.arange(0,len(I) * self.dt, self.dt)
        mem_pot = np.zeros_like(time)
        adaptive_curr = np.zeros_like(time) 
        spikes = []

        for i in range(1,len(time)):
            dV = (-(mem_pot[i-1] - self.V_rest) + self.gL*np.exp((mem_pot[i-1] - self.V_threshold)/self.DT)
                  + I[i-1] - adaptive_curr[i-1]) / self.C * self.dt
            mem_pot[i] = mem_pot[i-1] + dV

            dW = (self.a * (mem_pot[i-1] - self.V_rest) - adaptive_curr[i-1]) / self.tw * self.dt
            adaptive_curr[i] = adaptive_curr[i-1] + dW

            if mem_pot[i] >= self.V_threshold:
                mem_pot[i] = self.V_rest
                adaptive_curr[i] += 10
                spikes.append(i)
        return time, mem_pot, spikes
    