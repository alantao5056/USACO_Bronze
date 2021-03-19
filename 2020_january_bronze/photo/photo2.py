def checkOrder(B, first):
  orderArr = [False for _ in range(0, len(B) + 1)]
  order = [first]
  cur = first
  for i in range(0, len(B)):
    nextNum = B[i] - cur
    if nextNum - 1 <= len(B):
      if orderArr[nextNum - 1] == False:
        orderArr[nextNum - 1] = True
      else:
        return False
    else:
      return False
    order.append(nextNum)
    cur = nextNum
  return order


def getCowOrder(B, N):
  firstNum = B[0]
  for i in range(1, firstNum):
    result = checkOrder(B, i)
    if result:
      return result


def main(inputFile, outputFile):
  photoInput = open(inputFile, 'r')
  photoOutput = open(outputFile, 'w')

  N = int(photoInput.readline().strip())
  B = list(map(int, photoInput.readline().strip().split()))

  photoOutput.write(' '.join(map(str, getCowOrder(B, N))) + '\n')

  photoInput.close()
  photoOutput.close()


main('photo.in', 'photo.out')
