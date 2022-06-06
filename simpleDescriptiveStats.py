### Simple Descriptive Statistics Package v 0.6 (Training project)
###
### Implements Python functions for exploratory analysis of data given as a standard python list 
### -Displaying data (Histogram)
### -Measures of central tendency: Mean, Median, Mode
### -Measures of dispersion: Variance, Standard Deviation
### -Standardization: Z-Score
### -Correlation: Pearsons R, Pearsons R-Squared
### 
### 

import math

def histo(inList):
	for i in range(len(inList)):
		printString = str(i) + "   " + (inList[i] * "-")
		print(printString)

def mean(in_List):
	sum = 0
	for num in in_List:
		sum += num
	return (sum/len(in_List))

def median(in_List):
        listLength = len(in_List)
        halfLength = round(listLength / 2)                    
        listOrdered = sorted(in_List)

        if listLength % 2 == 0:
                upperMedian = listOrdered[halfLength-1]
                lowerMedian = listOrdered[halfLength]
                return (lowerMedian + upperMedian)/2
        else:
                return listOrdered[halfLength-1]             

def mode(in_List):
        countDict = {}
        for num in in_List:
                stringnum = str(num)
                if stringnum in countDict:
                        countDict[stringnum] += 1
                else:
                        countDict[stringnum] = 1
        dict_items_ListSortedValues = sorted(countDict.items(), key = lambda x : x[1], reverse = True)       
        return dict_items_ListSortedValues[0][0]                                                            
                                                
def variance(in_list):
	listMean = mean(in_list)
	sumSquared = 0
	for num in in_list:
		sumSquared += ((num - listMean)**2)
	return (sumSquared / (len(in_list)-1))

def covariance(in_list_x, in_list_y):
        if len(in_list_x) != len(in_list_y):
                raise Exception('The input lists have different length.')
        
        n = len(in_list_x)
        mean_x = mean(in_list_x)
        mean_y = mean(in_list_y)
        
        sum = 0
        for i in range(n):
                sum += (in_list_x[i] - mean_x) * (in_list_y[i] - mean_y)
        
        returnval = sum / (n-1)
        
        return returnval
        

def findSD(in_list):
	listVar = variance(in_list)
	return math.sqrt(listVar)

def standardiseScore(in_wert, in_group):
        meanDeviation = in_wert - mean(in_group)
        return (meanDeviation / findSD(in_group))

def standardiseList (in_list):
        returnList = []
        for eintrag in in_list:
                returnList.append(standardiseScore(eintrag, in_list))
        return returnList

def listsPearsonR(in_list_x, in_list_y):
        if len(in_list_x) != len(in_list_y):
                raise Exception("The input lists have different legnth.")
       
        n = len(in_list_x)
        
        standardsMultiSum = 0
        for i in range (len(in_list_x)):
                standardsMultiSum += (standardiseScore(in_list_x[i], in_list_x) * standardiseScore(in_list_y[i], in_list_y))

        return (standardsMultiSum / (n - 1))                


def listsPearsonRSquared(in_list_x, in_list_y):
        if len(in_list_x) != len(in_list_y):
                raise Exception("The input lists have different legnth.")
                
        rSquared = (listsPearsonR(in_list_x, in_list_y))**2
        return rSquared


def pearsonR_alt(in_list_x, in_list_y):                 #Alternative implementation of Pearson's R
        if len(in_list_x) != len(in_list_y):
                raise Exception("The input lists have different legnth.")
       
        cov_xy = covariance(in_list_x, in_list_y)
        sd_x = findSD(in_list_x)
        sd_y = findSD(in_list_y)

        return cov_xy / (sd_x * sd_y)




######### Test Data
test_X = [1,4,6,3,6,7,4,3,6,7,8,1,3,3,5,4,3,6,1,8,2]
test_Y = [7,3,4,2,0,1,8,5,5,3,2,1,7,5,8,9,6,7,8,3,4]

return_abc = [1.1, 1.7, 2.1, 1.4, 0.2]
return_xyz = [3, 4.2, 4.9, 4.1, 2.5]

r_x = [43,21,25,42,57,59]
r_y = [99,65,79,75,87,81]