import numpy as np 


class STDP:
    def __init__(self, lr=0.01, t_po=20, t_neg=20, A_pos=0.05, A_neg=0.005):
        self.lr = lr
        self.t_po = t_po
        self.t_neg = t_neg
        self.A_pos = A_pos
        self.A_neg = A_neg

        self.weights = 0.1
        self.last_pre_time = 0
        self.last_post_time = 0

    def update_weights(self, pre, post):
        delta_t = post - pre
        weight_change = np.where(delta_t > 0, self.A_pos * np.exp(-delta_t /
                                 self.t_po), -self.A_neg * np.exp(delta_t / self.t_neg))

        self.weights += self.lr * weight_change.sum()

    def simulate(self, spike_time):
        spike_time = np.array(spike_time)
        pre_spike = spike_time[:len(spike_time) // 2]
        post_spike = spike_time[len(spike_time) // 2:]

        self.update_weights(pre_spike, self.last_post_time)

        if pre_spike.size > 0:
            self.last_pre_time = pre_spike[-1]

        self.update_weights(self.last_pre_time, post_spike)

        if post_spike.size > 0:
            self.last_post_time = post_spike[-1]

        return self.weights

class TMM:
    def __init__(self,U=.5,
                 t_f=200,
                 t_d=1500,
                 S=1):
        self.U = U
        self.t_f = t_f
        self.t_d = t_d
        self.S = S
        self.u = U 
        self.x = 1 
        self.last_spike = - np.inf
    
    def update_var(self,spike_time):
        del_t = spike_time - self.last_spike
        self.u += (self.U - self.u) / self.t_f - self.u * self.x * np.exp(-del_t/self.t_d)
        self.x += (1 - self.x) / self.t_d - self.u * self.x * np.exp(-del_t/self.t_f)

        self.last_spike = spike_time
    
    def simulate(self,spike_times):
        u_val = []
        x_val = []

        for spike in spike_times:
            self.update_var(spike)
            u_val.append(self.u)
            x_val.append(self.x)
        return u_val,x_val 
    