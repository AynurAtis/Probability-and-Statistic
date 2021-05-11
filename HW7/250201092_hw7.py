import numpy as np
import matplotlib.pyplot as plt


def readFile():   # Read the titanic_data.txt file
    file = open("titanic_data.txt")
    dataList = [[]]
    result = [line.strip() for line in file]
    for i in result:
        split_line = i.split("\t")
        dataList.append(split_line)
    file.close()
    return dataList


def calcMean(dataList):  # Calculation of the data
    mean = 0
    for data in dataList:
        mean += int(data)
    mean /= len(dataList)
    return mean


def crewAndThirdClassPassengers(crewData, thirdClass):  # Third Class and crew calculation
    shuffleList = []
    newCrewData = []
    newThirdClass = []
    differenceBetweenMeans = []
    numBins_index = 0
    pValueArray = [0]
    x = calcMean(crewData) - calcMean(thirdClass)  # Difference between means of crewData and thirdClass
    for k in range(10000):
        for i in crewData:
            shuffleList.append(i)
        for j in thirdClass:
            shuffleList.append(j)
        np.random.shuffle(shuffleList) # Two lists are shuffled
        for l in range(len(crewData)):
            newCrewData.append(shuffleList[l])
        for m in range(len(crewData), len(shuffleList)):
            newThirdClass.append(shuffleList[m])
        meanNewCrewData = calcMean(newCrewData)
        meanNewThirdClass = calcMean(newThirdClass)
        sampleMean = meanNewCrewData - meanNewThirdClass
        differenceBetweenMeans.append(sampleMean)
        newCrewData.clear()
        newThirdClass.clear()
        shuffleList.clear()
    plt.figure(figsize=(12, 6))
    cdfHist, numBins, c = plt.hist(differenceBetweenMeans, bins=100, range=(-0.08, 0.08), density=False) # PDF graph
    cdf = np.cumsum(cdfHist) / cdfHist.sum()
    numBins = numBins[1:]
    for bin in range(len(numBins)):
        if numBins[bin] >= x:
            numBins_index = bin
            break

    pValue = cdf[numBins_index]
    pValueArray.append(round(pValue, 2))
    xValueArray = [x, x]
    plt.figure(figsize=(12, 6))
    plt.plot(numBins, cdf)  # CDf graph
    plt.plot(xValueArray, pValueArray)
    print("The p-value for " + str(round(x, 2)) + " difference and less between means for crew and 3rd class is "
          + str(round(pValue, 2)) + ".")
    plt.show()


def firstClassAndRest(crewData, firstClass, secondClass, thirdClass):
    shuffleList = []
    newFirstClass = []
    restData = []
    newRestData = []
    differenceBetweenMeans = []
    numBins_index = 0
    pValueArray = [0]

    # crewData, secondClass and thirdClass added in restData.
    for i in crewData:
        restData.append(i)
    for j in secondClass:
        restData.append(j)
    for k in thirdClass:
        restData.append(k)
    x = calcMean(firstClass) - calcMean(restData)  # Difference between means of firstClass and restData

    for l in range(10000):
        for i in firstClass:
            shuffleList.append(i)
        for j in restData:
            shuffleList.append(j)
        np.random.shuffle(shuffleList)  # Two lists are shuffled.
        for t in range(len(firstClass)):
            newFirstClass.append(shuffleList[t])
        for s in range(len(firstClass), len(shuffleList)):
            newRestData.append(shuffleList[s])
        meanNewFirstClass = calcMean(newFirstClass)
        meanNewRestData = calcMean(newRestData)
        sampleMean = meanNewFirstClass - meanNewRestData
        differenceBetweenMeans.append(sampleMean)
        newFirstClass.clear()
        newRestData.clear()
        shuffleList.clear()
    plt.figure(figsize=(12, 6))
    cdfHist, numBins, c = plt.hist(differenceBetweenMeans, bins=100, range=(-0.1, 0.1),  density=False)  # PDF graph
    cdf = np.cumsum(cdfHist) / cdfHist.sum()
    numBins = numBins[1:]
    for bin in range(len(numBins)):
        if numBins[bin] >= x:
            numBins_index = bin
            break
    pValue = cdf[numBins_index]
    pValueArray.append(round(pValue, 2))
    xValueArray = [x, x]
    plt.figure(figsize=(12, 6))
    plt.plot(numBins, cdf)              # CDF graph
    plt.plot(xValueArray, pValueArray)
    print("The p-value for " + str(round(x, 2)) + " difference and more in means for 1st class and the rest is "
          + str(pValue) + ".")
    plt.show()


def main():
    dataList = readFile()   # Call the readFile function
    dataList.pop(0)
    dataList.pop(0)
    # First 2 elements are popped because first element is empty list, and second element is [Class, Survive]
    # Thus, No need them.
    crewData = []
    firstClass = []
    secondClass = []
    thirdClass = []
    wholeData = []
    for i in range(len(dataList)):
        if dataList[i][0] == '1':
            firstClass.append(dataList[i][1])
        elif dataList[i][0] == '2':
            secondClass.append(dataList[i][1])
        elif dataList[i][0] == '3':
            thirdClass.append(dataList[i][1])
        elif dataList[i][0] == '0':
            crewData.append(dataList[i][1])
        wholeData.append(dataList[i][1])  # all survive data

    meanWholeData = calcMean(wholeData)
    meanCrewData = calcMean(crewData)
    meanFirstClass = calcMean(firstClass)
    meanSecondClass = calcMean(secondClass)
    meanThirdClass = calcMean(thirdClass)

    print("The averages for the whole data, crew data, first class, second class and third class data are " +
          str(round(meanWholeData, 2)) + ", " + str(round(meanCrewData, 2)) + ", " + str(round(meanFirstClass, 2)) +
          ", " + str(round(meanSecondClass, 2)) + " and " + str(round(meanThirdClass, 2)) + " respectively.")

    crewAndThirdClassPassengers(crewData, thirdClass)               # Crew and ThirdClass
    firstClassAndRest(crewData, firstClass, secondClass, thirdClass)  # FirstClass and Rest


main()
