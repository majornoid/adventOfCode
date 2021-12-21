def take_turn(score1, pos1, score2, pos2, wins, rollDist, multFactor, turn):
  turn += 1
  for total1 in rollDist:
    #if score1 == 0:
    #  print("Total 1: " + str(total1))
    newPos1   = pos1
    newScore1 = score1
    newPos1 += total1
    if newPos1 > 10:
      newPos1 -= 10
    newScore1 += newPos1
    if newScore1 >= 21:
      wins[0] += rollDist[total1] * multFactor
      #if wins[0] % 10000000 == 0:
      #  print("Player 1 Wins: " + str(wins[0]))    
    else:
      for total2 in rollDist:
        #if score2 == 0:
        #  print("Total 2: " + str(total2))
        newPos2   = pos2
        newScore2 = score2
        newPos2 += total2
        if newPos2 > 10:
          newPos2 -= 10
        newScore2 += newPos2
        if newScore2 >= 21:
          wins[1] += rollDist[total2] * multFactor
          #if wins[1] % 10000000 == 0:
          #  print("Player 2 Wins: " + str(wins[1]))
        else:
          newMultFactor = multFactor * (rollDist[total1] * rollDist[total2])
          #if multFactor < 1000000:
          #  print("Taking Turn: " + str(turn) + " - Score 1: " + str(newScore1) + "   Score 2: " + str(newScore2) + "   Mult: " + str(multFactor))
          take_turn(newScore1, newPos1, newScore2, newPos2, wins, rollDist, newMultFactor, turn)

def main():
  answer = 0
  wins = [0,0]
  pos1 = 4 # set your starting values here
  pos2 = 7
  score1 = 0
  score2 = 0
  rollDist = {}
  multFactor = 1

  for roll1 in [1,2,3]:
    for roll2 in [1,2,3]:
      for roll3 in [1,2,3]:
        total = roll1 + roll2 + roll3
        if total in rollDist:
          rollDist[total] += 1
        else:
          rollDist[total] = 1


  #print(rollDist)

  take_turn(score1, pos1, score2, pos2, wins, rollDist, multFactor, 0)

  #print(wins)

  if wins[0] > wins[1]:
    answer = wins[0]
  else:
    answer = wins[1]

  print(answer)


if __name__ == "__main__":
  main()