def splitter(word):
    return [char for char in word]

answer = 0
days = 256
debugCounter = 500

inFile = open("6input.txt" , 'r')
fish = inFile.read().split(",")
fish = [int(i) for i in fish]
print(fish)

for x in range(days):
  print(x)
  newFish = 0

  for y in range(0, len(fish)):
    if fish[y] == 0:
      fish[y] = 6
      newFish += 1
    else:
      fish[y] -= 1

  for z in range(newFish):
    fish.append(8)


answer = len(fish)


print(answer)