import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

np.random.seed(3)
x = np.linspace(-np.pi, np.pi, 201)
y = np.sin(x)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()