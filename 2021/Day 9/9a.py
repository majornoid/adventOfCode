def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('9input.txt', 'r') as inFile:
    rawData = inFile.read().strip().split()
  data = rawData
  return data



def main():
  answer = 0
  data = parse_data()
  lowSpots = 0
  totalRisk = 0
  
  for row, nums in enumerate(data):
    for col, valChar in enumerate(nums):
      val = int(valChar)
      lowest = True
      if row > 0 and int(data[row-1][col]) <= val:
        lowest = False
      elif row < len(data)-1 and int(data[row+1][col]) <= val:
        lowest = False
      elif col > 0 and int(nums[col-1]) <= val:
        lowest = False
      elif col < len(nums)-1 and int(nums[col+1]) <= val:
        lowest = False
      if lowest:
        lowSpots += 1
        totalRisk += (int(val) + 1)
  
  answer = totalRisk
  print(answer)

if __name__ == "__main__":
  main()