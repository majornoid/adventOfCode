def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('14input.txt', 'r') as inFile:
    rawData = inFile.read().split('\n\n')
  template = rawData[0]
  rulesList = rawData[1].split('\n')

  rulesList = [i.split(' -> ') for i in rulesList]
  rules = {}
  for rule in rulesList:
    rules[rule[0]] = rule[1]
  
  return template, rules

def main():
  answer = 0
  steps = 40
  pairs = {} # keeps a count of pairs
  rules = {} # determines which two pairs each pair becomes
  template, conversions = parse_data()

  for rule in conversions:
    rules[rule] = [(rule[0] + conversions[rule]), (conversions[rule] + rule[1])]
    pairs[rule] = 0

  print(rules)

  for i in range(len(template)-1):
    pair = template[i] + template[i+1]
    if pair in pairs:
      pairs[pair] += 1
    else:
      pairs[pair] = 1


  #print(template)
  #print(rules)
  for x in range(steps):
    print(x)
    print(pairs)
    temp = pairs.copy()
    for pair in pairs:
      if pair in rules:
        temp[pair] -= pairs[pair]
        newPairs = rules[pair]
        temp[newPairs[0]] += pairs[pair]
        temp[newPairs[1]] += pairs[pair]
    pairs = temp

  print(pairs)

  commonest = 0
  rarest = 100000000000000000000000000000000000

  for letter in char_range('A', 'Z'):
    print(letter)
    count = 0
    for pair in pairs:
      if letter in pair:
        if pair[0] != pair[1]:
          count += pairs[pair]
        else:
          count += 2*pairs[pair]
    count = int((count/2)+0.5)
    if count+1 > commonest:
      print("Common: " + letter)
      commonest = count
    if count < rarest and count > 1:
      print("Rare: " + letter)
      rarest = count

  answer = commonest - rarest

  print(commonest)
  print(rarest)

  print(answer)

if __name__ == "__main__":
  main()