inFile = open("1input.txt" , 'r')
numbers = inFile.read().split("\n")
max = 0
count = 0
counts = []
#print(numbers)
for x in range(len(numbers)):
  if numbers[x] == "":
    counts.append(count)
    count = 0
  else:
    count += int(numbers[x])
    if count > max:
      max = count

counts.sort()

print(counts[-1] + counts[-2] + counts[-3])
print(max)