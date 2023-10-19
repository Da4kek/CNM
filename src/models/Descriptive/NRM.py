import numpy as np 

class LNP():
    def __init__(self, kernel,input_stimulus,nonlinearity,dt):
        self.kernel = kernel 
        self.input_stimulus = input_stimulus
        self.nonlinearity = nonlinearity
        self.dt = dt 

    def nonlinearity(self,x):
        return max(0,x)
    
    def simulate(self):
        epochs = len(self.input_stimulus)
        firing_rates = []

        for t in range(epochs):
            
            conv = np.sum(self.kernel * self.input_stimulus[max(0,t-len(self.kernel) + 1 ):t + 1])

            rate = self.nonlinearity(conv)

            spike_prob = 1 - np.exp(-rate * self.dt)

            spike = np.random.rand() < spike_prob

            firing_rates.append(rate if spike else 0)
        return firing_rates
    