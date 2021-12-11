def parse_data():
  with open('5input.txt', 'r') as inFile:
    rawData = inFile.read().split('\n')
  data = rawData
  return data



def main():
  answer = 0
  data = parse_data()
  seatIDList = []

  for seat in data:
    row = [item for item in range(128)]
    col = [item for item in range(8)]
    for x in seat:
      #print(x)
      #print(row)
      #print(col)
      if x == 'B':
        row = row[int(len(row)//2):]
      elif x == 'F':
        row = row[:int(len(row)/2)]
      elif x == 'R':
        col = col[int(len(col)//2):]    
      elif x == 'L':
        col = col[:int(len(col)/2)]
    #print(row)
    #print(col)
    seatID = row[0] * 8 + col[0]
    seatIDList.append(seatID)

  seatIDList.sort()
  for i in range(8, len(seatIDList)):
    if seatIDList[i]+1 != seatIDList[i+1]:
      answer = seatIDList[i] + 1
      break
  print(answer)


if __name__ == "__main__":
  main()