inFile = open("1input.txt", 'r')
numbers = inFile.read().split()
solution = 0

for x in range(0, len(numbers)):
  mass = int(numbers[x])
  solution += int(int(mass/3) - 2)

print(solution)