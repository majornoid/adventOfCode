def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('16input.txt', 'r') as inFile:
    rawData = inFile.read()
  data = rawData
  return data

def packet_read(start, binary, answer):
  if start >= len(binary)-1:
    return len(binary)
  i = start
  value = 0
  subValues = []
  print("Inner Packet Start: " + str(i))
  version = binary[i:i+3]
  answer[0] += int(version, 2)
  i += 3
  type = binary[i:i+3]
  i += 3
  if type == '100':
    print("literal")
    litString = ''
    while True:
      litString += binary[i+1:i+5]
      i += 5
      if binary[i-5] == '0':
        break
    value = int(litString, 2)
  else:
    print("operator")
    lType = binary[i]
    i += 1
    if lType == '0':
      length = int(binary[i:i+15], 2)
      i += 15
      print("Length: " + str(length))
      count = 0
      while count < length:
        temp, subVal = packet_read(i, binary, answer)
        subValues.append(subVal)
        count += temp
        if count <= length:
          i += temp
        
    else:
      subPackets = int(binary[i:i+11], 2)
      i += 11
      print("Subpackets: " + str(subPackets))
      for _ in range(subPackets):
        temp, subVal = packet_read(i, binary, answer)
        i += temp
        subValues.append(subVal)

    match type:
      case '000':
        for subVal in subValues:
          value += subVal
      case '001':
        value = 1
        for subVal in subValues:
          value *= subVal
      case '010':
        subValues.sort()
        value = subValues.pop(0)
      case '011':
        subValues.sort(reverse=True)
        value = subValues.pop(0)
      case '101':
        if subValues[0] > subValues[1]:
          value = 1
        else:
          value = 0
      case '110':
        if subValues[0] < subValues[1]:
          value = 1
        else:
          value = 0
      case '111':
        if subValues[0] == subValues[1]:
          value = 1
        else:
          value = 0
  return (i - start), value

def main():
  answer = []
  answer.append(0) # answer[0] is version count
  answer.append(0) # answer[1] is literal count
  data = parse_data()
  binary = ''
  #print(data)
  i = 0

  for hex in data:
    match hex:
      case '0':
        binary += '0000'
      case '1':
        binary += '0001'
      case '2':
        binary += '0010'
      case '3':
        binary += '0011'
      case '4':
        binary += '0100'
      case '5':
        binary += '0101'
      case '6':
        binary += '0110'
      case '7':
        binary += '0111'
      case '8':
        binary += '1000'
      case '9':
        binary += '1001'
      case 'A':
        binary += '1010'
      case 'B':
        binary += '1011'
      case 'C':
        binary += '1100'
      case 'D':
        binary += '1101'
      case 'E':
        binary += '1110'
      case 'F':
        binary += '1111'

  #print(binary)

  while i < len(binary):
    #print("Outer Packet Start: " + str(i))
    value = 0
    subValues = []
    version = binary[i:i+3]
    #print(int(version, 2))
    answer[0] += int(version, 2)
    i += 3
    type = binary[i:i+3]
    i += 3
    if type == '100':
      print("literal")
      litString = ''
      while True:
        litString += binary[i+1:i+5]
        i += 5
        if binary[i-5] == '0':
          break
      value = int(litString, 2)
    else:
      print("operator")
      lType = binary[i]
      i += 1
      if lType == '0':
        length = int(binary[i:i+15], 2)
        count = 0
        i += 15
        #print("Length: " + str(length))
        while count < length:
          temp, subVal = packet_read(i, binary, answer)
          i += temp
          subValues.append(subVal)
          count += temp
      else:
        subPackets = int(binary[i:i+11], 2)
        i += 11
        #print("Subpackets: " + str(subPackets))
        for _ in range(subPackets):
          temp, subVal = packet_read(i, binary, answer)
          i += temp
          subValues.append(subVal)

      match type:
        case '000':
          print("sum")
          for subVal in subValues:
            value += subVal
        case '001':
          print("mult")
          value = 1
          for subVal in subValues:
            value *= subVal
        case '010':
          print("min")
          subValues.sort()
          value = subValues.pop(0)
        case '011':
          print("max")
          subValues.sort(reverse=True)
          value = subValues.pop(0)
        case '101':
          print("greater")
          if subValues[0] > subValues[1]:
            value = 1
          else:
            value = 0
        case '110':
          print("less")
          if subValues[0] < subValues[1]:
            value = 1
          else:
            value = 0
        case '111':
          print("equal")
          if subValues[0] == subValues[1]:
            value = 1
          else:
            value = 0

    answer[1] = value

    if i%4 != 0:  
      i += (4 - (i%4))

  print(answer[1])


if __name__ == "__main__":
  main()