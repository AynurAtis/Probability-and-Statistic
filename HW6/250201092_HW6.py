import numpy as np
import matplotlib.pyplot as plt

sampleSize = 1000


def calc_mean(sampleList):   # calculation of sample mean
    total = 0
    for i in sampleList:
        total += i
    return total / len(sampleList)


def calc_Variance(sampleList):  # calculation of sample variance
    sampleMean = calc_mean(sampleList)
    sampleVariance = 0
    for k in sampleList:
        sampleVariance += (sampleMean - k) ** 2
    return sampleVariance / len(sampleList)


def calc_StandardDeviation(sampleList):  # standard deviation is square root of the variance
    sampleStandardDeviation = calc_Variance(sampleList) ** 0.5
    return sampleStandardDeviation


def binomialDistribution(binomial_n):
    binomial_p = 0.3
    X = []
    for j in range(binomial_n):  # binomial_n = 40
        u = np.random.rand()  # creates a random number between 0-1
        x = u < binomial_p  # x is boolean, if u which is random number smaller than
        X.append(int(x))  # binomial_p = 0.3, the result is success , X list includes the 0 or 1

    y = sum(X)  # y is the sum of success experiment in 40 number
    return y


def MethodOfMoment(N):

    binomial_n = 40
    estimated_P_list = []
    estimated_N_list = []

    for i in range(sampleSize): # sampleSize = 1000
        successList = []
        for j in range(N):  # N = 200, 800, 3200
            y = binomialDistribution(binomial_n)  # Call the binomialDistribution function
            successList.append(y)   # All success experiments assign to successList list times N

        sampleMean = calc_mean(successList)  # sample mean in successList list
        sampleVariance = calc_Variance(successList)       # sample variance in successList list

        estimated_p = 1 - (sampleVariance / sampleMean)     # estimated_p = p^
        estimated_P_list.append(estimated_p)    # estimated_P_list includes the estimated_p 1000 number
        estimated_n = sampleMean / estimated_p  # estimated_n = n^
        estimated_N_list.append(estimated_n)    # estimated_N_list includes the estimated_n 1000 number

    mean_for_estimated_P = calc_mean(estimated_P_list)  # Mean of the estimated P
    standard_deviation_estimated_P = calc_StandardDeviation(estimated_P_list)   # Standard deviation of the estimated P
    mean_for_estimated_N = calc_mean(estimated_N_list)   # Mean of the estimated n
    standard_deviation_estimated_N = calc_StandardDeviation(estimated_N_list)   # Standard deviation of the estimated n

    print("Mean for estimated p for sample size of " + str(N) + " is", mean_for_estimated_P)
    print("Standard deviation for estimated p for sample size of " + str(N) + " is", standard_deviation_estimated_P)
    print("Mean for estimated n for sample size of " + str(N) + " is", mean_for_estimated_N)
    print("Standard deviation for estimated n for sample size of " + str(N) + " is", standard_deviation_estimated_N)

    return [estimated_P_list, estimated_N_list]


def main():
    sampleSize_200 = MethodOfMoment(200)
    sampleSize_800 = MethodOfMoment(800)
    sampleSize_3200 = MethodOfMoment(3200)
    plt.figure()
    plt.title("Histogram for estimated p")
    plt.hist(sampleSize_200[0], bins=100, range=(0.1, 0.5), label='200', density=True)
    plt.legend(loc='upper right')
    plt.hist(sampleSize_800[0], bins=100, range=(0.1, 0.5), label='800', density=True)
    plt.legend(loc='upper right')
    plt.hist(sampleSize_3200[0], bins=100, range=(0.1, 0.5), label='3200', density=True)
    plt.legend(loc='upper right')
    plt.figure()
    plt.title("Histogram for estimated n")
    plt.hist(sampleSize_200[1], bins=100, range=(20, 140), label='200', density=True)
    plt.legend(loc='upper right')
    plt.hist(sampleSize_800[1], bins=100, range=(20, 140), label='800', density=True)
    plt.legend(loc='upper right')
    plt.hist(sampleSize_3200[1], bins=100, range=(20, 140), label='3200', density=True)
    plt.legend(loc='upper right')
    plt.show()


main()
