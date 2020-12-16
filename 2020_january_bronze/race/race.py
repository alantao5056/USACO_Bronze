def getSpeedAdd(K, x, curDistance, curSpeed):
  for i in range(curSpeed, x - 1, -1):
    curDistance += i
  if curDistance == K:
    return 0
  return 1
  

def getTime(K, x):
  count = 0
  curDistance = 0
  curSpeed = 0

  while curDistance < K:
    curSpeed += getSpeedAdd(K, x, curDistance, curSpeed)
    curDistance += curSpeed
    count += 1

  return count


def main(inputFile: str, outputFile: str):
  raceInput = open(inputFile, 'r')
  raceOutput = open(outputFile, 'w')

  K, N = [int(x) for x in raceInput.readline().strip().split()]

  for _ in range(N):
    x = int(raceInput.readline().strip())
    raceOutput.write(f'{getTime(K, x)}\n')


main('race.in', 'race.out')
