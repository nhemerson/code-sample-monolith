import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,19,0.01)

amplitude = (np.sin(time)) * 1
amplitude2 = (np.sin(time)) * (-1)

plt.clf()

plt.plot(time, amplitude, label = 'Engineering',linewidth=5.0)
plt.plot(time, amplitude2, label = 'Data Science',linewidth=5.0)

plt.title('3 Sprint Inverses (2 week time box)',fontsize=30)
plt.legend()
plt.xticks([])
plt.show()

