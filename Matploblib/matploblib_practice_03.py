
# %%
import numpy as np
import matplotlib.pyplot as plt

# %% -- decay sine example

t = np.linspace(0, 100, 1000)
tau = 100
y = np.sin(t)*np.exp(-t/tau)
plt.plot(t, y, label='Decay OsciLLating Response')
plt.ylabel('y [m]')
plt.xlabel('t [s]')
plt.legend()

# %% -- Euler eq
t = np.linspace(0,1,100)
f = 1 # frequency [Hz]
y_euler = np.exp(1j*2*np.pi*f*t)
y_cos = np.real(y_euler)
y_sin = np.imag(y_euler)

hfig, hax = plt.subplots()
hax.plot(t,y_cos,'-r',label='cos')
hax.plot(t,y_sin,'--b',label='sin')
hax.grid()
hax.legend()

hfig, hax = plt.subplots(2,1)
hax[0].plot(t,y_cos,'-r',label='cos')
hax[1].plot(t,y_sin,'--b',label='sin')
hax[0].grid()
hax[0].legend()
hax[1].grid()
hax[1].legend()

# %% -- Histrogram
data = np.random.randn(10000)
plt.hist(data, 100, den)