from collections import deque

class BinarySearchTreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.value = val


def createBSTFromSortedList(arr: list) -> BinarySearchTreeNode:
  if len(arr) == 0:
    return None

  mid = len(arr) // 2

  root = BinarySearchTreeNode(arr[mid])

  # set the left as the middle node - 1 index
  root.left = createBSTFromSortedList(arr[:mid])

  # set the right as the middle node + 1 index
  root.right = createBSTFromSortedList(arr[mid+1:])

  return root

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

arr = [1,2,3,4,5,6,7,8,9]

bst = createBSTFromSortedList(arr)
printLevelOrderTraversal(bst)

print(bst.value)
print(bst.left.value)
print(bst.right.value)