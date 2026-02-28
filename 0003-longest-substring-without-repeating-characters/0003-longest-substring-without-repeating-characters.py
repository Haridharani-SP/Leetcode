class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==1:
            return 1
        b=[]
        a=""
        for i in s:
            if i not in a:
                a=a+i
            else:
                b.append(len(a))
                ind=a.index(i)
                a=a[ind+1:]+i
        b.append(len(a))
        return max(b)


            
        