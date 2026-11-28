class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable = min(income, upper) - prev
            tax += taxable * percent / 100
            prev = upper
        return tax
