inFile = open("input.txt" , 'r')
games = inFile.read().split("\n")

powerSum = 0

for game in games:
  game = game.split(":")
  try:
    idInt = int(game[0][5:])
  except:
    break
  redMax = 0
  greenMax = 0
  blueMax = 0
  subsets = game[1].split(";")
  for subset in subsets:
    colors = subset.split(",")
    for color in colors:
      if color[-3:] == "red":
        if int(color[:-4]) > redMax:
          redMax = int(color[:-4])
      elif color[-5:] == "green":
        if int(color[:-6]) > greenMax:
          greenMax = int(color[:-6])
      elif color[-4:] == "blue":
        if int(color[:-5]) > blueMax:
          blueMax = int(color[:-5])
  powerSum += redMax * greenMax * blueMax
print(powerSum)