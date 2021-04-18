class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        char_dict = {}
        need_extra_length = 0
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
                continue
            char_dict[char] += 1

        for key in char_dict:
            need_extra_length += char_dict[key] % 2
            ans += 2 * (char_dict[key]//2)
        if need_extra_length:
            ans += 1
        return ans


solution = Solution()
print solution.longestPalindrome("sseee1")
