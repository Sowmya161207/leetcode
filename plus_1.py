class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=" "
        for i in digits:
            s+=str(i)
        v=int(s)+1
        l=[]
        for i in str(v):
            l.append(int(i))
        return l