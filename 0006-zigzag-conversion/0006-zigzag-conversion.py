class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        row=[""]*numRows
        cur_row=0
        step=1
        for i in s:
            row[cur_row]+=i
            if cur_row==0:
                step=1
            elif cur_row==numRows-1:
                step=-1
            cur_row=cur_row+step
        s1=""
        for i in row:
            s1=s1+i
        return s1

        
        
        
        