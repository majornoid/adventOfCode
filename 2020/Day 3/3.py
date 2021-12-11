inFile = open("3input.txt", 'r')
data = inFile.read().split()
solution = 0
slopeRight = 3  # for part 2, just change these slope values
slopeDown = 1
col = slopeRight
row = slopeDown

while row < len(data):
    if col >= len(data[0]):
        col = col - len(data[0])

    if data[row][col] == "#":
        solution += 1

    col += slopeRight
    row += slopeDown

print(solution)