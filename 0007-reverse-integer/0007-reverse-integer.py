class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        if a[0]=="-":
            y=int(a[0]+a[:-len(a):-1])
        else:
            y=int(a[::-1])
        if -2**31 <= y <= 2**31 - 1:
            return y
        else:
            return 0