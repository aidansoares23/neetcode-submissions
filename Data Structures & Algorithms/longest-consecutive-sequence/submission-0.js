class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const mp = new Map();
        let result = 0;

        for (let num of nums) {
            if (!mp.has(num)) {
                mp.set(
                    num,
                    (mp.get(num - 1) || 0) + (mp.get(num + 1) || 0) + 1, 
                );
                mp.set(num - (mp.get(num - 1) || 0), mp.get(num));
                mp.set(num + (mp.get(num + 1) || 0), mp.get(num));
                result = Math.max(result, mp.get(num));
            }
        }
        return result;
    }
}
