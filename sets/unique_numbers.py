# Given an comma separated list of numbers find and return the unique ones

# Sample Input 1
# input: 0,1,1,2,3,3,3,4,5
# output: {0,1,2,3,4,5}

# Sample Input 2
# input: 1,1,1,1
# output: {1}

def main():
  print("Unique Numbers")

  string = str(input())
  arr = stringToArr(string)

  # Note: in python doing s(string) of a given comma separated string will return all the unique values but will also include the comma
  s = set()

  for i in arr:
    s.add(i)

  print(s)
  return s


def stringToArr(s):
  arr = s.split(",")
  return arr

main()
