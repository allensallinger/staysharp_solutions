from collections import deque

def main():
  q = deque()

  q.append("a")
  q.append("b")
  q.append("c")

  print(q)

  print("Popping value: " + q.popleft())
  print(q)

  print("Popping value: " + q.popleft())
  print(q)

  print("This is the length of the queue: " + str(len(q)))

main()