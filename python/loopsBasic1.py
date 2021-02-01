## Ison Thomas For Loop Basic 1
#
#for count in range(151):
#    print(count)
#
#for i in range (5, 1005, 5):
#    print(i)
#
#for i in range (1,101):
#    if i % 10 == 0:
#        print ("Dojo")
#    elif i % 5 == 0:
#        print ("Coding")
#    else:
#
#sum = 0
#
#for i in range (0, 500000):
#    sum += i
#
#print(sum)
#
#
#for i in range (2018, 0, -4):
#    print(i)
#
#
#def multiples (lowNum, highNum, mult):
#    for i in range(lowNum,highNum + 1):
#        if i % mult == 0:
#            print(i)
#
#multiples(3,9,3)


# Zip lists into dictionary

# Given two lists, create a dictionary containing keys from the first list,
# and values from the second.

# Input: ["abc", 3, "yo"], [42, "wassup", True]
# Output: {
#   "abc": 42,
#   3: "wassup",
#   "yo": True,
# }

def zippy(list1,list2):
    newDict = {}
    for i in range(len(list1)):
        newDict[list1[i]] = list2[i]
    return newDict

#    print(newDict)

print(zippy(["abc", 3, "yo"],[42, "wassup", True]))
    


#list1 = ["abc", 3, "yo"]
#list2 = [42, "wassup", True]
#
#def zip_list(list1, list2):
#    newdict = {list1[i]: list2[i] for i in range(len(list1))}
#    return newdict
#
#print (zip_list(list1, list2))


def swapper(incoming):
    new_dict = {}
    for key, val in incoming.items():
        new_dict[val] = key
    return new_dict

print(swapper({"name": "Zaphod", "charm": "high", "morals": "dicey"}))

#def zipped(dict):
#    newDict = {}
#    for i in range(0,len(dict)):
#        dict.key[i] = dict.val[i]+1
#        print(dict)
#
#
#print(zipped({ "name": "Zaphod", "charm": "high", "morals": "dicey" }))

# Invert Hash

# Given a dictionary, return a new dictionary that has the keys and the values
# swapped so that the keys become the values and the values become the keys

# Input: { "name": "Zaphod", "charm": "high", "morals": "dicey" }
# Output: { "Zaphod": "name", "high": "charm", "dicey": "morals" }
