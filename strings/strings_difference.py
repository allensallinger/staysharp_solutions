## Sample input
## abcde
## abcd
## return e

from collections import defaultdict

def main():
  print("Strings Differences")

  s1 = str(input())
  s2 = str(input())

  res = stringAddition(s1, s2)

  print(res)

# Use maps to count the letter occurrences and then return what is non zeroed
def singleMapCounting(s1, s2):
  m = defaultdict(int)

  if len(s1) > len(s2):
    for c in s1:
      m[c] += 1

    for c in s2:
      m[c] -= 1

  else:
    for c in s2:
      m[c] += 1

    for c in s1:
      m[c] -= 1

  for k in m:
    if m[k] != 0:
      return k

  return "same"

## add the ascii values of each character together then subtract the values and convert back to the character
## NOTE: fast but only works for a single character
def stringAddition(s1, s2):
  i1 = 0
  i2 = 0

  for c in s1:
    i1 += int(ord(c))

  for c in s2:
    i2 += int(ord(c))

  c = abs(i1 - i2)

  if c == 0:
    return "same"

  return chr(c)


main()
