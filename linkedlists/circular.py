# Given a list of values to parse into a linked list, see if the linked list is circular or not by tarversing the list.
# A list is circular if the final node is pointed to the head meaning the root node.
# For instance 1->2->3->head would be considered circular while 1->2->3 would not be.

# Input 1
# input: 1->2->3->head
# expected: True

# Input 2
# input: 1->2->3
# expected: False

# Input 3
# input: 1->head
# expected: True


class LinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.head = False


def main():
  values = str(input())

  root = parse_nodes(values)

  printNodes(root)

  circular = is_circular(root)
  print(circular)

def is_circular(root):
  node = root
  runner = root.next

  while(node != None and runner != None):
    if node.data == runner.data:
      return True

    else:
      node = node.next
      if runner.next != None and runner.next.next != None:
        runner = runner.next.next
      else:
        return False

  return False

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
    root.head = True
  else:
    node = root
    while(node.next != None):
      node = node.next
    # In the case of a circular linked list
    if val == "head":
      node.next = root
      return root
    else:
      node.next = temp

  return root


def printNodes(root):
  s = ""
  if root.next == None or root.next.data == root.data:
    s += root.data
  else:
    s += root.data + "->"
    root = root.next

  while(root != None and root.head == False):
    if root.next == None or root.next.head == True:
      s += root.data
    else:
      s += root.data + "->"
    root = root.next

  print(s)

main()