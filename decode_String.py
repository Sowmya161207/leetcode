class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        word = ""

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)

            elif i == '[':
                stack.append((word, num))
                word = ""
                num = 0

            elif i == ']':
                old_word, n = stack.pop()
                word = old_word + word * n

            else:
                word = word + i

        return word