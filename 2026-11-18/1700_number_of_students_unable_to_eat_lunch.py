class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        want = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if want[sandwich] == 0:
                break
            want[sandwich] -= 1
        return want[0] + want[1]
