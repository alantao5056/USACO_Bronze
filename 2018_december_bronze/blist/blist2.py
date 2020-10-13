def getMaxBucket(cows):
  bucketList = [0] * 1001
  for c in cows:
    for i in range(c[0], c[1] + 1):
      bucketList[i] += c[2]
  return max(bucketList)

def main(inputFile, outputFile):
  blistInput = open(inputFile, 'r')
  blistOutput = open(outputFile, 'w')
  
  N = int(blistInput.readline().strip())
  cows = []
  for _ in range(0, N):
    line = blistInput.readline().strip().split()
    line = list(map(int, line))
    cows.append(line)
  # print(getMaxBucket(cows))
  blistOutput.write(str(getMaxBucket(cows)) + '\n')
  blistInput.close()
  blistOutput.close()

main('blist.in', 'blist.out')