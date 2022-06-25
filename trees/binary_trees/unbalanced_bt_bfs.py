from collections import deque

from unbalanced_binary_tree import BinaryTreeNode, CreateTree

def printLevelOrderTraversal(root):
  if root is None:
    return

  s = deque()
  s.append(root)

  while len(s) > 0:
    node = s.popleft()
    print(node.value, end=" ")

    if node.left is not None:
      s.append(node.left)

    if node.right is not None:
      s.append(node.right)


bt_root = CreateTree()

print("\nPrinting LevelOrder(BFS) using a queue")
printLevelOrderTraversal(bt_root)
