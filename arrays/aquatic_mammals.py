# Given comma separated strings, one of water animals and the other of mammals, return a list of animals that appear in both lists

# Sample Input 1
# whale,platypus,starfish,octopus,dolphin
# whale,rhino,kangaroo,platypus,dog
# expected result: [whale,platypus]

def main():
  print("Aquatic Mammals")

  res = []

  s1 = str(input())
  s2 = str(input())

  arr1 = stringToArr(s1)
  arr2 = stringToArr(s2)

  res = findWaterMammals(arr1, arr2)
  print(res)
  return res


def findWaterMammals(arr1, arr2):
  am = []

  for i in arr1:
    for j in arr2:
      if i == j:
        am.append(i)

  return am

def stringToArr(s):
  arr = s.split(",")
  return arr

main()
