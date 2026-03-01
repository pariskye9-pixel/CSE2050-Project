class Student:
    def __init__(self,student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses = dict()
    
    def enroll(self, course, grade):
        self.courses[course] = grade


class Course:
    def __init__(self, course_code: str, credits: int):
        self.course_code = course_code
        self.credits = credits
        self.students = list()

    def add_student(self, student: Student):
        self.students.append(student)
    
    def get_student_count(self):
        return len(self.students)
    






