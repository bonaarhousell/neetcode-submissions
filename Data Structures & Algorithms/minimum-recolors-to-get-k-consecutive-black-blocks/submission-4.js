class Solution {
    /**
     * @param {string} blocks
     * @param {number} k
     * @return {number}
     */
    minimumRecolors(blocks, k) {
        let count_w = 0
        for(let i = 0; i < k; i++){
            if (blocks[i] === 'W' ){
                count_w++
            }
        }

        let res = count_w
        for(let i = k; i < blocks.length; i++){
            if(blocks[i - k] === 'B'){
                count_w++
            }
            if(blocks[i] === 'B'){
                count_w--
            }
            res = Math.min(res, count_w)
        }
        return res

    }
}
