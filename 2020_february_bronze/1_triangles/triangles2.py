import math

class Post:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
    self.maxSideY = 0
    self.maxSideX = 0
  
  def setSideY(self, sideY: int):
    self.maxSideY = max(self.maxSideY, sideY)
  
  def setSideX(self, sideX: int):
    self.maxSideX = max(self.maxSideX, sideX)

  def areaX2(self):
    return self.maxSideX * self.maxSideY

def findMaxArea(N: int, posts: list) -> int:
  for i in range(0, N):
    for j in range(i + 1, N):
      if posts[i].x == posts[j].x:
        sideY = abs(posts[i].y - posts[j].y)
        posts[i].setSideY(sideY)
        posts[j].setSideY(sideY)
      elif posts[i].y == posts[j].y:
        sideX = abs(posts[i].x - posts[j].x)
        posts[i].setSideX(sideX)
        posts[j].setSideX(sideX)
  
  maxArea = 0
  for post in posts:
    maxArea = max(maxArea, post.areaX2())
  
  return maxArea

def main(inputFile: str, outputFile: str):
  input = open(inputFile, 'r')
  output = open(outputFile, 'w')

  N = int(input.readline().strip())
  posts = []
  for _ in range(0, N):
    x, y = input.readline().strip().split()
    posts.append(Post(int(x), int(y)))

  maxArea = findMaxArea(N, posts)
  output.write(f'{maxArea}\n')

  input.close()
  output.close()

main('triangles.in', 'triangles.out')