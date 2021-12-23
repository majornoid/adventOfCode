def parse_data():
  with open('22input.txt', 'r') as inFile:
    rawData = inFile.read().replace('x=','').replace('y=','').replace('z=','').replace('..',',').split('\n')
  data = [i.split() for i in rawData]
  commands = []
  areas = []
  for line in data:
    commands.append(line[0])
    areas.append(line[1])
  areas = [line.split(',') for line in areas]

  return commands, areas

def main():
  answer = 0
  commands, areas = parse_data()
  on = {}

  print(commands)
  print(areas)

  for i in range(len(commands)): #first 20 stay in range 50
    print(i)
    area = areas[i]
    area = [int(i) for i in area]
    if commands[i] == 'on':
      for x in range(area[0], area[1] + 1): # not a scalable solution
        for y in range(area[2], area[3] + 1):
          for z in range(area[4], area[5] + 1):
            pointStr = str([x,y,z])
            if pointStr not in on:
              on[pointStr] = True
    else:
      for x in range(area[0], area[1] + 1):
        for y in range(area[2], area[3] + 1):
          for z in range(area[4], area[5] + 1):
            pointStr = str([x,y,z])
            if pointStr in on:
              on.pop(pointStr)

  answer = len(on)
  print(answer)


if __name__ == "__main__":
  main()