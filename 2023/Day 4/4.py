inFile = open("input.txt" , 'r')
lines = inFile.read().split("\n")
#numbers = [i.split(' ') for i in numbers]
sum = 0

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
  print(winningNums)
  
  nums = line.split("|")[1]
  print(nums)
  score = 0
  i = 1
  while i < len(nums):
    if nums[i:i+2] in winningNums:
      if score == 0:
        score = 1
      else:
        score *= 2
    i += 3
  sum += score
print(sum)