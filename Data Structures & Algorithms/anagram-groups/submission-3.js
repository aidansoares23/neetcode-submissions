class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // Make a result object
        // Iterate over eadch string
        // For each string, sort the chars
        // Add it to the result map as a keyif it isn't already there, value being an empty list
        // Then, sortedString (key) -> current string in iteration (value)
        // return the values from the result map, so it's a list of lists

        const result = {};
        for (let string of strs) {
            const sortedString = string.split('').sort().join('');
            if (!result[sortedString]) {
                result[sortedString] = [];
            }
            result[sortedString].push(string);
        }
        return Object.values(result);
    }
}
