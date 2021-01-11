from itertools import combinations

def checkIfValid(tup: tuple):
  # check if parallel to x
  xParallel = False
  base = 0
  height = 0
  
  if tup[0][0] == tup[1][0]:
    xParallel = True
    base = abs(tup[0][1] - tup[1][1])
  elif tup[0][0] == tup[2][0]:
    xParallel = True
    base = abs(tup[0][1] - tup[2][1])
  elif tup[1][0] == tup[2][0]:
    xParallel = True
    base = abs(tup[1][1] - tup[2][1])
 
  if not xParallel:
    return False

  # check if parallel to y
  if tup[0][1] == tup[1][1]:
    return (base, abs(tup[0][0] - tup[1][0]),)
  if tup[0][1] == tup[2][1]:
    return (base, abs(tup[0][0] - tup[2][0]),)
  if tup[1][1] == tup[2][1]:
    return (base, abs(tup[1][0] - tup[2][0]),)
  
  
  return False

def findMaxArea(N: int, posts: list) -> int:
  maxArea = -1
  for p in combinations(posts, 3):
    # print(p)
    ifValid = checkIfValid(p)
    if ifValid:
      maxArea = max(maxArea, (ifValid[0] * ifValid[1]) / 2)
  return maxArea * 2
  
def main(inputFile: str, outputFile: str):  
  trianglesInput = open(inputFile, 'r')
  trianglesOutput = open(outputFile, 'w')

  N = int(trianglesInput.readline().strip())
  
  posts = []
  for _ in range(N):
    line = trianglesInput.readline().strip().split()
    posts.append((int(line[0]), int(line[1]),))
    
  # print(fences)
  
  trianglesOutput.write('{}\n'.format(int(findMaxArea(N, posts))))
  
  trianglesInput.close()
  trianglesOutput.close()


main('triangles.in', 'triangles.out')
