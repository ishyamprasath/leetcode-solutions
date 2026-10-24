class Solution:
    def convertToBase7(self, num: int) -> str: return "0" if num==0 else ("-"+self.convertToBase7(-num) if num<0 else self.convertToBase7(num//7).lstrip("0")+str(num%7))
