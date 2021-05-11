import numpy as np
from matplotlib import pyplot as plt
import math

numSamples = 100000
numBins = 100


# For the random variable X, Fx(x) = 0.36 * ln|3x+2| - 0.36 * ln|2|.
# To find cdf of x, we calculate integration of f(x) = 1.08/3x+2 for bounded 0 to x.
# Then we obtain function of F(x) = 0.36 * ln|3x+2| - 0.36 * ln|2|.

def Fx(x):
    if x < 0:
        return 0
    elif x <= 10:
        return 0.36 * math.log((3*x + 2) / 2)
    else:
        return 1


Fx_array = []
ind = []
for i in range(-100, 1200):
    Fx_array.append(Fx(i / 100))
    ind.append(i / 100)
plt.figure()
plt.title('Cdf of X')
plt.plot(ind, Fx_array)

# inverse transformation method
print('-------------------------- Inverse transformation method for X--------------------------')


def Fx_inverse(u):
    return (np.exp(u / 0.36) * 2 - 2) / 3   # inverse of 0.36 * log(3x+2) /2


U = []
X = []
for i in range(numSamples):
    U.append(np.random.rand())
    X.append(Fx_inverse(U[i]))
plt.figure()
plt.title('Histograms of the generated U and X samples (pdf)')
hU = plt.hist(U, numBins, alpha=0.5, density=True)
hX = plt.hist(X, numBins, alpha=0.5, density=True)
plt.figure()
plt.title('Normalized cumulative sum of histogram values for the generated U and X samples (cdf)')
plt.plot(np.cumsum(hU[0]) / hU[0].sum())
plt.plot(np.cumsum(hX[0]) / hX[0].sum())
plt.show()


# ################################################################################################

# For the random variable Y, fy(y) = 2y:
# To find pdf of y, we calculate derivation of f(y) = y**2.
# Then we obtain function of f'(y) = 2y and we apply y function as f(y).

def fy(y):
    if y < 0:
        fy = 0
    elif y <= 1:
        fy = 2 * y
    else:
        fy = 0
    return fy


fy_array = []
ind = []
for i in range(-100, 200):
    fy_array.append(fy(i / 100))
    ind.append(i / 100)
plt.figure()
plt.title('Pdf of Y')
plt.plot(ind, fy_array)

# rejection method
print('----------------------------- Rejection method for Y -----------------------------')
c = 1
a = -0.001
b = 10
Y = []
i = 0
while i < numSamples:
    u = np.random.rand()
    v = np.random.rand()
    x = (b - a) * u + a
    y = c * v
    if x <= fy(y):
        Y.append(y)
        i = i + 1

plt.figure()
plt.title('Histogram of the generated Y samples (pdf)')
hY = plt.hist(Y, numBins, density=True)
plt.figure()
plt.title('Normalized cumulative sum of histogram values for the generated Y samples (cdf)')
plt.plot(hY[1][0:numBins], np.cumsum(hY[0]) / hY[0].sum())
plt.show()
