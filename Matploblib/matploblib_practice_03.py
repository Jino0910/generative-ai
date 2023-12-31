
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
data = np.random.randn(5000)
plt.hist(data, 100, density=True)

# normal distribution
x = np.linspace(-4,4,100)
sigma = 1
mean = 0
nd = ( (1/(sigma*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mean)/sigma)**2)) )
plt.plot(x,nd,  'r', label='Std Normal Dist')
plt.ylabel('PSD')
plt.xlabel('X')
plt.legend()

np.std(data)

# %% 3D plot
x = np.linspace(0,2*np.pi,20)
y = np.linspace(0,2*np.pi,20)
grid_x, grid_y = np.meshgrid(x,y)

z = np.sin(grid_x)*np.sin(grid_y)

hfig = plt.figure()
hax = hfig.gca(projection='3d')
hax.plot_surface(grid_x,grid_y,z,camp='jet')
hax.set_xlabel('y')
hax.set_xlabel('x')
hax.set_xlabel('z')

# %% Simple Animation

fig, ax = plt.subplots()

x = np.array([1,2,3,4,5])
y = np.array([1,1,1,1,1])

hp, = ax.plot(x,y)
ax.set_ybound([0,11])

for i in range(0,11,1):
    hp.set_ydata(i*y)
    plt.pause(0.5)
    #





