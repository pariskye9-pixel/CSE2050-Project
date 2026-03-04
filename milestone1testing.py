import unittest

from wholething import University, Student, Course


class test_Student_Class(unittest.TestCase):

    def setUp(self):
        student1_id = "STU00001"
        student1_name = "Student_1"
        
        self.student1 = Student(student1_id, student1_name)
        self.test_course1 = Course("MATH2010", 3 )
        self.test_course2 = Course("CSE1010", 3 )

    def test_init_(self):
        self.assertEqual(self.student1.student_id, 'STU00001')
        self.assertEqual(self.student1.name, 'Student_1')
        self.assertEqual(self.student1.courses, dict())

    
    def test_not_valid_id(self):
        #ensure ID is correctly formatted for STU and length
        self.assertRaises(ValueError, Student, "MIAMI000", "Invalid")
        self.assertRaises(ValueError, Student, "MIAMI", "Invalid")

    def test_enroll(self):
        
        #enroll student in courses
        self.student1.enroll(self.test_course1, 'C+')
        self.student1.enroll(self.test_course2, 'B+')

        #assert that student was enrolled in courses dictionary
        self.assertIn(self.test_course1, self.student1.courses)
        self.assertIn(self.test_course2, self.student1.courses)

        #assert grade and course in dictionary match
        self.assertEqual(self.student1.courses[self.test_course1], 'C+')
        self.assertEqual(self.student1.courses[self.test_course2], 'B+')

    def test_invalid_grades(self):
        #assert grade is only in grade point system
        with self.assertRaises(ValueError):
            self.student1.enroll(self.test_course1, "AA")
        
    def test_update_grade(self):
        
        #enroll student in course
        self.student1.enroll(self.test_course1, 'C+')

        #update grade and assert value was changed
        self.student1.update_grade(self.test_course1, 'A')
        self.assertEqual(self.student1.courses[self.test_course1], 'A')

    def test_invalid_updated_grades(self):
        self.student1.enroll(self.test_course1, 'C+')

        #assert grade is only in grade point system
        with self.assertRaises(ValueError):
            self.student1.update_grade(self.test_course1, "AA")
        
    def test_calculate_gpa(self):

        #ensure gpa is 0 with no courses
        self.assertEqual(self.student1.calculate_gpa(), 0)
        
        #enroll student in two courses
        self.student1.enroll(self.test_course1, 'C+')
        self.student1.enroll(self.test_course2, 'B+')

        #ensure gpa is equivalent to hard coded value
        self.assertEqual(self.student1.calculate_gpa(), 2.8)
        
    
    def test_get_courses(self):
        
        #enroll student in course
        self.student1.enroll(self.test_course1, 'C+')
        self.student1.enroll(self.test_course2, 'B+')

        #assert students courses align with what they have been enrolled in
        expected_courses = {self.test_course1: "C+", self.test_course2: "B+"}
        self.assertEqual(self.student1.get_courses(), expected_courses )

    def test_get_course_info(self):
        self.student1.enroll(self.test_course1, 'A-')

        tested_course1_info = self.student1.get_course_info()

        #finish this



class test_Course_Class(unittest.TestCase):

    def setUp(self):
        course1_code = "CSE2050"
        course1_credits = 2

        self.test_student = Student("STU00001", "Student_1")

        self.course1 = Course(course1_code, course1_credits)

    def test__init__(self):
        self.assertEqual(self.course1.course_code, "CSE2050")
        self.assertEqual(self.course1.credits, 2)
        self.assertEqual(self.course1.students, list())


    def test_get_student_count(self):

        #empty course
        self.assertEqual(self.course1.get_student_count(), 0)

        #assert that adding a student increases student count
        self.course1.add_student(self.test_student)
        self.assertEqual(self.course1.get_student_count(), 1)


    def test_add_students(self):

        self.course1.add_student(self.test_student)
        self.assertIn(self.test_student, self.course1.students)

        #assert duplicates are not added
        self.course1.add_student(self.test_student)
        self.assertEqual(self.course1.get_student_count, 1)

class test_University_Class(unittest.TestCase):

    def setUp(self):

        self.uni_tester = University()

    def test__init__(self):
        self.assertEqual(self.uni_tester.students, dict())
        self.assertEqual(self.uni_tester.courses, dict())

    def test_add_course(self):

        #ensure courses can be added and will appear in courses dictionary
        self.uni_tester.add_course("CSE1010", 3)
        self.assertIn("CSE1010",self.uni_tester.courses)
        
        #make sure duplicates are raising errors
        self.assertRaises(ValueError, self.uni_tester.add_course, "CSE1010", 3)

    def test_add_student(self):

        #ensure students can be added and will appear in student dictionary
        self.uni_tester.add_student("STU00001", "Student_1")
        self.assertIn("STU00001", self.uni_tester.students)

        #make sure duplicates are raising errors
        self.assertRaises(ValueError, self.uni_tester.add_student, "STU00001", "Student_1")

    def test_get_student(self):

        self.uni_tester.add_student("STU00001", "Student_1")
        tester_student = self.uni_tester.get_student("STU00001")

        #test that student can be returned from student dictionary system
        self.assertEqual(tester_student.student_id, "STU00001" )

        #test for none if student not in system
        self.assertIsNone(self.uni_tester.get_student("STU00006"))

    def test_get_course(self):

        self.uni_tester.add_course("CSE1010", 3)
        tester_course = self.uni_tester.get_course("CSE1010")

        #test that course can be returned from course dictionary system
        self.assertEqual(tester_course.course_code, "CSE1010")

        #test for none if course not in system
        self.assertIsNone(self.uni_tester.get_course("CSE2050"))

    # TODO: def test_interesect_students(self):

    # TODO: def test_get_course_enrollment(self):

    # TODO def test_get_course_stats(self):

    # TODO: def test_get_students_in_course(self):

    # TODO: gpa stats wait for paris





    
if __name__ == "__main__":
    unittest.main()


        





    

