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
  template, rules = parse_data()

  #print(template)
  #print(rules)
  for x in range(steps):
    print(x)
    temp = template[0]
    for i in range(len(template)-1):
      newChar = ''
      pair = template[i] + template[i+1]
      if pair in rules:
        newChar = rules[pair]
      temp += (newChar + template[i+1])
    template = temp

  print(template)

  commonest = 0
  rarest = 1000

  for letter in char_range('A', 'Z'):
    count = 0
    for char in template:
      if letter == char:
        count += 1

    if count > commonest:
      print("Common: " + letter)
      commonest = count
    if count < rarest and count > 0:
      print("Rare: " + letter)
      rarest = count

  print(commonest)
  print(rarest)

  answer = commonest - rarest

  print(answer)

if __name__ == "__main__":
  main()