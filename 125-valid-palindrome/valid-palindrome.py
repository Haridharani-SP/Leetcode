class Solution:
    def isPalindrome(self, s: str) -> bool:
        m=""
        for i in s:
            if i.lower() in "abcdefghijklmnopqrstuvwxyz" or i in "0123456789":
                m+=i
            else:
                continue
        m=m.lower()
        if m==m[::-1]:
            return True
        return False
