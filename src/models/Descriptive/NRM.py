import numpy as np

class LNP:
    def __init__(self, kernel, input_stimulus, nonlinearity, dt):
        self.kernel = kernel
        self.input_stimulus = input_stimulus
        self.nonlinearity = nonlinearity
        self.dt = dt

    def nonlinearity_(self, x):
        return max(0, x)

    def simulate(self):
        epochs = len(self.input_stimulus)
        firing_rates = []

        for t in range(epochs):
            
            start_index = max(0, t - len(self.kernel) + 1)
            end_index = t + 1

            if start_index < 0:
                
                padding = np.zeros(-start_index)
                kernel_slice = self.kernel
                input_slice = np.concatenate((padding, self.input_stimulus[:end_index]))
            else:
                kernel_slice = self.kernel[-(end_index - start_index):]
                input_slice = self.input_stimulus[start_index:end_index]

            conv = np.sum(kernel_slice * input_slice)
            rate = self.nonlinearity_(conv)
            spike_prob = 1 - np.exp(-rate * self.dt)
            spike = np.random.rand() < spike_prob
            firing_rates.append(rate if spike else 0)

        return firing_rates
    
class ReLUModel:
    def __init__(self, time_constant, dt):
        self.time_constant = time_constant
        self.dt = dt
        self.membrane_potential = 0  
        self.firing_rate = []  

    def update_membrane_potential(self, external_input):
        self.membrane_potential += (external_input - self.membrane_potential) * (self.dt / self.time_constant)

    def simulate(self, external_inputs):
        for input_value in external_inputs:
            self.update_membrane_potential(input_value)
            
            rate = max(0, self.membrane_potential)
            self.firing_rate.append(rate)
    
    def get_firing_rate(self):
        return self.firing_rate

