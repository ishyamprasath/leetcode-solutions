class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        d = int(day[:-2])
        m = months.index(month) + 1
        return f"{year}-{m:02d}-{d:02d}"
