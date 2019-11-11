#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Kamis, 07 November 2019 //////////////////////////////////////

#TODO Membuat fungsi rata - rata
def findMean(param):
    length = len(param)
    tempVal = 0
    for i in param:
        tempVal += i

    return (tempVal/length)

#TODO Membuat fungsi modus
def findMode(param):
    paramDict = {}
    newList = []
    maxCount = 0
    for i in param:
        paramDict.setdefault(i, 0)
        paramDict[i] += 1
    print(paramDict)
    
    for i in paramDict:
        if maxCount < paramDict[i]:
            maxCount = paramDict[i]

    for i in paramDict:
        if paramDict[i] == maxCount:
            newList.append(i)
    return newList

#TODO Membuat fungsi nilai tengah
def findMedian(param):
    param = sorted(param)
    length = len(param)
    if(length%2==1):
        medianValue = param[int(length/2)+1]
    else:
        medianValue = (param[int(length/2)-1] + param[int(length/2)]) / 2

    return medianValue