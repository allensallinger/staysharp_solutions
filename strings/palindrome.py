## Sample Input

## Case 1
## input: abc
## output: False

## Case 2
## input: tacocat
## ouput: True

def main():
  print("Palindromes")

  s1 = str(input())

  ans = isPalindrome(s1)

  print(ans)


def isPalindrome(s1):
  if len(s1) == 0:
    return True

  if len(s1) == 1:
    return True

  for i in range(int(len(s1)/2)):
    if s1[i] != s1[-i+1]:
      return False

  return True

main()