# Ison Thomas For Loops Basics 2


# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def bigFunk(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = 'big'
    return list

print(bigFunk([-1,3,5,-5]))

## 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
##Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it

def countFunk(list):
    count = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            count += 1
        list[len(list)-1] = count
    return list

print(countFunk([-1,1,1,1]))

# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
def sumTotalFunk(list):
    sum = 0

    for i in range(0,len(list)):
        sum += list[i]

    return sum

print(sumTotalFunk([1,2,3,4]))

# 4 Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def averageFunk(list):
    sum = 0
    avg = 0

    for i in range(0, len(list)):
        sum += list[i]
    avg = sum / len(list)
    return avg

print(averageFunk([1,2,3,4]))

# 5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4

def lengthFunk(list):
    length = len(list)
    
    if len(list) <= 0:
        return 0
    
    return length

print(lengthFunk([1,2,3,4]))
print(lengthFunk([]))

# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9

def minFunk(list):
    if len(list) <= 0:
        return False

    min = list[0]
    for i in range(0, len(list)):
        if list[i] < min:
            min = list[i]

    return min

print(minFunk([4,2,9,-5]))
print(minFunk([]))

# 7 Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37

def maxFunk(list):
    if len(list) <= 0:
        return False

    max = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]

    return max

print(maxFunk([4,2,9,-5]))
print(maxFunk([]))

# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultiFunk(list):

    analysis = {}

    analysis["sumTotal"] = 0
    analysis["average"] = 0
    analysis["minimum"] = 0
    analysis["maximum"] = 0
    analysis["length"] = len(list)

    for i in range(0, len(list)):
        if analysis["maximum"] < list[i]:
            analysis["maximum"] = list[i]
        elif analysis["minimum"] > list[i]:
            analysis["minimum"] = list[i]
        analysis["sumTotal"] += list[i]

        analysis["average"] = analysis["sumTotal"] / analysis["length"]

    return analysis

print(ultiFunk([37,2,1,-9]))

# 9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseFunk(listy):
    
    for i in range(0, len(listy)):
        if i < len(listy)/2:
            listy[i], listy[len(listy)-1 -i] = listy[len(listy)-1-i], listy[i]


    return listy
    
print(reverseFunk([37,2,1,-9]))
