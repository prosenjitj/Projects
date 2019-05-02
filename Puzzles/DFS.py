    #      12
    #     /  \
    #   10    14
    #   /\     \
    # 4   11    2
# LVR

class Node :
    def __init__(self, key):
        self.val = key
        self.visited = False
        self.left = None
        self.right = None

    def add(self, leftNode, rightNode):
        self.left = leftNode
        self.right = rightNode
        return self

def createNode () :
    root = Node(12)
    root.add(Node(10).add(Node(4) , Node(11)) ,
             Node(14).add(None, Node(20)))

    return root

def traverseBalanceTree(root) :
    arr = list()
    if root :
        if root.left :
            arr.extend(traverseBalanceTree(root.left))

        arr.append(root.val)

        if root.right :
            arr.extend(traverseBalanceTree(root.right))



    return arr

def validateBalanceArray(arr) :
    max = 0
    for i in arr :
        if i < max :
            return False
        max = i
    return True

validationArr = traverseBalanceTree(createNode())
print(validationArr)
print("Is It Balanced :" , validateBalanceArray(validationArr))
