def getMooCount(start: int, end: int) -> int:
  moo3 = int(end / 3) - int(start / 3)
  moo5 = int(end / 5) - int(start / 5)
  moo15 = int(end / 15) - int(start / 15)
  
  return moo3 + moo5 + moo15

def getNum(N: int):
  cur = N
  

print(getMooCount(1, 5))