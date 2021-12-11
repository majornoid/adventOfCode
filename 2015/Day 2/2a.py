def parse_data():
  with open('2input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = [i.split('x') for i in rawData]
  return data

def main():
  answer = 0
  data = parse_data()
  for box in data:
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    print(box)
    paper = 2*l*w + 2*w*h + 2*h*l
    sides = []
    sides.append(l*w)
    sides.append(w*h)
    sides.append(h*l)
    sides.sort()
    slack = sides[0]
    paper += slack
    answer += paper
  print(answer)

if __name__ == "__main__":
  main()