# Implement a queue from a stack
from collections import deque

class QueueFromStack:
  def __init__(self):
    self.s1 = deque()
    self.s2 = deque()

  def enqueue(self, item):
    self.s1.append(item)

  def dequeue(self):
    # check to make sure both stack are not empty
    if not self.s1 and not self.s2:
      print("The queue is empty")
      exit(0)

    # if the second stack is empty, move items from s1 to s2
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())

    return self.s2.pop()

def main():
  qfs = QueueFromStack()
  items = [1,2,3,4,5,6]

  for item in items:
    qfs.enqueue(item)

  print("Dequeueing from queue:")
  print(qfs.dequeue())
  print(qfs.dequeue())
  print(qfs.dequeue())
  print(qfs.dequeue())
  print(qfs.dequeue())

main()

