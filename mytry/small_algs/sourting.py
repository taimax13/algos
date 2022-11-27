def selectionSort(array):
    currInd = 0
    while currInd < len(array) - 1:
        minInd = currInd
        for i in range(currInd + 1, len(array)):
            if array[minInd] > array[i]:
                minInd = i

        swap(currInd, minInd, array)
        currInd += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


###################################################################3
##bucket sourt
def threeNumberSort(array, order):
    firstIdn = 0
    for v in array:
        if v == order[0]:
            firstIdn += 1
    lastInd = len(array)-1
    for v in array:
        if v==order[len(array)-1]:
            lastInd-=1
        pass
    return array

#####################################################
def threeNumberSort2(array, order):
    first = order[0]
    second = order[1]
    firstind, secondind, thirdind = 0,0, len(array)-1
    while secondind <= thirdind:
        value = array[secondind]

        if value == first:
            array[secondind], array[firstind]=array[firstind], array[secondind]
            firstind += 1
            secondind += 1
        elif value == second:
            secondind += 1
        else:
            array[secondind], array[thirdind] = array[thirdind], array[secondind]
            thirdind -= 1
    return array