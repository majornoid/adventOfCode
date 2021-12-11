# started making better use of functions today, aiming for cleaner code
from os import curdir


def parse_data():
  with open('7input.txt', 'r') as inFile:
    rawData = inFile.read().split(',')
  data = fish = [int(i) for i in rawData]
  return data



def main():
  answer = 0
  data = parse_data()
  minfuel = 99999999
  for i in data:
    currfuel = 0
    for j in data:
      for k in range(abs(i-j)):
        currfuel += (k+1)
    if currfuel < minfuel:
      minfuel = currfuel

      
  
  print(minfuel)


if __name__ == "__main__":
  main()