rectangle = [1,2,0,2,1,5,0,4,5]

#         |
#     |   |   |
# |   |   |   |   |

def findBiggestRectangle(rec) :

    weightStack = list()
    maxRects = {}
    for indx , val in enumerate(rec) :
        if val == 0 :
            maxRects = calcHeight(weightStack, maxRects , indx)
        else :
            weightStack.append(val)

    maxRects = calcHeight(weightStack, maxRects , len(rec))

    maxVal = 0
    for key , val in maxRects.items() :
        if maxVal < val :
            maxVal = val

    print(maxRects)
    return maxVal

def calcHeight(weightStack , maxRects , indx) :
    recHeight = weightStack.pop()
    count = 1
    while len(weightStack) > 0 :
        val = weightStack.pop()
        if recHeight > val :
            recHeight = val
        count += 1
    maxRects[indx] = recHeight * count
    return maxRects



print(findBiggestRectangle(rectangle))
