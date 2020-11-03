def findMaxSpeeding(speedLimits, bessieSpeed):
  speedLimitsList = [-1] * 101
  speeding = 0
  
  count = 1
  for s in speedLimits:
    for i in range(count, count + s[0]):
      speedLimitsList[i] = s[1]
    count += s[0]
  # print(speedLimitsList)
  bessieCount = 1
  for b in bessieSpeed:
    for j in range(bessieCount, bessieCount + b[0]):
      speeding = max(speeding, b[1] - speedLimitsList[j])
    bessieCount += b[0]
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