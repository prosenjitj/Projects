def ConsecutiveSum(num) :
    consecutives = []
    for i in range(1, num) :
        consecutives.append(i)

    allSums = []
    seek = 0
    while seek < len(consecutives) :
        sum , arr = consecutiveCalc(consecutives , seek, num)
        if sum == num :
            allSums.append(arr)
        seek += 1

    print(allSums)
    return len(allSums)


def consecutiveCalc(consecutives , indx , num) :
    arr = []
    sum = 0
    for i in range(indx , len(consecutives)) :
        sum += consecutives[i]
        arr.append(consecutives[i])
        if sum == num :
            break
        elif sum > num :
            break

    return sum , arr

# print(ConsecutiveSum(3))


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rankIndx = []
    rankedArray = []
    aliceRev = removeDuplicate(list(reversed(alice)))
    scores = removeDuplicate(scores)
    print(scores , aliceRev)
    
    while len(scores) > 0 and len(aliceRev) > 0 :
        if scores[0] < aliceRev[0] :
            rankedArray.append(aliceRev[0])
            aliceRev.remove(aliceRev[0])
            rankIndx.append(len(rankedArray) - 1)
        elif  scores[0] > aliceRev[0] :
            rankedArray.append(scores[0])
            scores.remove(scores[0])
        else :
            rankedArray.append(scores[0])
            aliceRev.remove(aliceRev[0])
            scores.remove(scores[0])
            rankIndx.append(len(rankedArray) - 1)

    while len(scores) > 0 :
        rankedArray.append(scores[0])
        scores.remove(scores[0])

    while len(aliceRev) > 0 :
        rankedArray.append(aliceRev[0])
        aliceRev.remove(aliceRev[0])
        rankIndx.append(len(rankedArray) - 1)

    print(rankedArray)
    return rankIndx


def removeDuplicate (arr) :
    arrNonDup = []
    for val in arr :
        if val not in arrNonDup:
            arrNonDup.append(val)
    return arrNonDup



def climbingLeaderboardScore(scores, alice):
    rank = []
    alice = removeDuplicate(alice)
    scores = removeDuplicate(scores)
    print(scores , alice)
    scrIndx = len(scores) - 1
    for al in alice :
        matched = False
        prevIndx = scrIndx
        print(scrIndx , scores[scrIndx] ,'--', al)
        while scores[scrIndx] <= al and scrIndx > -1:
            print(scrIndx , scores[scrIndx] ,'++++', al)
            prevIndx = scrIndx
            scrIndx -= 1
            matched = True

        print('ScoreIndx :', prevIndx + 1)
        if not matched :
            rank.append(prevIndx + 1 + 1)
        else :
            rank.append(prevIndx + 1)
    return removeDuplicate(rank)


print(climbingLeaderboardScore([100,90,90,80,75,60],[50,65,77,90,102]))
