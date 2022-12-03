inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
#numbers = [i.split(' ') for i in numbers]
answer = 0
print(numbers)

for x in numbers:
  half = int(len(x)/2)
  c1 = x[:half]
  c2 = x[half:]
  print(c1, c2)
  shared = ' '
  priority = 0
  for i in range(len(c1)):
    if c1[i] in c2:
      shared = c1[i]
      break
  print(shared)
  if ord(shared[0]) > 95:
    priority = ord(shared[0])  - 96
  else:
    priority = ord(shared[0])  - (65-27)
  print(priority)
  answer += priority

print(answer)