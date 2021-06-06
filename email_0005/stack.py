# Starting with stacks
from collections import deque

def main():
  print("Stack Example")
  s = deque()

  s.append("a")
  s.append("b")

  print(s)

  print(s.pop())
  print(s)

  s.append("c")
  print(s)
  print("Length of stack: " + str(len(s)))

main()
