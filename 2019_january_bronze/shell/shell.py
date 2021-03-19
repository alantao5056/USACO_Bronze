def getScore(ballPos, guess):
  curBallPos = ballPos
  count = 0
  for g in guess:
    if curBallPos == g[0]:
      correctAnswer = g[1]
    elif curBallPos == g[1]:
      correctAnswer = g[0]
    else:
      correctAnswer = 6 - g[0] - g[1]
    if correctAnswer == g[2]:
      count += 1
    curBallPos = correctAnswer
  return count
    

def getMaxScore(guess):
  maxScore = -1
  for ballPos in range(1, 4):
    maxScore = max(maxScore, getScore(ballPos, guess))
  return maxScore

def main(inputFile, outputFile):
  shellInput = open(inputFile, 'r')
  shellOutput = open(outputFile, 'w')
  
  N = int(shellInput.readline().strip())
  guess = []
  
  for _ in range(N):
    line = shellInput.readline().strip().split()
    guess.append([int(line[0]), int(line[1]), int(line[2])])
  
  shellOutput.write(str(getMaxScore(guess)) + '\n')
  
  shellInput.close()
  shellOutput.close()

main('shell.in', 'shell.out')