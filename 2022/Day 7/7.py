from itertools import accumulate
inFile = open("input.txt" , 'r')
rows = inFile.read().split("\n")
rows = [i.split(' ') for i in rows]
#rows = [i.replace('-',',').split(',') for i in rows]
answer = 0
answer2 = 70000000
#print(rows)
directories = {'/':0}
path = []
total = 0

for line in rows:
  if line[0] == '$':
    if line[1] == "cd":
      print(line)
      if line[2] == '/':
        path = ['/']
      elif line[2] == '..':
        path.pop()
      else:
        path.append(line[2])
        if ''.join(path) not in directories:
          directories[''.join(path)] = 0
      print(path)
  elif line[0] == "dir":
    pass
  else:
    total += int(line[0])
    for directory in accumulate(path):
      directories[directory] += int(line[0])

for directory in directories:
  if directories[directory] <= 100000:
    answer += int(directories[directory])

print(answer)

for directory in directories:
  if directories[directory] > directories['/'] - 40000000 and answer2 > directories[directory]:
    answer2 = directories[directory]

print(answer2)