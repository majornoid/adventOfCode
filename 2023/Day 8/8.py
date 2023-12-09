inFile = open("input.txt" , 'r')
parts = inFile.read().split("\n\n")
sequence = parts[0]
translations = parts[1].split("\n")
paths = {}
for x in translations:
  paths[x[:3]] = (x[7:10], x[12:15])
  
current = "AAA"
steps = 0
while current != "ZZZ":
  for char in sequence:
    if char == "L":
      current = paths[current][0]
    elif char == "R":
      current = paths[current][1]
    steps += 1
    if current == "ZZZ":
      break
      

print(steps)