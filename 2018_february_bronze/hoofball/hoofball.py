def getListOfPeople(c, cows):
  curBallPos = c
  result = []

  while curBallPos not in set(result):
    closest = cows[-1]
    for i in range(len(cows) - 2, -1, -1):
      if cows[i] != curBallPos:
        if abs(curBallPos - cows[i]) <= abs(curBallPos - closest):
          closest = cows[i]
    result.append(closest)
    curBallPos = closest
  return result

def getMinBall(N, cows):
  cowLog = [0] * N
  for c in cows:
    print(getListOfPeople(c, cows))
  return 0
    
def main(inputFile, outputFile):
  hoofballInput = open(inputFile, 'r')
  hoofballOutput = open(outputFile, 'w')

  N = int(hoofballInput.readline().strip())
  
  cows = list(map(int, hoofballInput.readline().strip().split()))
  
  hoofballOutput.write(str(getMinBall(N, cows)) + '\n')
  
  hoofballInput.close()
  hoofballOutput.close()


main('hoofball.in', 'hoofball.out')
