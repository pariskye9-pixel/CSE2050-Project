import unittest

#from StudentClass import Student
#from CourseClass import Course
#from wholething import University

class test_Student_Class(unittest.TestCase):

    def setUp(self):
        student1_id = "STU00001"
        student1_name = "Student_1"
        
        student1 = Student(student1_id, student1_name)

    def test_init_(self):
        self.assertEqual(self.student1.student1_id, 'STU00001')
        self.assertEqual(self.student1.student1_name, 'Student_1')
        self.assertEqual(self.student1.courses, None)

    def test_enroll(self):
        self.student1.courses['MATH2010'] = 'C+'
        self.assertIn(self.student1.courses['MATH2010'], 'C+')

        self.student1.courses['CSE2050'] = 'B+'
        self.assertIn(self.student1.courses['CSE2050'], 'B+')

    def test_update_grade(self):
        self.student1.courses['MATH2010'] = 'A'
        self.assertIn(self.student1.courses['MATH2010'], 'A')
        
    def test_calculate_gpa(self):
        self.assertEqual(self.student1.calculate_gpa(), 3.65)

    def test_get_courses(self):
        expected_courses = {"MATH2010": "A", "CSE2050": "B+"}
        self.assertEqual(self.student1.get_courses(), expected_courses )


class test_Course_Class(unittest.TestCase):

    def setUp(self):
        course1_code = "CSE2050"
        course1_credits = 2

        test_student = Student("STU00001", "Student_1")

        course1 = Course(course1_code, course1_credits)

    def test__init__(self):
        self.assertEqual(self.course1.course_code, "CSE2050")
        self.assertEqual(self.course1.course_credits, 2)
        self.assertEqual(self.course1.students, None)

    def test_add_students(self):
        self.students.append(self.test_student)
        self.assertIn(self.course1.students, self.test_student)

    def test_get_student_count(self):
        self.assertEqual(self.course1.get_student_count(), 1)

class test_University_Class(unittest.TestCase):

    def setUp(self):

        uni_tester = University()

    def test__init__(self):
        self.assertEqual(self.uni_tester.students, None)
        self.assertEqual(self.uni_tester.courses, None)

    def test_add_course(self):
        self.uni_tester.add_course("CSE1010", 3)
        self.assertIn(self.uni_tester.courses, "CSE1010")

        self.assertRaises(ValueError, self.uni_tester.add_course("CSE1010", 3))

    def test_add_student(self):
        self.uni_tester.add_student("STU00001", "Student_1")
        self.assertIn(self.uni_tester.students, "STU00001")

        self.assertRaises(ValueError, self.uni_tester.add_course("STU00001", "Student_1"))

    def test_get_student(self):
        self.uni_tester.add_student("STU00001", "Student_1")
        self.assertEqual(self.uni_tester.get_student("STU00001"), Student("STU00001", "Student_1") )

        self.assertRaises(ValueError, self.uni_tester.get_student("STU00005"))

    def test_get_course(self):
        self.uni_tester.add_course("CSE1010", 3)
        self.assertEqual(self.uni_tester.get_course("CSE1010"), Course("CSE1010", 3))

        self.assertRaises(ValueError, self.uni_tester.get_student("CSE2050"))

    
unittest.main()



        





    

