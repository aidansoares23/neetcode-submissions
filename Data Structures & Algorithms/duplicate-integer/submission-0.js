class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // Convert the array into a hash set, which removes duplicates
        // This is the nature of a set (arr w/out dups)
        // Compare the size of the set with the size of the original array
        // If the the set is smaler, return true because duplicates must have been removed
        // Otherwise, return false
        const mySet = [...new Set(nums)];
        const hasDuplicates = mySet.length < nums.length;
        if (hasDuplicates) return true;
        else return false; 
        // return new Set(nums).size < nums.length;
    }
}
