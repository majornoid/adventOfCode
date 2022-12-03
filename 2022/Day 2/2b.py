inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
numbers = [i.split(' ') for i in numbers]
answer = 0
print(numbers)

score = 0

for x in numbers:
  p1 = ""
  p2 = ""

  if x[0] == "A":
    p1 = "r"
  elif x[0] == "B":
    p1 = "p"
  elif x[0] == "C":
    p1 = "s"

  if x[1] == "X":
    if p1 == "r":
      p2 = "s"
    elif p1 == "p":
      p2 = "r"
    elif p1 == "s":
      p2 = "p"
  elif x[1] == "Y":
    if p1 == "r":
      p2 = "r"
    elif p1 == "p":
      p2 = "p"
    elif p1 == "s":
      p2 = "s"
  elif x[1] == "Z":
    if p1 == "r":
      p2 = "p"
    elif p1 == "p":
      p2 = "s"
    elif p1 == "s":
      p2 = "r"

  if p2 == "r":
    score += 1
  elif p2 == "p":
    score += 2
  elif p2 == "s":
    score += 3

  if p1 == p2:
    score += 3
  elif p1 == "r" and p2 == "p" or p1 == "p" and p2 == "s" or p1 == "s" and p2 == "r":
    score += 6

print(score)