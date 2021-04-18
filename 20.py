class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_dict = {
            '(': -1,
            '{': -2,
            '[': -3,
            ')': 1,
            '}': 2,
            ']': 3
        }
        stack = []
        for char in s:
            if len(stack):
                last_char = stack.pop()
                if char_dict[char] < 0 or char_dict[last_char] + char_dict[char] != 0:
                    stack.append(last_char)
                    stack.append(char)
            else:
                stack.append(char)
        return not len(stack)
