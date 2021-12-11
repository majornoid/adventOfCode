inFile = open("1input.txt", 'r')
numbers = inFile.read().split()
solution = -1

for x in range(0, len(numbers)):
    if solution != -1:
        break
    for y in range(x + 1, len(numbers)):
      if solution != -1:
        break  
      for z in range(y + 1, len(numbers)):
        if int(numbers[x]) + int(numbers[y]) + int(numbers[z]) == 2020:
            solution = int(numbers[x]) * int(numbers[y]) * int(numbers[z])
            break

print(solution)