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
        return float(vars(self)[grade_number])

    def Fquart_Qav(self):
        return (self.get_grade('Q1') + self.get_grade('Q2')) / 2
        

    def Fquart_Gav(self):
        return -(-(self.get_grade('T1')) // 2) + -(-self.Fquart_Qav() // 2)
         

    def quarter_av(self):
        pass

    def year_av(self):
        pass

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
        return Student.get_grade(grade_number)