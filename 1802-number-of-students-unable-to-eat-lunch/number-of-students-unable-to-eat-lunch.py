class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unmet = 0
        students.reverse()
        sandwiches.reverse()
        while sandwiches:
            
            if students[-1] == sandwiches [-1]:
                students.pop()
                sandwiches.pop()
                unmet = 0
            else:
                unmet += 1
                last_elem = students.pop()
                students.insert(0, last_elem)
            if len(students) == unmet:
                return unmet
        return 0
        
            

        