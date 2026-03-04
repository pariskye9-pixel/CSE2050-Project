import csv

class Student:
    """Represents an individual student with their courses and attached grades"""


    
    def __init__(self, student_id: str, name: str):
        """Initializes a student object with an id and the students' name"""
        validate_id = student_id.startswith("STU")

        if validate_id == False:
            raise ValueError(f"{student_id} is not a valid ID! Must start with STU")
        elif len(student_id) != 8:
            raise ValueError(f"{student_id} is not a valid ID! Must be 8 characters long!")
        else:
            self.student_id = student_id

        self.name = name
        self.courses = dict()
        self.grade_points = {
            'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D': 1.0, 'F': 0.0
        }
    
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    
    def __hash__(self):
        return hash(self.student_id)
    
    def enroll(self, course, grade: str):
        """Enrolls a student into a course"""
        if grade not in self.grade_points:
            raise ValueError(f"{grade} is not a grade in the system")
        else:
            self.courses[course] = grade
            course.add_student(self)

    
    def update_grade(self, course, grade: str):
        """Updates a students' grade in a course"""
        if grade not in self.grade_points:
            raise ValueError(f"{grade} is not a grade in the system")
        else:
            self.courses[course] = grade

    
    def get_courses(self):
        """Returns all courses a student is enrolled in"""
        return list(self.courses.keys())

    
    def calculate_gpa(self):    
        """Calculates a students overall GPA"""

        total_points = 0
        total_credits = 0

        for course, grade in self.courses.items():
            total_points += self.grade_points[grade] * course.credits
            total_credits += course.credits

        if total_credits == 0:
            return 0

        return total_points / total_credits

    
    def get_course_info(self,):
       """Returns a summary of all the courses a student is taking"""
       all_courses = list()
       for course, grade in self.courses.items():
            all_courses.append(f'Course: {course.course_code}, Grade: {grade}, Credits: {course.credits} \n')
       return all_courses



class Course:
    """Represents a single course and the students in it"""
    
    def __init__(self, course_code: str, credits: int):
        """Initializes a Course object with a code and how many credits for the course"""
        self.course_code = course_code
        self.credits = credits
        self.students = list()

    
    def add_student(self, student: Student):
        """Adds a students to course roster"""
        if student not in self.students:
            self.students.append(student)
    
    
    def get_student_count(self):
        """Counts how many students are in a course"""
        return len(self.students)
 
class University:
    """Stores all students and all courses"""

    
    def __init__ (self):
        """Initializes empty course and student rosters"""
        self.students = {}
        self.courses = {}
    
    
    
    def load_courses_from_csv(self):
        """Load in course information from csv file"""
        with open('course_catalog.csv', 'r') as f:
            data = csv.DictReader(f)
            for line in data:
                course_code = line['course_code']
                credits = int(line['credits'])
                self.add_course(course_code, credits)

    
    
    def load_students_from_csv(self):
        """Load in student information from csv file"""
        with open('university_data.csv', 'r') as f:
            data2 = csv.DictReader(f)
            for line in data2:
                student_id =  line['Student ID']
                name = line['Name']
                All_courses = line['Courses']
                student = self.add_student(student_id, name)
                courses = All_courses.split(';')

                for entry in courses:
                    if entry:
                        course_code, grade = entry.split(':')
                        course = self.get_course(course_code)

                        if course:
                            student.enroll(course, grade)


    
    
    def add_course(self, course_code, credits):
        """Adds a course into course roster"""
        if course_code not in self.courses:
            course = Course(course_code, credits)
            self.courses[course_code] = course
            return self.courses[course_code]
        else: 
            raise ValueError(f"{course_code} is already in the system!")

    
    
    def add_student(self, student_id: str, name: str):
        """Adds a student into student roster"""
        if student_id not in self.students:
            student = Student(student_id, name)
            self.students[student_id] = student
            return self.students[student_id]
        else:
            raise ValueError(f"{student_id} is already in the system!")
    
    
    def get_student(self, student_id: str):
        """Returns a student in system"""
        if student_id not in self.students:
            return None
        return self.students[student_id]
    
    
    def get_course(self, course_code: str):
        """Returns a course in system"""
        if course_code not in self.courses:
            return None
        return self.courses[course_code]

    
    def get_course_enrollment(self, course_code: str):
        """Returns the number of students enrolled in a given course"""
        course = self.courses.get(course_code)
        if course is None:
            raise ValueError(f"{course_code} is not in the system!")
        return course.get_student_count()

    
    def get_students_in_course(self, course_code: str):
        """Returns a list of students enrolled in a given course"""
        course = self.get_course(course_code)
        if course:
            return course.students
        return None

    
    def get_course_stats(self, course_code: str):
        """Returns mean, median, and mode for a course"""

        course = self.get_course(course_code)
        if course is None or not course.students:
            return None

        grade_points = {
            'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D': 1.0, 'F': 0.0
        }

        scores = []

        for student in course.students:
            grade = student.courses.get(course)
            if grade in grade_points:
                scores.append(grade_points[grade])

        if not scores:
            return None
        
        mean = sum(scores) / len(scores)

        scores.sort()
        n = len(scores)
        if n % 2 == 1:
            median = scores[n // 2]
        else:
            median = (scores[n // 2 - 1] + scores[n // 2]) / 2

    
        frequency = {}
        for score in scores:
            frequency[score] = frequency.get(score, 0) + 1

        mode = max(frequency, key=frequency.get)

        return {
            "mean": round(mean, 2),
            "median": round(median, 2),
            "mode": mode
        }
    
    
    def intersect_students(self, course_code1: str, course_code2: str):
        """Print common students in two different courses"""
        course1_students= self.get_students_in_course(course_code1)
        course2_students = self.get_students_in_course(course_code2)
        common_students = set(course1_students) & set(course2_students)
        return list(common_students)

    
    def get_university_gpa_stats(self):
        """Gets mean and median GPA for all students in a university"""
        students_GPAs = []

        for student in self.students.values():
            students_GPAs.append(student.calculate_gpa())

        if not students_GPAs:
            return None

        mean = sum(students_GPAs) / len(students_GPAs)

        students_GPAs.sort()
        n = len(students_GPAs)

        if n % 2 == 1:
            median = students_GPAs[n // 2]
        else:
            median = (students_GPAs[n // 2 - 1] + students_GPAs[n // 2]) / 2

        return {
            "mean": round(mean, 2),
            "median": round(median, 2)
        }
    

    
if __name__ == "__main__":
    u = University() 
    u.load_courses_from_csv()
    u.load_students_from_csv()


    print("Total students:", len(u.students))
    print("Total courses:", len(u.courses))

    student = u.get_student("STU00001")
    print("Student name:", student.name)
    print("GPA:", student.calculate_gpa())
    print("Student courses:", student.get_course_info())

    print("CSE2050 enrollment:", u.get_course_enrollment("CSE2050"))
    
    stats = u.get_course_stats("CSE2050")
    print("CSE2050 statistics:", stats)

    gpa_stats = u.get_university_gpa_stats()
    print("University Student GPA statistics:", gpa_stats)
