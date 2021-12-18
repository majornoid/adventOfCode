def main():
  answer = 0
  initials = []
  
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
  
  xVel = (testX-3)

  for testX in range(0, tarX[(len(tarX)-1)]+1):
    for testY in range(tarY[0], 1000):
      currX = 0
      currY = 0
      tempX = testX
      tempY = testY
      while currY >= tarY[0]:
        currX += tempX
        currY += tempY
        if tempX > 0:
          tempX -= 1
        elif tempX < 0:
          tempX += 1
        
        tempY -= 1

        if currY in tarY and currX in tarX:
          #print("Success: " + str(tempX) + " " + str(testY))
          initials.append((testX, testY))
          break




  answer = len(initials)
  #print(initials)

  print(answer)


if __name__ == "__main__":
  main()