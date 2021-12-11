inFile = open("25input.txt", 'r')
data = inFile.read().split()
pub1 = int(data[0])
pub2 = int(data[1])
ekey = 1
subject = 7
loop1 = 0
loop2 = 0
val = 1
x = 0

while loop1 == 0 and loop2 == 0:
  x += 1
  val = val * subject
  val = val % 20201227
  if val == pub1:
    loop1 = x
  if val == pub2:
    loop2 = x

for y in range(loop1):
  ekey = ekey * pub2
  ekey = ekey % 20201227

for y in range(loop2):
  ekey = ekey * pub1
  ekey = ekey % 20201227

print(ekey)