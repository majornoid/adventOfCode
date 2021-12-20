def parse_data():
  with open('20input.txt', 'r') as inFile:
    rawData = inFile.read().split('\n\n')
  key = rawData[0]
  img = rawData[1]
  image = img.split()
  return key, image

def bit_get(image, row, col, voidBit):
  if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]):
    if image[row][col] == '#':
      bit = '1'
    else:
      bit = '0'
  else:
    bit = voidBit
  return bit

def enhance(key, image, iteration):
  output = []
  if iteration % 2 == 1 and key[0] == '#':
    voidBit = '1'
  else:
    voidBit = '0'
  for row in range(-1, len(image)+1):
    outputRow = ''
    for col in range(-1, len(image[0])+1):
      binary = ''

      binary += bit_get(image, row-1, col-1, voidBit)
      binary += bit_get(image, row-1, col, voidBit)
      binary += bit_get(image, row-1, col+1, voidBit)
      binary += bit_get(image, row, col-1, voidBit)
      binary += bit_get(image, row, col, voidBit)
      binary += bit_get(image, row, col+1, voidBit)
      binary += bit_get(image, row+1, col-1, voidBit)
      binary += bit_get(image, row+1, col, voidBit)
      binary += bit_get(image, row+1, col+1, voidBit)
      #print(binary)

      keyIndex = int(binary, 2)
      #print(keyIndex)
      #print(key[keyIndex])
      outputRow += key[keyIndex]
    #print(outputRow)
    output.append(outputRow)
  return output

def main():
  answer = 0
  key, image = parse_data()
  steps = 50 #set number of enhancements

  for row in image:
    break
    print(row) #allow for visualization
  #print()

  for i in range(steps): 
    image = enhance(key, image, i)
    for row in image:
      break
      print(row)
    #print()

  for row in image:
    for pixel in row:
      if pixel == "#":
        answer += 1

  print(answer)


if __name__ == "__main__":
  main()