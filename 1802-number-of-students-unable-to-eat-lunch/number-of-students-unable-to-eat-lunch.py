class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unmet = 0
        while sandwiches:
            
            if students[0] == sandwiches [0]:
                students.pop(0)
                sandwiches.pop(0)
                unmet = 0
            else:
                unmet += 1
                first_elem = students.pop(0)
                students.append(first_elem)
            if students and len(students) == unmet:
                return unmet
        return 0
        
            

        