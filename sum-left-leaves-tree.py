# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Write your solution in below function
def sumOfLeftLeaves(root: TreeNode):
    print('root', root)
    """
    :type root: TreeNode - Node representing the root of the tree
    :rtype: int: sum of left leaves
    """
    
    def travel_tree(node, side):
        summ = node.val if side == 'left' else 0
        left = 0
        right = 0
        if node.left is not None:
            left = travel_tree(node.left, 'left')
        if node.right is not None:
            right = travel_tree(node.right, 'right')
        return summ + left + right

    result = travel_tree(root, 'root')
    
    return result

# Don't change anything below this line
def createTree(arr):
    if arr is None or len(arr) == 0 or not arr[0].isnumeric():
        return None

    treeNodeQueue = []
    integerQueue = []

    for a in arr:
        integerQueue.append(a)

    treeNode = TreeNode(int(integerQueue.pop(0)))
    treeNodeQueue.append(treeNode)

    while integerQueue != []:
        leftVal = None if (integerQueue == []) else integerQueue.pop(0)
        rightVal = None if (integerQueue == []) else integerQueue.pop(0)
        current = treeNodeQueue.pop(0)

        if leftVal and leftVal.isnumeric():
            left = TreeNode(int(leftVal))
            current.left = left
            treeNodeQueue.append(left)

        if rightVal and rightVal.isnumeric():
            right = TreeNode(int(rightVal))
            current.right = right
            treeNodeQueue.append(right)

    return treeNode


if __name__ == "__main__":
    line = input()
    components = line.strip().split(",")
    root = createTree(components)
    print(sumOfLeftLeaves(root))
