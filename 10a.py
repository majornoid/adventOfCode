def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('10input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = rawData
  return data

def isValid(s):
  left = []
  valid = True
  score = 0
  for e in s: #iterates through characters (elements) in string
    #print(left)
    if e == '(' or e == '{' or e == '[' or e == '<':
      left.insert(0, e) #new left bracket will be put at front of list

    elif e == ')':
      if left and left[0] == '(':
        left.pop(0) #when a bracket is closed by the proper bracket, it will be removed
      else:
        valid = False #if attempting to close with improper bracket, mark invalid and break
        score = 3
        break

    elif e == ']':
      if left and left[0] == '[':
        left.pop(0)
      else:
        valid = False
        score = 57
        break   

    elif e == '}':
      if left and left[0] == '{':
        left.pop(0)
      else:
        valid = False
        score = 1197
        break

    elif e == '>':
      if left and left[0] == '<':
        left.pop(0)
      else:
        valid = False
        score = 25137
        break
  #print(score)
  return score

  if left: #if left has not been emptied, a bracket hasn't been closed
      valid = False
  return valid
    

def main():
  answer = 0
  data = parse_data()
  for row in data:
    print(answer)
    answer += isValid(row)
  
  print(answer)

if __name__ == "__main__":
  main()