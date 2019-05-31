################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~ Created ~~~~~~~~~~~#
#~~~~~~~ By: Eric Morse ~~~~~~~#
#~~~~~~ Date: Apr.23.2019 ~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
################################

import math

# Vector Class, will store 2 values, generally a x and a y
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Vector3 class, will store 3 values, generally a x, y, and a z
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Big for biggest on left, small for smallest on left
def InsertionSort(list, direction):
        for i in range(len(list)):
            cursor = list[i]
            pos = i

            if (direction.lower() == 'big'):
                while pos > 0 and list[pos - 1] < cursor:
                    # Swap the number down the list
                    list[pos] = list[pos - 1]
                    pos = pos - 1
            elif (direction.lower() == 'small'):
                while pos > 0 and list[pos - 1] > cursor:
                    # Swap the number down the list
                    list[pos] = list[pos - 1]
                    pos = pos - 1
            # Break and do the final swap
            list[pos] = cursor
        return list

# Big for biggest on left, small for smallest on left
def SelectionSort(list, direction):
    for i in range(len(list)):
        minimum = i
        for j in range(i + 1, len(list)):
            if (list[j] < list[minimum] and direction.lower() == 'small'):
                minimum = j
            elif (list[j] > list[minimum] and direction.lower() == 'big'):
                minimum = j
        list[minimum], list[i] = list[i], list[minimum]
    return list

#Get Number func will get a valid number, and will not spit a error upon getting a non-number
def GetNumber(statement):
    while (True):
        try: # while no runtime error
            number = input("\n" + statement + " ") # Gets number
            return number # returns number
            break
        except: # if runtime error prtin invalid num
            print("{0} is not a valid number".format(number))

def map(val, start1, end1, start2, end2):
    # y=mx+b
    m = (float(end2) - float(start2)) / (float(end1) - float(start1)) # slope of equation
    b = float(end2) - float(m) * float(end1) # y intercept of line
    return float(m) * float(val) + float(b) # m = m, val = x, b = b, 'y = m * x + b'

def PythagTheorem(a, b):
    return math.sqrt(math.pow(float(a), 2) + math.pow(float(b), 2))
