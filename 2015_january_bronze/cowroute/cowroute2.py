import math


def getCheapestRoute(a, b, planes: list):
  least = math.inf
  for p in planes:
    aInArray = False
    bInArray = False
    for d in p[1]:
      if d == a:
        aInArray = True
      if d == b:
        if aInArray:
          least = min(least, p[0])
        else:
          break

  if least == math.inf:
    return -1
  return least

def main(inputFile: str, outputFile: str):
  cowrouteInput = open(inputFile, 'r')
  cowrouteOutput = open(outputFile, 'w')

  A, B, N = [int(x) for x in cowrouteInput.readline().split()]

  planes = []

  for _ in range(0, N):
    cost = int(cowrouteInput.readline().strip().split()[0])
    route = [int(x) for x in cowrouteInput.readline().strip().split()]

    planes.append((cost, route))

  # print(planes)

  cowrouteOutput.write('{}\n'.format(getCheapestRoute(A, B, planes)))

  cowrouteInput.close()
  cowrouteOutput.close()


main('cowroute.in', 'cowroute.out')
