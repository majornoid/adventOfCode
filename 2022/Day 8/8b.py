inFile = open("input.txt" , 'r')
rows = inFile.read().split("\n")
#rows = [i.split(' ') for i in rows]
#rows = [i.replace('-',',').split(',') for i in rows]
answer = 0


for row in range(len(rows)):
  for col in range(len(rows[0])):
    val = int(rows[row][col])

    up = 0
    down = 0
    left = 0
    right = 0

    if row == 0 or row == len(rows)-1 or col == 0 or col == len(rows[0])-1:
      continue

    for searchRow in range(row+1, len(rows)):
      down += 1
      if int(rows[searchRow][col]) >= val:
        break

    for searchRow in range(row-1, -1, -1):
      up += 1
      if int(rows[searchRow][col]) >= val:
        break

    for searchCol in range(col+1, len(rows[0])):
      right += 1
      if int(rows[row][searchCol]) >= val:
        break

    for searchCol in range(col-1, -1, -1):
      left += 1
      if int(rows[row][searchCol]) >= val:
        break

    if up * down * left * right > answer:
      answer = up * down * left * right
      

print(answer)