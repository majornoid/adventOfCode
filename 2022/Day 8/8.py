inFile = open("input.txt" , 'r')
rows = inFile.read().split("\n")
#rows = [i.split(' ') for i in rows]
#rows = [i.replace('-',',').split(',') for i in rows]
answer = 0


for row in range(len(rows)):
  for col in range(len(rows[0])):
    val = int(rows[row][col])
    
    if row == 0 or row == len(rows)-1 or col == 0 or col == len(rows[0])-1:
      answer+=1
      continue

    done = True 
    for searchRow in range(row+1, len(rows)):
      if int(rows[searchRow][col]) >= val:
        done = False
        break
    if done:
      answer += 1
      continue

    done = True
    for searchRow in range(row-1, -1, -1):
      if int(rows[searchRow][col]) >= val:
        done = False
        break
    if done:
      answer += 1
      continue

    done = True
    for searchCol in range(col+1, len(rows[0])):
      if int(rows[row][searchCol]) >= val:
        done = False
        break
    if done:
      answer += 1
      continue

    done = True
    for searchCol in range(col-1, -1, -1):
      if int(rows[row][searchCol]) >= val:
        done = False
        break
    if done:
      answer += 1
      continue
      

print(answer)