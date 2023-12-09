inFile = open("input.txt" , 'r')
parts = inFile.read().split("\n\n")
sequence = parts[0]
translations = parts[1].split("\n")
paths = {}
currents = []


def get_factors(n):
  factors = []
  for i in range(1, n + 1):
    if n % i == 0:
      factors.append(i)
  return factors

def lowest_common_multiple(numbers):
  allFactors = set()
  for number in numbers:
    factors = get_factors(number)
    if len(factors) == 4:
      factors = factors[1:-1]
    allFactors.update(factors)
  lcm = 1
  for factor in allFactors:
    lcm *= factor
  return lcm

for x in translations:
  paths[x[:3]] = (x[7:10], x[12:15])
  if x[2] == "A":
    currents.append(x[:3])
  
totals = []
steps = 0
end = False
answer = 1
distances = []
while not end and len(currents) > 0:
  for char in sequence:
    if char == "L":
      for i in range(len(currents)):
        currents[i] = paths[currents[i]][0]
    elif char == "R":
      for i in range(len(currents)):
        currents[i] = paths[currents[i]][1]
    steps += 1
    for current in currents:
      if current[2] == "Z":
        currents.remove(current)
        distances.append(steps)
        answer *= steps
    if end:
      break
    
answer = lowest_common_multiple(distances)
print(f"Answer: {answer}")


      