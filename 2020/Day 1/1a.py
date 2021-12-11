inFile = open("1input.txt", 'r')
numbers = inFile.read().split()
#print(numbers)
solution = -1

for x in range(len(numbers)):
    if solution != -1:
        break
    for y in range(x + 1, len(numbers)):
        if int(numbers[x]) + int(numbers[y]) == 2020:
            solution = int(numbers[x]) * int(numbers[y])
            break

print(solution)