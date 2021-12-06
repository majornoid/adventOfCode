answer = 0
days = 256
fishCount  = [0]*9

inFile = open("6input.txt" , 'r')
fish = inFile.read().split(",")
fish = [int(i) for i in fish]

for y in fish: #get initial counts of each type of fish
  fishCount[y] += 1

for x in range(days): #adjusts counts per day
  rebornFish = 0
  newFish = 0
  for f in range(9):
    if f == 0:
      rebornFish = fishCount[0]
      newFish = fishCount[0]
    else:
      fishCount[f-1] = fishCount[f]
  fishCount[6] += rebornFish
  fishCount[8] = newFish

for x in fishCount:
  answer += x

print(answer)