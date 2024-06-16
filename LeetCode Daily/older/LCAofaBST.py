def findLCA(root, node1, node2):
    if root is None:
            return None
    
    if node1.val < root.val and node2.val < root.val:
        return findLCA(root.left, node1, node2)

    if node1.val > root.val and node2.val > root.val:
        return findLCA(root.right, node1, node2)

    return root