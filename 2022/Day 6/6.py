inFile = open("input.txt" , 'r')
input = inFile.read()
#numbers = [i.split(' ') for i in numbers]
#numbers = [i.replace('-',',').split(',') for i in numbers]
PATTERN_LENGTH = 14
answer = 0
buff = []
for i in range(len(input)):
  letter = input[i]
  if len(buff) < PATTERN_LENGTH:
    buff.append(letter)
  else:
    buff.pop(0)
    buff.append(letter)
    if len(set(buff)) == PATTERN_LENGTH:
      print(buff)
      answer = i + 1
      break


print(answer)