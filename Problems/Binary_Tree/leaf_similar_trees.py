"""
Consider all the leaves of a binary tree, from left to right order,
the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
"""


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_leaves(root, leaves):
    if root:
        if not root.left and not root.right:
            leaves.append(root.val)
        else:
            find_leaves(root.left, leaves)
            find_leaves(root.right, leaves)
    return leaves


def leaf_similar(root1, root2) -> bool:

    root1_leaves = find_leaves(root1, [])
    root2_leaves = find_leaves(root2, [])

    if len(root1_leaves) != len(root2_leaves):
        return False

    for i, j in zip(root1_leaves, root2_leaves):
        if i != j:
            return False
    return True


def leaf_similar_tree(root1, root2):
    def get_leaves(root, leaves):
        if root:
            if not root.left and not root.right:
                leaves.append(root.val)
            else:
                get_leaves(root.left, leaves)
                get_leaves(root.right, leaves)

    leaves1, leaves2 = [], []
    get_leaves(root1, leaves1)
    get_leaves(root2, leaves2)
    return leaves1 == leaves2


def main():
    pass


if __name__ == '__main__':
    main()
