inFile = open("1input.txt" , 'r')
numbers = inFile.read().split()
count = 0

for x in range(1, len(numbers)-2):
  if int(numbers[x]) + int(numbers[x+1]) + int(numbers[x+2]) > int(numbers[x-1]) + int(numbers[x]) + int(numbers[x+1]):
    count += 1

print(count)