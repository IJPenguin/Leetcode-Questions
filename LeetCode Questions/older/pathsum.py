class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(curr, path, summ, targetSum, res):
    if curr is None:
        return

    summ += curr.val
    path.append(curr.val)

    if not curr.left and not curr.right and summ == targetSum:
        res.append(path[:])

    path_sum(curr.left, path, summ, targetSum, res)
    path_sum(curr.right, path, summ, targetSum, res)

    path.pop()


targetSum = 22
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

res = []
path_sum(root, [], 0, targetSum, res)
print(res)
