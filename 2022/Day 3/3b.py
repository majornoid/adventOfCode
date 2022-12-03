inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
#numbers = [i.split(' ') for i in numbers]
answer = 0
#print(numbers)

for x in range(0, len(numbers), 3):
  shared = ' '
  priority = 0
  r1 = numbers[x]
  r2 = numbers[x+1]
  r3 = numbers[x+2]
  for i in r1:
    if i in r2 and i in r3:
      shared = i
      break
  #print(shared)
  if ord(shared[0]) > 95:
    priority = ord(shared[0])  - 96
  else:
    priority = ord(shared[0])  - (65-27)
  #print(priority)
  answer += priority

print(answer)