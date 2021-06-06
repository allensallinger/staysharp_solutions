from collections import deque

def isBalanced(text):
  s = deque()

  if len(text)%2 == 1:
    return False

  for c in text:
    if c == '(':
      s.append(')')
    elif c == '[':
      s.append(']')
    elif c == '{':
      s.append('}')

    elif len(s) == 0 or s.pop() != c:
      return False

  if len(s) > 0:
    return False

  return True

def main():
  text0 = ""
  text1 = "{}"
  text2 = "({})[]"
  text3 = "{]"

  print("Checking if expersions are balanced:")
  print(f"{text0} : {isBalanced(text0)}")
  print(f"{text1} : {isBalanced(text1)}")
  print(f"{text2} : {isBalanced(text2)}")
  print(f"{text3} : {isBalanced(text3)}")


main()