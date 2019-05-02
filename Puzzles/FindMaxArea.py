A = [[0, 0, 1, 1],
     [1, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]

def findRegions(mat) :
    w = len(mat[0])
    h = len(mat)
    visited = []
    for i in range(h):
        visited.append([0] * w)

    rgn = []
    for row in range(h) :
        lower = 0
        while lower < w :
            if mat[row][lower] == 1 and visited[row][lower] == 0:
                visited , count = traverseMat(mat , visited, row , lower, 0)
                rgn.append(count)
            lower += 1

    max = rgn[0]
    for val in rgn :
        if max < val : max = val
    return max

def traverseMat(mat , visited, row , lower , count) :
    if row > len(mat) - 1 or row < 0 or lower < 0 or lower > len(mat[0]) - 1 \
                or mat[row][lower] != 1  or visited[row][lower] == 1:
        return visited , count

    visited[row][lower] = 1
    count += 1
    for indxI in range (-1 , 2) :
        for indxJ in range (-1 , 2) :
            if not (indxI == 0 and indxJ == 0):
                visited , count = traverseMat(mat , visited, row + indxI , lower + indxJ, count)

    return visited , count


print(findRegions(A))
