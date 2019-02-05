import rebound
from IPython.display import display, clear_output
import matplotlib.pyplot as plt
import ipywidgets as widgets
import numpy as np

sim = rebound.Simulation()
sim.G = 4*np.pi**2
sim.units = ['AU', 'yr', 'Msun']

sim.add(["Sun","Mercury","Venus","Earth","Mars"])

sim.add("NAME=1986 TO", m=6.537671975029727e-17)#3753 Cruithne

sim.add(["Jupiter","Saturn","Uranus","Neptune"])
sim.move_to_com()

sim.status()
#widget = sim.getWidget()
#display(widget)
#sim.integrate(1000)

Noutputs = 1000
year = 2.*np.pi # One year in units where G=1
times = np.linspace(0.,+10.*year, Noutputs)
x = np.zeros((2,Noutputs))
y = np.zeros((2,Noutputs))

sim.integrator = "ias15" # IAS15 is the default integrator, so we actually don't need this line
sim.move_to_com()        # We always move to the center of momentum frame before an integration
ps = sim.particles       # ps is now an array of pointers and will change as the simulation runs

for i,time in enumerate(times):
    sim.integrate(time)
    x[0][i] = ps[3].x   # Earth This stores the data which allows us to plot it later
    y[0][i] = ps[3].y
    x[1][i] = ps[5].x   # Cruithne
    y[1][i] = ps[5].y

fig = plt.figure(figsize=(5,5))
ax = plt.subplot(111)
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
plt.plot(x[0], y[0]);
plt.plot(x[1], y[1]);

fig = plt.figure(figsize=(12,5))
ax = plt.subplot(111)
ax.set_xlabel("time [yrs]")
ax.set_ylabel("distance [AU]")
distance = np.sqrt(np.square(x[0]-x[1])+np.square(y[0]-y[1]))
plt.plot(times/year, distance);
closeencountertime = times[np.argmin(distance)]/year
print("Minimum distance (%f AU) occured at time: %f years." % (np.min(distance),closeencountertime))



# sim.move_to_com()
# for time in np.linspace(0,1.,20):
#     sim.integrate(time)
#     #print(sim.calculate_energy())
#     fig = rebound.OrbitPlot(sim,color=True,unitlabel="[AU]",lim=2.)
#     display(fig)
#     plt.close(fig)
#     clear_output(wait=True)
