def ifDivideBy3(cur: int):
  s = 0
  while cur:
    s += cur % 10
    cur //= 10
  if s % 3 == 0:
    # divisible by 3
    return True
  return False


def ifDivideBy5(cur: int):
  lastDigit = cur % 10
  if lastDigit == 0 or lastDigit == 5:
    # divisible by 5
    return True
  return False


def getNum(N):
  count = 0
  cur = 1
  while count != N:
    divide3 = ifDivideBy3(cur)
    divide5 = ifDivideBy5(cur)
    
    if not divide3 and not divide5:
      count += 1
    cur += 1
  return cur - 1
    

def main(inputFile: str, outputFile: str):
  moobuzzInput = open(inputFile, 'r')
  moobuzzOutput = open(outputFile, 'w')
  
  N = int(moobuzzInput.readline())

  moobuzzOutput.write(str(getNum(N)) + '\n')
  
  moobuzzInput.close()
  moobuzzOutput.close()


main('moobuzz.in', 'moobuzz.out')
