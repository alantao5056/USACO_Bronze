def checkOrder(order: list, N):
  orderSet = set(order)
  for i in range(1, N + 1):
    if i not in orderSet:
      return False
  return True


def getOrder(B, first):
  order = [first]
  cur = first
  for i in range(0, len(B)):
    nextNum = B[i] - cur
    order.append(nextNum)
    cur = nextNum
  return order


def getCowOrder(B, N):
  firstNum = B[0]
  for i in range(1, firstNum):
    order = getOrder(B, firstNum - i)
    if checkOrder(order, N):
      return order


def main(inputFile, outputFile):
  photoInput = open(inputFile, 'r')
  photoOutput = open(outputFile, 'w')

  N = int(photoInput.readline().strip())
  B = list(map(int, photoInput.readline().strip().split()))

  photoOutput.write(' '.join(map(str, getCowOrder(B, N))) + '\n')

  photoInput.close()
  photoOutput.close()


main('photo.in', 'photo.out')
