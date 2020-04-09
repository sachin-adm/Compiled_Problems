def timeTake(word):
  global typedWord
  L = ['d', 'f']
  R = ['j', 'k']
  previousGroup = L if word[0] in L else R
  total = 2
  if len(word) > 1:
    for letter in word[1:]:
      if letter in previousGroup:
        total += 4
      else:
        total += 2
        previousGroup = L if letter in L else R

  if word in typedWord:
    return total/2
  else:
    typedWord.add(word)
    return total

T = int(input())
for _ in range(T):
  typedWord = set()
  N = int(input())
  total = sum(timeTake(input()) for x in range(N))
  print(int(total))