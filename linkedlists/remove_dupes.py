# Given a string separated by -> that represents the values in a linkedList, create the linked list and remove duplicated values. Assume that the list of data is sorted

# Input 1
# 1->2->2->3->4
# return 1->2->3->4

# Input 2
# 0->1->1->1
# 0->1

# Input 3
# 1
# 1

class LinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

def main():
  values = str(input())

  root = parse_nodes(values)

  printNodes(root)

  root = remove_dupes(root)
  printNodes(root)


def remove_dupes(root):
  node = root
  while(node.next != None):
    if node.data == node.next.data:
      if node.next.next == None:
        node.next = None
      else:
        node.next = node.next.next
    node = node.next

  return root


def parse_nodes(s):
  vals = s.split("->")

  root = None

  for v in vals:
    root = insert(root, v)

  return root

def insert(root, val):
  temp = LinkedListNode(val)

  if root == None:
    root = temp
  else:
    node = root
    while(node.next != None):
      node = node.next
    node.next = temp

  return root

def printNodes(root):
  s = ""
  while(root != None):
    if root.next == None:
      s += root.data
    else:
      s += root.data + "->"
    root = root.next

  print(s)

main()


