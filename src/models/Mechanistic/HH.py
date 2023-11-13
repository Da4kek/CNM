import numpy as np 
from scipy.integrate import odeint

class OHH:
    def __init__(self,duration,dt,inject_current):
        self.duration = duration 
        self.dt = dt 
        self.inject_current = inject_current

    def alpha_n(self, V):
        return 0.01 * (V + 55) / (1 - np.exp(-0.1 * (V + 55)))

    def beta_n(self, V):
        return 0.125 * np.exp(-0.0125 * (V + 65))

    def alpha_m(self, V):
        return 0.1 * (V + 40) / (1 - np.exp(-0.1 * (V + 40)))

    def beta_m(self, V):
        return 4.0 * np.exp(-0.0556 * (V + 65))

    def alpha_h(self, V):
        return 0.07 * np.exp(-0.05 * (V + 65))

    def beta_h(self, V):
        return 1.0 / (1 + np.exp(-0.1 * (V + 35)))

    def hh_model(self, y, t):
        V, n, m, h = y        
        INa = self.g_Na * (m**3) * h * (V - self.V_Na)
        IK = self.g_K * (n**4) * (V - self.V_K)
        IL = self.g_L * (V - self.V_L)
        I_inj = self.inject_current(t)
        
        dVdt = (I_inj - INa - IK - IL) / self.Cm
        dndt = self.alpha_n(V) * (1 - n) - self.beta_n(V) * n
        dmdt = self.alpha_m(V) * (1 - m) - self.beta_m(V) * m
        dhdt = self.alpha_h(V) * (1 - h) - self.beta_h(V) * h

        return [dVdt, dndt, dmdt, dhdt]

    def simulate(self, g_Na=120, g_K=36, g_L=0.3, V_Na=50, V_K=-77, V_L=-54.4, Cm=1):
        self.g_Na = g_Na
        self.g_K = g_K
        self.g_L = g_L
        self.V_Na = V_Na
        self.V_K = V_K
        self.V_L = V_L
        self.Cm = Cm
        y0 = [-65, 0.317, 0.05, 0.6]
        t = np.arange(0, self.duration, self.dt)
        solution = odeint(self.hh_model, y0, t)
        V, n, m, h = solution.T
        return t, V, n, m, h
