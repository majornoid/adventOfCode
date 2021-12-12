def parse_data():
  with open('12input.txt', 'r') as inFile:
    connections = inFile.read().split()
  connections = [i.split('-') for i in connections]

  cavesList = []
  for connection in connections:
    for cave in connection:
      cavesList.append(cave)

  caves = set(cavesList)

  graph = {}

  for cave in caves:
    graph[cave] = []

  for connection in connections:
    a = connection[0]
    b = connection[1]
    graph[a].append(b)
    graph[b].append(a)

  return graph

def visit_cave(cave, graph, log, allowTwice, paths):
  visited = log.copy()
  allowRepeat = allowTwice.copy()
  if cave not in visited or (allowRepeat[0] and cave != 'start'):
    if cave in visited:
      #print(cave + " visited twice, no more repeats")
      allowRepeat[0] = False
    if cave == 'end':
      paths[0] += 1
      return
    if not cave.isupper():
      visited.append(cave)
    for neighbor in graph[cave]:
      visit_cave(neighbor, graph, visited, allowRepeat, paths)

def main():
  answer = 0
  graph = parse_data()

  visited = []
  allowTwice = []
  allowTwice.append(True)
  paths = []
  paths.append(0)

  visit_cave('start', graph, visited, allowTwice, paths)

  print(paths[0])

if __name__ == "__main__":
  main()