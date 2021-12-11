from os import closerange


def parse_data():
  with open('6input.txt', 'r') as inFile:
    rawData = inFile.read().split('\n\n')
  data = rawData
  return data



def main():
  answer = 0
  groups = parse_data()

  for group in groups:
    groupYeses = []
    for yes in group:
      if yes not in groupYeses and yes != '\n':
        groupYeses.append(yes)
    answer += len(groupYeses)
  print(answer)


if __name__ == "__main__":
  main()