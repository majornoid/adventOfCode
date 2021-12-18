def main():
  answer = 0

  step = 0
  currX = 0
  currY = 0
  xVel = 0
  yVel = 0

  #set target area
  tarX = [*range(111,162)]
  tarY = [*range(-154, -100)]

  testX = 0
  #detimines max number of steps (lowest xVel possible)
  while currX <= tarX[(len(tarX)-1)]:
    testX += 1
    currX += testX
  
  xVel = (testX-1)

  for testY in range(-620, 620):
    currX = 0
    currY = 0
    tempX = xVel
    tempY = testY
    highestY = 0
    while currY >= tarY[0]:
      currX += tempX
      currY += tempY
      if tempX > 0:
        tempX -= 1
      elif tempX < 0:
        tempX += 1
      
      tempY -= 1

      if currY > highestY:
        highestY = currY

      if currY in tarY and currX in tarX:
        #print(currY, currX)
        #print("In Target: " + str(testY) + ' ' + str(xVel))
        if highestY > answer:
          answer = highestY
    #print(highestY)






  print(answer)


if __name__ == "__main__":
  main()