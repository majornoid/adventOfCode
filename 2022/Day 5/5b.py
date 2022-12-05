inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
#numbers = [i.split(' ') for i in numbers]
#numbers = [i.replace('-',',').split(',') for i in numbers]

answer = ""

skip = 0


for x in range(len(numbers)):
  if numbers[x][0] != "[":
    nums = numbers[x].split("   ")
    stackCount = int(nums[-1])
    skip = x+2
    break

stacks = [[] for i in range(stackCount)]

for x in range(skip-3, -1, -1):
  line = numbers[x]
  #1, 5, 9, 
  for y in range(stackCount):
    index = y * 4 + 1
    if line[index] != " ":
      stacks[y].append(line[index])

for x in range(skip, len(numbers)):
  line = numbers[x]
  line = line.split(' ')
  count = int(line[1])
  src = int(line[3]) - 1
  dest = int(line[5]) - 1

  for x in range(count, 0, -1):
    i = x * -1
    stacks[dest].append(stacks[src].pop(i))


for stack in stacks:
  answer += str(stack[-1])

print(answer)
