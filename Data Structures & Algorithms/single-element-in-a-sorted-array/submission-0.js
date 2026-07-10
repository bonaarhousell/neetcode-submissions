class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNonDuplicate(nums) {
        
        let i = 0
        let k = 1

        while (true){
            if (nums[i] != nums[k]){
                return nums[i]
            }
            i += 2
            k += 2
        }
        

    }
}
