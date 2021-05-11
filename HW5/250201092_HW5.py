# 250201092

import numpy as np
import matplotlib.pyplot as plt

sampleSize = 100000


def calc_mean(value_list):  # Calculation of mean
    total = 0
    for i in value_list:
        total += i
    mean = total / len(value_list)
    return mean


def calc_standard_deviation(value_list):  # Calculation of standard deviation
    mean = calc_mean(value_list)
    variance = 0
    for i in value_list:
        variance += (mean - i) ** 2
    standard_deviation = variance ** 0.5  # standard deviation is square root of variance
    return standard_deviation / len(value_list) ** 0.5


def Experiment_1_2_3(experiment_list):  # experiment_list is taken experiment values are [2, 10, 50]
    random_variables = []
    sum_of_random_variables = []
    counter = 0  # counter is number of experiment
    for i in experiment_list:
        counter += 1
        random_variables.clear()
        sum_of_random_variables.clear()
        for j in range(sampleSize):
            sums = 0
            for k in range(i):
                n = np.random.rand()
                sums += n   # Sum of i numbers
                random_variables.append(n)  # random_variables list is the list that include all variables (100000 * i)

            sum_of_random_variables.append(sums) # sum_of_random_variable list is the list that include the all sums

        print("------------- Experiment ", counter, " ---------------")
        sample_mean = calc_mean(sum_of_random_variables)  # Sample mean
        std_deviation = calc_standard_deviation(sum_of_random_variables) # Sample standard deviation
        print("Sample mean is ", sample_mean)
        print("Sample standard deviation is ", std_deviation)

        if counter == 1:
            plt.figure("Experiment " + str(counter) + ".1")
            plt.title("Histogram for generated random variables")
            plt.hist(random_variables, bins=100, alpha=0.5, density=True)
            plt.figure("Experiment " + str(counter) + ".2")
            plt.title("Histogram for sums of generated random variables")
            number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(-1, 3), density=True)
            plt.plot(bins, 1/(std_deviation*np.sqrt(2*np.pi))*np.exp(-(bins-sample_mean)**2/(2*std_deviation**2)))
            plt.show()
        elif counter == 2:
            plt.figure("Experiment " + str(counter))
            plt.title("Histogram for sums of generated random variables")
            number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(0, 10), density=True)
            plt.plot(bins, 1./(std_deviation*np.sqrt(2 * np.pi))*np.exp(-(bins - sample_mean)**2/(2*std_deviation**2)))
            plt.show()
        else:
            plt.figure("Experiment " + str(counter))
            plt.title("Histogram for sums of generated random variables")
            number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(15, 35), density=True)
            plt.plot(bins, 1./(std_deviation*np.sqrt(2*np.pi))*np.exp(-(bins - sample_mean)**2/(2*std_deviation**2)))
            plt.show()


def Experiment_4(exp4):
    random_variables = []
    sum_of_random_variables = []

    for i in range(sampleSize):
        sum = 0
        for j in range(exp4):
            if sum < 40:
                n = np.random.uniform(0.5, 1.5)
                random_variables.append(n)
                sum += n
            else:
                n = np.random.uniform(-0.5, 0.5)
                random_variables.append(n) # random_variables list is the list that include all variables (100000 * i)
                sum += n
        sum_of_random_variables.append(sum) # sum_of_random_variable list is the list that include the all sums

    print("------------- Experiment 4 ---------------")
    sample_mean = calc_mean(sum_of_random_variables)                    # Sample mean
    std_deviation = calc_standard_deviation(sum_of_random_variables)    # Sample standard deviation
    print("Sample mean is ", sample_mean)
    print("Sample standard deviation is ", std_deviation)

    plt.figure("Experiment 4.1")
    plt.title("Histogram for generated random variables")
    plt.hist(random_variables, bins=100, alpha=0.5, density=True)
    plt.figure("Experiment 4.2")
    plt.title("Histogram for sums of generated random variables")
    plt.xlim([36, 50])
    number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(35, 51), density=True)
    plt.plot(bins, 1 / (std_deviation*np.sqrt(2 * np.pi))*np.exp(-(bins - sample_mean)**2 / (2 * std_deviation**2)))
    plt.show()


def Experiment_5_6_7(experiment_list):
    random_variables = []
    sum_of_random_variables = []
    counter = 5  # counter is number of experiment
    c = 2  # center
    R = 1  # radius
    for i in experiment_list:
        random_variables.clear()
        sum_of_random_variables.clear()
        for j in range(sampleSize):
            sum = 0
            for k in range(i):
                phi = np.random.rand() * np.pi
                r = np.sqrt(np.random.rand()) * R
                x = r * np.cos(phi) + c
                sum += x
                random_variables.append(x)  # random_variables list is the list that include all variables (100000 * i)

            sum_of_random_variables.append(sum)  # sum_of_random_variable list is the list that include the all sums

        print("------------- Experiment ", counter, " ---------------")
        sample_mean = calc_mean(sum_of_random_variables)                    # Sample mean
        std_deviation = calc_standard_deviation(sum_of_random_variables)    # Sample standard deviation
        print("Sample mean is ", sample_mean)
        print("Sample standard deviation is ", std_deviation)

        if counter == 5:
            plt.figure("Experiment " + str(counter) + ".1")
            plt.title("Histogram for generated random variables")
            plt.hist(random_variables, bins=100, alpha=0.5, density=True)
            plt.figure("Experiment " + str(counter) + ".2")
            plt.title("Histogram for sums of generated random variables")
            number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(1, 7), density=True)
            plt.plot(bins, 1/(std_deviation*np.sqrt(2 * np.pi))*np.exp(-(bins - sample_mean)**2/(2 * std_deviation**2)))
            plt.show()
        elif counter == 6:
            plt.figure("Experiment " + str(counter))
            plt.title("Histogram for sums of generated random variables")
            number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(12, 28), density=True)
            plt.plot(bins, 1./(std_deviation*np.sqrt(2*np.pi))*np.exp(-(bins-sample_mean)**2 / (2*std_deviation**2)))
            plt.show()
        else:
            plt.figure("Experiment " + str(counter))
            plt.title("Histogram for sums of generated random variables")
            number, bins, ign = plt.hist(sum_of_random_variables, 100, range=(85, 115), density=True)
            plt.plot(bins, 1./(std_deviation*np.sqrt(2*np.pi))*np.exp(-(bins-sample_mean)**2/(2*std_deviation**2)))
            plt.show()
        counter += 1


def main():
    experiments = [2, 10, 50]
    Experiment_1_2_3(experiments)
    Experiment_4(100)
    Experiment_5_6_7(experiments)


main()
