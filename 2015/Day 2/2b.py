def parse_data():
  with open('2input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = [i.split('x') for i in rawData]
  return data

def main():
  answer = 0
  data = parse_data()
  for box in data:
    box = [int(i) for i in box]
    box.sort()
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    bow = l*w*h
    ribbon = 2*l + 2*w + bow
    answer += ribbon
  print(answer)

if __name__ == "__main__":
  main()