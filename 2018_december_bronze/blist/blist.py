def getBuckets(time, cows):
  buckets = 0
  for c in cows:
    if c[0] <= time < c[1]:
      buckets += c[2]
  return buckets

def getMaxBucket(cows):
  maxBucket = 0
  for t in range(1, 1001):
    maxBucket = max(maxBucket, getBuckets(t, cows))
  return maxBucket

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