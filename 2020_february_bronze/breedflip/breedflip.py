def getMinFlip(A, B, N):
  count = 0
  sequence = True
  for i in range(0, N):
    if A[i] == B[i]:
      if not sequence:
        sequence = True
        count += 1
    else:
      sequence = False
  return count

def main(inputFile, outputFile):
  breedInput = open(inputFile, 'r')
  breedOutput = open(outputFile, 'w')
  
  N = int(breedInput.readline().strip())
  
  A = breedInput.readline().strip()
  B = breedInput.readline().strip()
   
  breedOutput.write(f'{getMinFlip(A, B, N)}\n')
  
  breedInput.close()
  breedOutput.close()
  
  
main('breedflip.in', 'breedflip.out')
  