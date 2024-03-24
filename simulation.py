import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, ode
 
"""
https://www.sciencedirect.com/science/article/pii/S0022519315004142
"""
 
def dFdt_original(F,t):
    """
    System of differential equations
    """
    dF = [0,0,0,0,0] # P, S, N, G, C
    P = F[0]
    S = F[1]
    N = F[2]
    G = F[3]
    C = F[4]
 
    dF[0] = -k_s*S*P - k_G*P - k_450*P + k_N*N
    dF[1] = -k_s*S*P + b_s - d_s*S
    dF[2] = k_450*P - k_N*N - k_GSH*N*G - k_PSH*N
    dF[3] = -k_GSH*N*G + b_G - d_G*G
    dF[4] = k_PSH*N
   
    return dF
 
d_G = 2
b_G = 1.374e-14
k_GSH = 1.6e18
k_G = 2.99
k_s = 2.26e14
b_s = 2.65e-14
d_s = 2
k_450 = 0.315
k_N = 0.0315
k_PSH = 110
 
P_0 = 1.32e-13
 
# Times
t_min = 0; t_max = 5; dt = 0.001
times = np.arange(t_min, t_max+dt, dt) #generate time-grid list
 
### Simulation ###
F0 = [P_0, b_s/d_s, 0, b_G/d_G, 0] # initial conditions ### these match what the paper had
print(F0)
F = odeint(dFdt_original, F0, times) #run simulation
 
plt.plot(times, F[:, 1])
plt.show()

print(F.shape)