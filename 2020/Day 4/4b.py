import re

inFile = open("4input.txt", 'r')
passports = inFile.read().split('\n\n')
validPassports = []
solution = 0

for x in passports:
  currPass = x.replace(':', ' ').split()
  fieldCount = 0
  totalFields = 0
  for y in range(0, len(currPass)-1):
    currField = currPass[y]
    dataField = currPass[y+1]

    if currField == 'byr':
      totalFields +=1
      if int(dataField) >= 1920 and int(dataField) <= 2002: 
        #print(dataField)
        fieldCount += 1

    if currField == 'iyr':
      totalFields +=1
      if int(dataField) >= 2010 and int(dataField) <= 2020: 
        #print(dataField)
        fieldCount += 1

    if currField == 'eyr':
      totalFields +=1
      if int(dataField) >= 2020 and int(dataField) <= 2030: 
        #print(dataField)
        fieldCount += 1

    if currField == 'hgt':
      totalFields +=1
      regex = re.compile('\D{2}')
      regex2 = re.compile('\d+')
      value = int(regex2.match(dataField)[0])
      if(regex.search(dataField) and regex.search(dataField)[0] == 'cm'):
        if value >= 150 and value <= 193:
          #print(dataField)
          fieldCount += 1
      elif(regex.search(dataField) and regex.search(dataField)[0] == 'in'):
        if value >= 59 and value <= 76:
          #print(dataField)
          fieldCount += 1

    if currField == 'hcl':
      totalFields +=1
      regex = re.compile('#[0-9a-f]{6}')
      if(regex.fullmatch(dataField)):
        #print(dataField)
        fieldCount += 1
      #else:
        #print(dataField)

    if currField == 'ecl':
      totalFields +=1
      if any(x in dataField for x in ['amb','blu','brn','gry','grn','hzl','oth']):
        #print(dataField)
        fieldCount += 1

    if currField == 'pid':
      totalFields +=1
      regex = re.compile('\d{9}')
      if(regex.fullmatch(dataField)):
        #print(dataField)
        fieldCount += 1
      #else:
        #print(dataField)

  if fieldCount >= 7:
    validPassports.append(x)
  elif fieldCount == 6 and totalFields == 7:
    print(x + "\n")

solution = len(validPassports)

print(solution)