inFile = open("input.txt" , 'r')
lines = inFile.read().split("\n")
answer = 0

def diffs(sequence):
  print(sequence)
  newSequence = []
  for i in range(len(sequence) - 1):
    newSequence.append(sequence[i+1] - sequence[i])
  end = True
  for x in newSequence:
    if x != 0:
      end = False
  if end:
    return 0
  passUp = newSequence[0] - diffs(newSequence)
  print(passUp)
  return passUp

for line in lines:
  sequence = line.split(" ")
  sequence = [int(i) for i in sequence]
  x = sequence[0] - diffs(sequence)
  print(x)
  answer += x
  
print(answer)