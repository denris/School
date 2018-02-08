from math import ceil


class School():
    def __init__(self, school="LVCS"):
        self.school = school


class Student(School):

    
    programming_students = []

    def __init__(self, first, last, grade=None, which_class=None):
        super().__init__()
        self.first = first
        self.last = last
        self.grade = grade
        self.which_class = which_class
        
        if which_class == "programming":
            Student.programming_students.append(self.get_fullname)
        
        
    def set_grades(self, item, dictionary, person):
        vars(self)[item] = dictionary[person][item]
        
    def get_grade(self, grade_number):
        try:
            return float(vars(self)[grade_number])
        except KeyError:
            self.text_Input.set("N/A")

    def quart_av(self, q_num1, q_num2, t_num):
        global grade
        global text_Input
        try:
            quiz_grade = (((self.get_grade(q_num1) + self.get_grade(q_num2))) / 2) / 2
            test_grade = self.get_grade(t_num) / 2
            av = quiz_grade + test_grade
            av = ceil(av)
            grade = str(av)
            self.text_Input.set(grade + '%')
            return av
        except TypeError:
            print("The quarter avarage is not yet available.")
    
    @property
    def get_fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Student({}, {}, {}, {})".format(self.first, self.last, self.grade, self.which_class)

    def __str__(self):
        return '{}, {}, {}'.format(self.get_fullname, self.grade, self.which_class)

class Teacher(Student):

    def __init__(self, first, last, title, classes=None):
        super().__init__(first, last)
        self.title = title
        if classes is None:
            self.classes = []
        else:
            self.classes = classes

    @staticmethod        
    def get_grade(Student, grade_number):
        return print(Student.get_grade(grade_number))