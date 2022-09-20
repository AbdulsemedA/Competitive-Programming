class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        l=[]
        l.append('0')
        for i in range(1,n):
            x=l[i-1]+'1' 
            s=''
            for j in l[i-1]:
                if j=='0':
                    s=s+'1'
                else:
                    s=s+'0'
            x=x+s[::-1]
            l.append(x)
        return l[-1][k-1]
