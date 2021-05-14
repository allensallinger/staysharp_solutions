# Given a list of characters and a list of words, see if each word can be generated for the given characters

# Sample Input 1
# input: abcdefghijklmnopqrstuvwxyz
# input: dog,cat,alpaca
# output: {'dog': True, 'cat': True, 'alpaca': False}

# Sample Input 2
# input: aaplcad
# input: dog,alpaca,cat
# output: {'dog': False, 'alpaca': True, 'cat': False}

from collections import defaultdict

def main():
  s1 = str(input())
  s2 = str(input())

  availableLetters = countCharacters(s1)
  words = stringToArr(s2)

  wordPossible = dict()

  for word in words:
    wordLetters = countCharacters(word)
    wordPossible[word] = True
    for letter in wordLetters:
      if wordLetters[letter] > availableLetters[letter]:
        wordPossible[word] = False

  print(wordPossible)
  return wordPossible

def stringToArr(s):
  arr = s.split(",")
  return arr

def countCharacters(string):
  m = defaultdict(int)
  for c in string:
    m[c] += 1

  return m

main()
