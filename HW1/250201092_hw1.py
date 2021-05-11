# When the difference between the expected value and the unexpected value is small, the variance value is at the
# highest level. When the difference between the expected value and the unexpected value is high, the variance value
# is at the lowest level.

import matplotlib.pyplot as plt

x = []  # x-axis
y = []  # y-axis
for i in range(101):
    p = i * 0.01        # p is expected value
    x.append(p)
    var = (1 - p) * p   # 1-p is unexpected value and var is variance
    y.append(var)

plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.xlabel('P VALUES')
plt.ylabel('VARIANCES')
plt.title('BERNOULLI DISTRIBUTION')
plt.show()

