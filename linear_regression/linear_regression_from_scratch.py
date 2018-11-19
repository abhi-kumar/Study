import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

np.random.seed(3)
x = np.linspace(-np.pi, np.pi, 201)
y = np.sin(x)

#slope = sum(
#			(x(i) - mean(x)) * (y(i) - mean(y))
#		) 
#		/ sum( 
#			(x(i) - mean(x))^2
#		)

#intercept = mean(y) - slope * mean(x)

print x.shape

mean_x = x.mean()
mean_y = y.mean()

print mean_x, mean_y

slope_num = 0.0
slope_den = 0.0
for i in range(x.shape[0]):
	slope_num += (x[i] - mean_x) * (y[i] - mean_y)
	slope_den += (x[i] - mean_x) * (x[i] - mean_x)

slope = slope_num/slope_den

intercept = mean_y - slope * mean_x

print slope, intercept


plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()
