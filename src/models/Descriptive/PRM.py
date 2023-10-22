import numpy as np 

class FRM:
    def __init__(self,firing_rate,stimulus_intensity, response_gain):
        self.firing_rate = firing_rate
        self.stimulus_intensity = stimulus_intensity
        self.response_gain = response_gain
    
    def simulate(self,time,dt):
        firing_rates = []
        for _ in range(time):
            rate = self.firing_rate + self.response_gain * self.stimulus_intensity

            rate = max(0,rate)

            spike_prob = 1- np.exp(-rate * dt)
            spike = np.random.rand() < spike_prob
            firing_rates.append(rate if spike else 0)
        return firing_rates
    
class GPM:
    def __init__(self):
        self.mean = 0.0
        self.std = 1.0
    
    def fit(self,x):
        self.mean = np.mean(x)
        self.std = np.std(x)
    
    def simulate(self,time, dt):
        population_act = np.zeros(time)
        time = np.arange(0,time * dt ,dt)
        for t in range(len(time)):
            population_act[t] = np.exp(-(time[t] - self.mean)**2/(2*self.std**2))

        return population_act