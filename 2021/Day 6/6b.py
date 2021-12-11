from os import curdir
import sys
sys.setrecursionlimit(1000000000)

answer = 0
dayCount = 256
debugCounter = 500
newFishList = []
newFish64 = []
fishPer64 = []

# I acknowledge that this was far from clean code,
# but it is fast, I'm sure I could make a much better solution,
# one that works for thinks beyond multiples of 64 and quick,
# but I'm really tired right now and was just trying to write a
# solution quick

fishCount  = [0]*9
fishCount2 = [0]*9
fishCount3 = [0]*9
fishCount4 = [0]*9
fishCount5 = [0]*9

inFile = open("6input.txt" , 'r')
fish = inFile.read().split(",")
fish = [int(i) for i in fish]

# establishes what each possible number while become after 64 days
# prevents countless recalculations
testFish = [0,1,2,3,4,5,6,7,8]
for i in range(len(testFish)):
  currFish = []
  currFish.append(testFish[i])
  for x in range(64): #days
    print(x)
    newFish = 0
    for y in range(0, len(currFish)):
      if currFish[y] == 0:
        currFish[y] = 6
        newFish += 1
      else:
        currFish[y] -= 1

    for z in range(newFish):
      currFish.append(8)
  newFish64.append(currFish)
  newFishList.append(len(currFish))


# figures out how many fish at each stage are produced after
# 64 days from 1 fish starting at each stage
print(newFishList)
for fishNum in newFish64:
  count = [0]*9
  for y in fishNum:
    count[y] += 1
  fishPer64.append(count)



for y in fish:
  fishCount[y] += 1
print(fishCount)


#this part could obviously be improved with loops
for f in range(9):
  for t in range(9):
    fishCount2[t] += fishCount[f] * fishPer64[f][t]
print(fishCount2)

for f in range(9):
  for t in range(9):
    fishCount3[t] += fishCount2[f] * fishPer64[f][t]
print(fishCount3)

for f in range(9):
  for t in range(9):
    fishCount4[t] += fishCount3[f] * fishPer64[f][t]
print(fishCount4)

for f in range(9):
  for t in range(9):
    fishCount5[t] += fishCount4[f] * fishPer64[f][t]
print(fishCount5)

# at this point in polished version, calculation could be done like above 
# but for the remainder of days, which would be under 64

# those would then be use for a final multiplication of fishCountX

# that said, I probably won't revisit this problem soon, though I may

for x in fishCount5:
  answer += x

print(answer)