def couldAdd(distanceRan, finishSpeed, speed, distance):
  if speed == 0:
    return True
  speed += 1
  distanceRan += speed
  while distanceRan < distance:
    distanceRan += (speed - 1)
    speed -= 1
    if speed == 0:
      return True
  if speed > finishSpeed:
    return False
  return True


def couldKeepGoing(distanceRan, finishSpeed, speed, distance):
  if distanceRan + speed >= distance and speed <= finishSpeed:
    return True
  distanceRan += speed
  return couldAdd(distanceRan, finishSpeed, speed, distance)


def getTime(distance, finishSpeed):
  distanceRan = 0
  curSpeed = 0
  count = 0

  while distanceRan < distance:
    if couldAdd(distanceRan, finishSpeed, curSpeed, distance):
      curSpeed += 1
      distanceRan += curSpeed
    elif couldKeepGoing(distanceRan, finishSpeed, curSpeed, distance):
      distanceRan += curSpeed
    else:
      curSpeed -= 1
      distanceRan += curSpeed
    count += 1
  return count


def main(inputFile: str, outputFile: str):
  raceInput = open(inputFile, 'r')
  raceOutput = open(outputFile, 'w')

  K, N = [int(x) for x in raceInput.readline().strip().split()]

  for _ in range(N):
    x = int(raceInput.readline().strip())
    raceOutput.write(f'{getTime(K, x)}\n')

  raceInput.close()
  raceOutput.close()


main('race.in', 'race.out')
