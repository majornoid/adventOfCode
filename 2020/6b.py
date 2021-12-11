from os import closerange


def parse_data():
  with open('6input.txt', 'r') as inFile:
    rawData = inFile.read().split('\n\n')
  data = [i.split() for i in rawData]
  return data



def main():
  answer = 0
  groups = parse_data()

  for group in groups:
    groupYeses = []

    #get full list of possible group yeses
    for person in group:
      for yes in person:
        if yes not in groupYeses:
          groupYeses.append(yes)

    #if one is not found for a person, remove
    for person in group:
      i = 0
      while i < len(groupYeses):
        if groupYeses[i] not in person:
          groupYeses.pop(i)
        else:
          i += 1
                
    answer += len(groupYeses)
  print(answer)


if __name__ == "__main__":
  main()