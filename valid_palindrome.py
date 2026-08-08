class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=""
        for i in s:
            if i.isalnum():
                if 65<=ord(i)<=90:
                    ss+=chr(ord(i)+32)
                else:
                    ss+=i
        if ss[0:]==ss[::-1]:
            return True