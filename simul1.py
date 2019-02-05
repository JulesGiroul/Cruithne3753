import rebound
from IPython.display import display, clear_output
import matplotlib.pyplot as plt

sim = rebound.Simulation()
sim.getWidget()
sim.add("Sun")
## Other examples:
sim.add("Mercury")
sim.add("Venus")
sim.add("Earth")
#sim.add("Jupiter")
#sim.add("Saturn")
#sim.add("Uranus")
#sim.add("Neptune")


sim.status()
sim.integrate(5)
#matplotlib inline
fig = rebound.OrbitPlot(sim)
fig.show()
plt.show()
