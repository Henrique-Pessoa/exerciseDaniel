import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import signal


x = np.linspace(2,2 + 0.1,10)
y = np.linspace(3,5,100)

plt.plot(x,y)

plt.show()


num = (g1,g2)

den = (all,b,c)



sys = signal.TransferFunction(num,den)



time, voltagem = signal.step(sys)


plt.plot(time,voltagem, label = "Simulation")

plt.show()

