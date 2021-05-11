import numpy as np
import matplotlib.pyplot as plt

help(np.random.rand)
help(plt.hist)

# --------------------------Part-A------------------------------------------------

# we divide (0,1) 3 sub-intervals

N = 20  # trials
# ----Sub-intervals
p1 = 0.1
p2 = 0.3
p3 = 0.6
# --------------
Y1, Y2, Y3 = [], [], []

for j in range(1000):           # Returns the binomial distribution between [0,0.1].
    X1 = []
    for i in range(1, N+1):
        u = np.random.rand()
        x = u <= p1
        X1.append(x)            # Find success values
        y = sum(X1)
        Y1.append(y)
print(Y1)
plt.figure()
plt.title("Y1")
plt.hist(Y1, bins=range(0, N+1), density=True)
for j in range(1000):           # Returns the binomial distribution between (0.1, 0.4].
    X2 = []
    for i in range(1, N+1):
        u = np.random.rand()
        x = p1 < u <= p1+p2
        X2.append(x)            # Find success values
        y2 = sum(X2)
        Y2.append(y2)
for j in range(1000):           # Returns the binomial distribution between (0.4,1]
    X3 = []
    for i in range(1, N+1):
        u = np.random.rand()
        x = p1+p2 < u
        X3.append(x)            # Find success values
        y3 = sum(X3)
        Y3.append(y3)
Y4 = Y1 + Y2 + Y3
plt.figure()
plt.hist(Y4, bins=range(0, N+1), density=True)

# ---------------------------EndOfPart-A------------------------------------------------

# ---------------------------Part-B--------------------------------------------------

# 1. part   Geometric distribution with Bernouilli

p = 0.5
N = 8
X = []
for j in range(1000):
    for i in range(1, N+1):
        u = np.random.rand()
        x = u < p
        if x:
            X.append(i)     # when the success value is found, its index number added in X.
            break           # and break the loop
plt.figure()
plt.hist(X, bins=range(0, N+1), density=True)

# ---------------------------------------------------

# 2. Part    Geometric Distribution with using sub-intervals
# Sub-interval values are up. (Inside part A)

Y1, Y2, Y3 = [], [], []

for j in range(1000):
    for i in range(1, N+1):
        u = np.random.rand()
        if u <= p1:
            Y1.append(i)        # when the success value is found, its index number added in X.
            break               # and break the loop

for j in range(1000):
    for i in range(1, N+1):
        u = np.random.rand()
        if p1 < u <= p1+p2:
            Y2.append(i)        # when the success value is found, its index number added in X.
            break               # and break the loop

for j in range(1000):
    for i in range(1, N+1):
        u = np.random.rand()
        if p1+p2 < u:
            Y3.append(i)        # when the success value is found, its index number added in X.
            break               # and break the loop

Y4 = Y1 + Y2 + Y3
plt.figure()
plt.hist(Y4, bins=range(0, N+1), density=True)
plt.show()

# ---------------------------------EndOfPart-B------------------------------------------------------------------

# ---------------------------------Part-C--------------------------------------------------------------------


def not_swap_door(doors):
    random_doors = {1: "Prize", 2: "Goat", 3: "Goat"}
    choice = np.random.choice(list(random_doors.keys()))
    if choice == 1: # if choose the prize door
        return True
        # We have prize door So we win
    else:
        # We have not prize door so we loss
        return False


def swap_door(doors):
    random_doors = {1: "Prize", 2: "Goat", 3: "Goat"}
    choice = np.random.choice(list(random_doors.keys()))
    if choice == 1: # if chosen the prize door
        # We have prize door but we change the door with one of the other doors. So we loss
        return False
    else:
        # We have not prize door and we change the door So we will be choose the prize door
        return True


swap_door_wins = 0
not_swap_door_wins = 0

for i in range(1000):
    if swap_door(3):
        swap_door_wins += 1    # number of wins that are swap door in 1000 people
    if not_swap_door(3):
        not_swap_door_wins += 1 # number of wins that are no swap door in 1000 people

prob_sw_do_wins = float(swap_door_wins) / 10       # probability of wins that are swap door
prob_no_sw_do_wins = float(not_swap_door_wins) / 10 # probability of wins that are not swap door

print('People that are not swapping doors won you {0} prizes out of {1} ({2}%)'.format(not_swap_door_wins, 1000,
                                                                                       prob_no_sw_do_wins))
print('People that are Swapping doors won you {0} prizes out of {1} ({2}%)'.format(swap_door_wins, 1000,
                                                                                   prob_sw_do_wins))


# --------------------------------EndOfPart-C---------------------------------------------------------
