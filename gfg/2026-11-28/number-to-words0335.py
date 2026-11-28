class Solution:
    def convertToWords(self, n):
        if n == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def below_thousand(x):
            words = []
            if x >= 100:
                words += [ones[x // 100], "Hundred"]
                x %= 100
            if x >= 20:
                words.append(tens[x // 10])
                x %= 10
            if x:
                words.append(ones[x])
            return words

        result = []
        for value, name in ((10**9, "Billion"), (10**6, "Million"), (1000, "Thousand"), (1, "")):
            if n >= value:
                result += below_thousand(n // value)
                if name:
                    result.append(name)
                n %= value
        return " ".join(result)
