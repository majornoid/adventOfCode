def main():
  answer = 0
  rolls = 0
  diePos = 0
  pos1 = 4  # set your starting values here
  pos2 = 7
  score1 = 0
  score2 = 0
  losingScore = 0

  while score1 < 1000 or score2 < 1000:
    currMove = 0
    for _ in range(3):
      rolls += 1
      diePos += 1
      currMove += rolls
    if diePos == 101:
      diePos = 1
    pos1 += currMove
    while pos1 > 10:
      pos1 -= 10
    score1 += pos1
    
    #print(diePos)

    if score1 >= 1000:
      break

    currMove = 0
    for _ in range(3):
      rolls += 1
      diePos += 1
      currMove += rolls
    if diePos == 101:
      diePos = 1
    pos2 += currMove
    while pos2 > 10:
      pos2 -= 10
    score2 += pos2

    #print(diePos)
    #print(rolls)
    #print("Pos 1: " + str(pos1))
    #print("Pos 2: " + str(pos2))
    #print("Score 1: " + str(score1))
    #print("Score 2: " + str(score2))
    #print("Rolls: " + str(rolls))

  print("Score 1: " + str(score1))
  print("Score 2: " + str(score2))
  print("Rolls: " + str(rolls))
  
  if score1 < score2:
    losingScore = score1
  else:
    losingScore = score2

  answer = losingScore * rolls

  print(answer)


if __name__ == "__main__":
  main()