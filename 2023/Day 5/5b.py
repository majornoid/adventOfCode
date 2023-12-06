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


nums = lines[0].split(" ")
seeds = []
del nums[0]
for i in range(0, len(nums), 2):
  details = {}
  details["start"] = int(nums[i])
  details["range"] = int(nums[i+1])
  seeds.append(details)

mappings = []
for line in lines:
  mappings.append(generateMapping(line))
  
# determine ranges that reach certain outcomes
# then use that to figure out the minimum from the seeds
# this is a lot faster than iterating through every seed
# and every mapping
ranges = []
for mapping in mappings:
  for map in mapping:
    start = map["start"]
    diff = map["diff"]
    range = map["range"]
    for i in range(range):
      if i*diff + start not in ranges:
        ranges.append(i*diff + start)
ranges.sort()
print(ranges)
for seed in seeds:
  curr = seed["start"]
  range = seed["range"]
  for i in range(range):
    if curr + i not in ranges:
      curr += i
      break
  if curr < min:
    min = curr
    print(seed, curr)
    
    

print(min)