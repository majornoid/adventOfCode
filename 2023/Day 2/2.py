inFile = open("input.txt" , 'r')
games = inFile.read().split("\n")

idSum = 0

red = 12
green = 13
blue = 14

for game in games:
  game = game.split(":")
  try:
    idInt = int(game[0][5:])
  except:
    break
  subsets = game[1].split(";")
  valid = True
  for subset in subsets:
    colors = subset.split(",")
    for color in colors:
      if color[-3:] == "red":
        if int(color[:-4]) > red:
          valid = False
          break
      elif color[-5:] == "green":
        if int(color[:-6]) > green:
          valid = False
          break
      elif color[-4:] == "blue":
        if int(color[:-5]) > blue:
          valid = False
          break
  if valid:
    idSum += idInt
print(idSum)