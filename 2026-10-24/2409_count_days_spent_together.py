class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int: d=[31,28,31,30,31,30,31,31,30,31,30,31]; f=lambda s: sum(d[:int(s[:2])-1])+int(s[3:]); return max(0,min(f(leaveAlice),f(leaveBob))-max(f(arriveAlice),f(arriveBob))+1)
