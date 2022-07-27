def findMax(list):
    if(len(list) > 0):
        max = list[0]
        for element in list:
            if element > max:
                max = element
    return max


def findMin(list):
    if(len(list) > 0):
        min = list[0]
        for element in list:
            if element < min:
                min = element
    return min


L = [1, 7, 2, 4]
print("Max:")
print(findMax(L))
print("Min:")
print(findMin(L))
