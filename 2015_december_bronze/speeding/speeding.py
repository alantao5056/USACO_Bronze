def getLimitOrBessie(distance, x):
  speedCount = 0
  curSpeedLimit = 0
  for i in range(0, len(x)):
    speedCount += x[i][0]
    if distance <= speedCount:
      return x[i][1]

def findMaxSpeeding(speedLimits, bessieSpeed):
  speeding = 0
  for i in range(1, 100 + 1):
    speedLimit = getLimitOrBessie(i, speedLimits)
    curSpeed = getLimitOrBessie(i, bessieSpeed)
    speeding = max(speeding, curSpeed - speedLimit)
  return speeding

def main(inputFile, outputFile):
  speedingInput = open(inputFile, 'r')
  speedingOutput = open(outputFile, 'w')
  
  N, M = speedingInput.readline().strip().split()
  N, M = int(N), int(M)
  
  speedLimits = []
  for _ in range(N):
    line = speedingInput.readline().strip().split()
    speedLimits.append([int(line[0]), int(line[1])])

  bessieSpeed = []
  for _ in range(M):
    line = speedingInput.readline().strip().split()
    bessieSpeed.append([int(line[0]), int(line[1])])
  
  speedingOutput.write(str(findMaxSpeeding(speedLimits, bessieSpeed)) + '\n')
  speedingInput.close()
  speedingOutput.close()

main('speeding.in', 'speeding.out')