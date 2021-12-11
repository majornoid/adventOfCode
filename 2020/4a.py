inFile = open("4input.txt", 'r')
passports = inFile.read().split('\n\n')
validPassports = []
solution = 0

for x in passports:
  currPass = x.replace(':', ' ').split()
  fieldCount = 0
  for y in currPass:
    if y == 'byr':
      fieldCount += 1
    if y == 'iyr':
      fieldCount += 1
    if y == 'eyr':
      fieldCount += 1
    if y == 'hgt':
      fieldCount += 1
    if y == 'hcl':
      fieldCount += 1
    if y == 'ecl':
      fieldCount += 1
    if y == 'pid':
      fieldCount += 1
  if fieldCount >= 7:
    validPassports.append(x)

solution = len(validPassports)

print(solution)