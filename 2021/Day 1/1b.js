const fs = require('fs')
fs.readFile('1input.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return -1
  }

  let nums = data.split("\n")
  let answer = 0

  for(let i = 1; i <= nums.length-2; i++){
    if ( ( Number(nums[i]) + Number(nums[i+1]) + Number(nums[i+2]) ) > ( Number(nums[i]) + Number(nums[i+1]) + Number(nums[i-1]) ) ){
      answer += 1
    }
  }
  
  console.log(answer)

})
