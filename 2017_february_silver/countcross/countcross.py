# def run(startPos, ranSet, notWentTo, roads, cowsSet, count):
#   possiblePos = [(startPos[0] - 1, startPos[1],), (startPos[0] + 1, startPos[1],), (startPos[0], startPos[1] + 1,), (startPos[0], startPos[1] - 1,)]
#   ranSet.add(startPos)
  
#   for p in possiblePos:
#     if p in roads: # checking if not out of range
#       if p not in ranSet: # check if already ran
#         if p not in roads[startPos]: # check if there's a road
#           notWentTo.remove(p)
#           ranSet.add(p)
#           if p in cowsSet:
#             count += 1
#           count = run(p, ranSet, notWentTo, roads, cowsSet, count)
#   return count

def run2(lastPos, curPos, ranSet, notWentTo, roads, cowsSet, count):
  if (curPos not in roads) or (curPos in ranSet) or (curPos in roads[lastPos]): # check if out of range
    return count
  ranSet.add(curPos)
  notWentTo.remove(curPos)
  if curPos in cowsSet:
    count += 1
  
  possiblePos = [(curPos[0] - 1, curPos[1],), (curPos[0] + 1, curPos[1],), (curPos[0], curPos[1] + 1,), (curPos[0], curPos[1] - 1,)]
  
  for p in possiblePos:
    count = run2(curPos, p, ranSet, notWentTo, roads, cowsSet, count)
  return count
       

def main(inputFile, outputFile):
  countcrossInput = open(inputFile, 'r')
  countcrossOutput = open(outputFile, 'w')
  
  N, K, R = countcrossInput.readline().strip().split()
  N, K, R = int(N), int(K), int(R)
  
  roads = {}
  cows = []
  cowsSet = set()
  notWentTo = set()
  
  for i in range(0, N):
    for j in range(0, N):
      roads[(i, j,)] = set()
      notWentTo.add((i, j,))
  
  for _ in range(R):
    line = countcrossInput.readline().strip().split()
    first, second = (int(line[0]) - 1, int(line[1]) - 1,), (int(line[2]) - 1, int(line[3]) - 1,)
    roads[first].add(second)
    roads[second].add(first)
  
  for _ in range(K):
    line = countcrossInput.readline().strip().split()
    cow = (int(line[0]) - 1, int(line[1]) - 1,)
    cowsSet.add(cow)
    cows.append(cow)
  
  # print(cows)
  # print(roads)
  arr = []
  total = K * (K - 1) // 2
  while len(notWentTo) != 0:
    start = notWentTo.pop()
    notWentTo.add(start)
    result = run2(start, start, set(), notWentTo, roads, cowsSet, 0)
    if result != 0:
      arr.append(result)
    total -= result * (result - 1) // 2
  countcrossOutput.write(str(total) + '\n')
  
  countcrossInput.close()
  countcrossOutput.close()


main('countcross.in', 'countcross.out')
