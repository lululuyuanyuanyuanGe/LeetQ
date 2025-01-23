/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let farthest = 0;
    let currentEnd = 0;
    let jumps = 0;

    for (let i = 0; i < nums.length - 1; i ++) {
        farthest = Math.max(farthest, i + nums[i])
        if (currentEnd === i) {
            currentEnd = farthest;
            jumps ++;
        }
        if (currentEnd >= nums.length - 1){
            return jumps;
        }
    }
    return jumps
};