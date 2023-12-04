inFile = open("input.txt" , 'r')
lines = inFile.read().split("\n")
answer = 0
for line in lines:
  first = ""
  last = ""
  for char in line:
    try:
      num = int(char)
      if first == "":
        first = char
      last = char
    except:
      continue
  try:
    value = int(first + last)
  except:
    continue
  answer += value
print(answer)