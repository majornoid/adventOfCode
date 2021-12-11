const fs = require('fs')
fs.readFile('1input.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return -1
  }

  let nums = data.split("\n")

  let answer = 0

  for(let i = 1; i <= nums.length; i++){
    if (Number(nums[i]) > Number(nums[i-1])){
      answer += 1
    }
  }
  console.log(answer)

})
