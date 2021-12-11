# started making better use of functions today, aiming for cleaner code
from os import curdir


def parse_data():
  with open('7input.txt', 'r') as inFile:
    rawData = inFile.read().split(',')
  data = [int(i) for i in rawData]
  return data



def main():
  answer = 0
  data = parse_data()
  minfuel = 99999999
  for i in data:
    currfuel = 0
    for j in data:
      currfuel += abs(i-j)
    if currfuel < minfuel:
      minfuel = currfuel

      
  
  print(minfuel)


if __name__ == "__main__":
  main()