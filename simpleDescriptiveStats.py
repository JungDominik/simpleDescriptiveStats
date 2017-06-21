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

def histo(inList):
	for i in range(len(inList)):
		printString = str(i) + "   " + (inList[i] * "-")
		print(printString)

def mean(in_List):
	sum = 0
	for zahl in in_List:
		sum += zahl
	return (sum/len(in_List))

def median(in_List):
        listeLaenge = len(in_List)
        halbeLaenge = round(listeLaenge / 2)                    
        listeGeordnet = sorted(in_List)

        if listeLaenge % 2 == 0:
                oberMedian = listeGeordnet[halbeLaenge-1]
                unterMedian = listeGeordnet[halbeLaenge]
                return (unterMedian + oberMedian)/2
        else:
                return listeGeordnet[halbeLaenge-1]             

def mode(in_List):
        zaehlDict = {}
        for zahl in in_List:
                stringZahl = str(zahl)
                if stringZahl in zaehlDict:
                        zaehlDict[stringZahl] += 1
                else:
                        zaehlDict[stringZahl] = 1
        dict_items_ListeGesortedValues = sorted(zaehlDict.items(), key = lambda x : x[1], reverse = True)       
        return dict_items_ListeGesortedValues[0][0]                                                            
                                                
def variance(in_list):
	listMean = mean(in_list)
	sumSquared = 0
	for zahl in in_list:
		sumSquared += ((zahl - listMean)**2)
	return (sumSquared / (len(in_list)-1))


def findSD(in_list):
	listVar = variance(in_list)
	return math.sqrt(listVar)

def standardiseScore(in_wert, in_group):
        meanAbweichung = in_wert - mean(in_group)
        return (meanAbweichung / findSD(in_group))

def standardiseList (in_list):
        returnList = []
        for eintrag in in_list:
                returnList.append(standardiseScore(eintrag, in_list))
        return returnList

def listsPearsonR(in_listA, in_listB):
        standardsMultiSum = 0
        for i in range (len(in_listA)):
                standardsMultiSum += (standardiseScore(in_listA[i], in_listA) * standardiseScore(in_listB[i], in_listB))
        return (standardsMultiSum / (len(in_listA) - 1))                


def listsPearsonRSquared(in_listA, in_listB):
        rSquared = (listsPearsonR(in_listA, in_listB))**2
        return rSquared