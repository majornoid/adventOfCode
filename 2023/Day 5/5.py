inFile = open("input.txt" , 'r')
lines = inFile.read().split("\n\n")
min = 10000000000000000

def generateMapping(string):
  lines = string.split("\n")
  mapping = []
  del lines[0]
  for line in lines:
    details = {}
    line = line.split(" ")
    nums = [int(i) for i in line]
    details["start"] = nums[1]
    details["diff"] = nums[0] - nums[1]
    details["range"] = nums[2]
    mapping.append(details)
  return mapping


seeds = lines[0].split(" ")
del seeds[0]
seeds = [int(i) for i in seeds]
del lines[0]

mappings = []
for line in lines:
  mappings.append(generateMapping(line))
  
for seed in seeds:
  curr = seed
  for mapping in mappings:
      for map in mapping:
        if curr >= map["start"] and curr < map["start"] + map["range"]:
          curr += map["diff"]
          break
  if curr < min:
    min = curr
    

print(min)