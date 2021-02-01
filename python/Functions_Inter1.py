# Ison Thomas Functions Intermediate 1

import random

def randInt(min = 0, max = 100):
    if min > max or max < 0:
        return "Min needs to be less than Max"
        
    num = round(random.random() * (max - min) + min)

    return num

print(randInt())
print(randInt(max = 75))
print(randInt(min = 90))
print(randInt(min = 25, max = 30))
print(randInt(min = 35, max = 30))
