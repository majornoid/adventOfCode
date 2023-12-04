inFile = open("input.txt" , 'r')
lines = inFile.read().split("\n")
#numbers = [i.split(' ') for i in numbers]

# there are definitely better ways to do this with dynamic programming, 
# but the goal was finding a solution quickly, not finding the best solution
# extra parameters were for a potential dynamic programming solution
def nextCard(card, sum, scores, endScores, pathScore):
  sum[0] += 1
  for i in range(1, scores[card]+1):
    if i < len(scores):
      nextCard(card+i, sum, scores, endScores, pathScore)

sum = [0]
#print(numbers)
scores = []
endScores = {}

for line in lines:
  winningNums = [
    line[10:12],
    line[13:15],
    line[16:18],
    line[19:21],
    line[22:24],
    line[25:27],
    line[28:30],
    line[31:33],
    line[34:36],
    line[37:39],
  ]
  nums = line.split("|")[1]
  score = 0
  i = 1
  while i < len(nums):
    if nums[i:i+2] in winningNums:
      score += 1
    i += 3
  scores.append(score)
for i in range(len(scores)):
  nextCard(i, sum, scores, endScores, 1)

print(sum[0])