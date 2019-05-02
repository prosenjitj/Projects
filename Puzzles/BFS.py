treeMat = [[1,2,4,5],
          [3,5,6,8]]
ROW = 2
COL = 4

class Node :
    def __init__(self, key):
        self.val = key
        self.visited = False
        self.left = None
        self.right = None

def CreateTree(arr):
    return TraverseTree(arr , 0 , 0)

def TraverseTree(arr , row , col):
    node = Node(arr[row][col])

    if row == ROW - 1 and col == COL - 1 :
        return node

    if row < ROW - 1 :
        node.right = TraverseTree(arr , row + 1 , col)

    if col < COL - 1 :
        node.left = TraverseTree(arr , row , col + 1)

    return node


def traverseBFS(root) :
    queue = list()
    queue.append(root)

    while len(queue) > 0:

        node = queue.pop(0)
        node.visited = True
        print(node.val , "-->")
        if node.left and not node.left.visited:
                queue.append(node.left)
        if node.right and not node.right.visited:
                queue.append(node.right)


tree = CreateTree(treeMat)
traverseBFS(tree)
