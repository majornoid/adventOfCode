from os import closerange


def parse_data():
  with open('7input.txt', 'r') as inFile:
    rawData = inFile.read().split('\n')
  rules = [i.split(' bags contain ') for i in rawData]
  data = {}

  for i in range(len(rules)-1):
    ruleStrings = rules[i][1].replace(' bag, ','$').replace(' bags, ','$').replace(' bag.','').replace(' bags.','').split('$')
    containers = {}
    for x in ruleStrings:
      if x[0] != 'n':
        containers[x[2:]] = int(x[0])
    data[rules[i][0]] = containers

  return data



def main():
  answer = 0
  data = parse_data()
  print(data)

  bagsContaining = ['shiny gold']

  bagFound = True
  while bagFound:
    bagFound = False

    for bagType in data:
      i = 0
      while i < len(bagsContaining):
        if ( bagsContaining[i] in data[bagType] ) and ( bagType not in bagsContaining ):
          bagsContaining.append(bagType)
          bagFound = True
        i += 1

  answer = len(bagsContaining) - 1

  print(answer)

if __name__ == "__main__":
  main()