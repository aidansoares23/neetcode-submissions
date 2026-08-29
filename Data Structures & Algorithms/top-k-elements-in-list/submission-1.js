// class Solution {
//     /**
//      * @param {number[]} nums
//      * @param {number} k
//      * @return {number[]}
//      */

    
//     topKFrequent(nums, k) {
//         // Plain object as a hashmap: keys = numbers, values = frequency counts
//         const count = {};

//         // for...of iterates over VALUES of the array (contrast with for...in which iterates keys)
//         for (const num of nums) {
//             // || 0 trick: if count[num] is undefined (first time seen), undefined || 0 = 0, then +1
//             // On repeat visits, the existing count is used
//             count[num] = (count[num] || 0) + 1;
//         }

//         // Object.entries converts the object to [[key, value], ...] pairs — keys are always strings
//         // .map with ([num, freq]) destructures each pair directly in the params (no entry[0]/entry[1])
//         const arr = Object.entries(count).map(([num, freq]) => [
//             freq,           // swap order: put freq first so we can sort by pair[0]
//             parseInt(num),  // parseInt converts the string key "1" back to the number 1
//         ]);

//         // Comparator b[0] - a[0] sorts DESCENDING by frequency
//         // Positive result = b first, negative = a first
//         // Note: sort mutates arr in place, unlike map/slice which return new arrays
//         arr.sort((a, b) => b[0] - a[0]);

//         // slice(0, k) takes the first k elements non-destructively (new array)
//         // .map(pair => pair[1]) extracts just the number, discarding freq now that sorting is done
//         return arr.slice(0, k).map((pair) => pair[1]);
//     }
// }

class Solution {
    topKFrequent(nums, k) {
        
        // Build frequency map
        const count = {};
        for (const num of nums) {
            if (count[num] === undefined) {
                count[num] = 1;
            } else {
                count[num] = count[num] + 1;
            }
        }

        // Convert to array of pairs [[freq, num], ...]
        const arr = [];
        const entries = Object.entries(count); // [["1", 3], ["2", 1], ...]
        for (let i = 0; i < entries.length; i++) {
            const entry = entries[i];
            const numAsString = entry[0];
            const freq = entry[1];
            const numAsInt = parseInt(numAsString);
            arr.push([freq, numAsInt]);
        }

        // Sort descending by frequency
        arr.sort(function(a, b) {
            return b[0] - a[0];
        });

        // Extract the top k numbers
        const result = [];
        for (let i = 0; i < k; i++) {
            const pair = arr[i];
            result.push(pair[1]);
        }

        return result;
    }
}