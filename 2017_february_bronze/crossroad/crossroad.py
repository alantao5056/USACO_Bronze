def getCrossings(cows):
  cowLog = {}
  count = 0
  for i in range(0, len(cows)):
    cowID = cows[i][0]
    cowSide = cows[i][1]
    if cowID not in cowLog:
      cowLog[cowID] = cowSide
    elif cowLog[cowID] != cowSide:
      count += 1
      cowLog[cowID] = cowSide
  return count

def main(inputFile, outputFile):
  crossroadInput = open(inputFile, 'r')
  crossroadOutput = open(outputFile, 'w')
  N = int(crossroadInput.readline().strip())
  
  cows = []
  for _ in range(N):
    line = crossroadInput.readline().strip().split()
    cows.append([int(line[0]), int(line[1])])
  # print(cows)
  crossroadOutput.write(f'{getCrossings(cows)}\n')
  crossroadInput.close()
  crossroadOutput.close()

main('crossroad.in', 'crossroad.out')