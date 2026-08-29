class Solution:

    def encode(self, strs: List[str]) -> str:
        # Init an emptry result string
        res = ""
        # For each string
        for string in strs:
            # compute the length
            # Append (length#string) to the result
            res += str(len(string)) + "#" + string
        # Return final encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Init an empty list for decoded strings
        res = []
        # and point i = 0
        i = 0

        # Move a pointer j forward until it finds '#' - the length
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # convert the substring s[i:j] into an integer length
            length = int(s[i:j])
            # Move i to the next character after #
            i = j + 1
            # Extract the next length characters - the original string
            j = i + length
            # Append the extracted string to the result list
            res.append(s[i:j])
            # Move i forward by length to continue decoding the next segment
            i = j

        return res
