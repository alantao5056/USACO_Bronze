def couldAdd(distanceRan, finishSpeed, speed, distance):
  while distanceRan < K:
    distanceRan += (speed - 1)
    if speed == 0:
      return True
  if speed > finishSpeed:
    return False
  return True

def getTime(distance, finishSpeed):
  distanceRan = 0
  runningLog = []
  
  
  
def main(inputFile: str, outputFile: str):
  raceInput = open(inputFile, 'r')
  raceOutput = open(outputFile, 'w')

  K, N = [int(x) for x in raceInput.readline().strip().split()]

  for _ in range(N):
    x = int(raceInput.readline().strip())
    raceOutput.write(f'{getTime(K, x)}\n')


main('race.in', 'race.out')
