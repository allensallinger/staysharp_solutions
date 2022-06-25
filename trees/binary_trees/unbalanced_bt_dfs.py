from collections import deque

from unbalanced_binary_tree import BinaryTreeNode, CreateTree

## DFS Searches of trees
# InOrder left, root, right
def printInOrder(root: BinaryTreeNode):
  if root:
    printInOrder(root.left)

    print(root.value)

    printInOrder(root.right)


# root, left, right
def printPreOrder(root: BinaryTreeNode):
  if root:
    print(root.value)

    printPreOrder(root.left)

    printPreOrder(root.right)

# left, right, root
def printPostOrder(root: BinaryTreeNode):
  if root:
    printPostOrder(root.left)

    printPostOrder(root.right)

    print(root.value)

def printDFSUsingStack(root: BinaryTreeNode):
  current = root
  s = deque()

  while True:
    if current is not None:
      s.append(current)
      current = current.left

    elif(s):
      current = s.pop()

      print(current.value, end=" ")

      current = current.right

    else:
      break

bt_root = CreateTree()

print("Printing tree InOrder Traversal")
printInOrder(bt_root)

print("Printing tree PreOrder Traversal")
printPreOrder(bt_root)

print("Printing tree PostOrder Traversal")
printPostOrder(bt_root)

print("Printing InOrder using a stack")
printDFSUsingStack(bt_root)