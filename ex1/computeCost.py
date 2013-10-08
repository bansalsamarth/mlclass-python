import numpy as np

#The function computes the cost of using theta as the parameter 
#for linear regression to fit the data points in X and y

def computeCost(X, y, theta):
    m = len(y)					#number of training examples
    X = np.array([np.ones(m), X])		#Added a column with all ones to X
    X = X.transpose()
   
    theta = theta.transpose()
    c = np.dot(X, theta)			#Matrix multiplication X*theta
    c = c.transpose() - y
    J = np.sum(c**2)/(2*m)			#Calculating cost

    return J
