#ex1-mlclass plotData.py

#Before starting on any task, it is often useful to understand the data by
#visualizing it. For this dataset, you can use a scatter plot to visualize the
#data, since it has only two properties to plot (profit and population).

import numpy as np
import pylab as pl

print "Plotting data..."

data = np.genfromtxt('ex1data.csv', delimiter = ',')
dataT = data.transpose()

X = dataT[0]
y = dataT[1]

pl.plot(X, y, 'ro')
pl.xlabel('Population of City in 10,000s')
pl.ylabel('Profit in $10,000s')
pl.show()
