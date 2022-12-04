inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
numbers = [i.replace('-',',').split(',') for i in numbers]
answer = 0
#print(numbers)

for x in numbers:
  if int(x[0]) <= int(x[2]) and int(x[1]) >= int(x[3]):
    answer += 1
    print(x, answer)
  elif int(x[0]) >= int(x[2]) and int(x[1]) <= int(x[3]):
    answer += 1
    print(x, answer)

print(answer)