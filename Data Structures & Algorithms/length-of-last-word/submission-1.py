class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr = len(s) - 1
        length = 0
        while curr >= 0 and s[curr] == " ":
            curr -= 1
        while curr >= 0 and s[curr] != " ":
            length += 1
            curr -= 1

        return length
