class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal=int(a,2)+int(b,2)
        return bin(decimal)[2:]
        