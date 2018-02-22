# Written by Denver Risser 1/16/18 - 1/ /18
# Script to average school grades from spreadsheet

### Take care of any necessary imports ###
import csv
from school import  School, Student, Teacher
import tkinter as tk


# Quiz & Test grades Path
qu_path = 'E:\\Documents\\School\\Grades\\Quizes\\Quiz_grades.csv'
test_path = 'E:\\Documents\\School\\Grades\\Tests\\Tests_grades.csv'

# List of the Students Names
students = []
    
# Getting two lists initial lists to make things easier
everything = []
everything_2 = []
quizes = []
    
# Lists for Quiz/Test Nums
quiz_num = []
tests_num = []
    
# Lists for Grades
tests_grades = []
quiz_grades = []
        
# The two final Dicts 
studentQgrades = {}
studentTgrades = {}

###  Open our file to pull our grade averages info ###
with open(qu_path, 'r') as quizgrades, \
    open(test_path, 'r') as testgrades:
    readCSV_quizes = csv.reader(quizgrades, delimiter=',')
    readCSV_tests = csv.reader(testgrades, delimiter=',')
        
    ### Reading from the rows in quizes spreedsheet ###
    for row in readCSV_quizes:
        quizes.append(row[0])
        everything.append(row[1:])
    
    ### Make Master Student List ###
    for person in everything[0]:
        students.append(person)
    
    ### Getting copies of just the info needed ###
    
    quiz_num = quizes[1:]
    quiz_grades = everything[1:]
    
    ######### Start with getting our Stdents:Quiz_grades Dict #########
    
    for student in students:
        studentQgrades[student] = dict.fromkeys(quiz_num, '')
    
    ### Make our Main dict that will store studentQgrades ###

    quiz_counter = 0
    grade_counter = -1
    
    while quiz_counter < (len(quiz_num)-1):
        for student in students:
            quiz_counter = 0
            grade_counter += 1
            for grade in quiz_grades:
                studentQgrades[student][quiz_num[quiz_counter]] = grade[grade_counter]       
                quiz_counter += 1
   
    ######### Next get our Stdents:Text_grades Dict #########
    
    ### Reading from the rows in tests spreedsheet ###
    for row in readCSV_tests:
        everything_2.append(row[1:])
        tests_num.append(row[0])
    
    ### Sorting needed info in variables ###
    test_grades = everything_2[1:]
    test_num = tests_num[1:]

    ### Make our Main dict that will store student_test_grades ###
    for student in students:
        studentTgrades[student] = dict.fromkeys(test_num,'')
    
    ### set a counter for while loop ###
    test_counter = 0   
    grade_counter = -1
    
    ### While loop to combine massive studentTgrades  final dictionary ###
    while test_counter < (len(test_num)-1):
        for student in students:
            test_counter = 0
            grade_counter += 1
            for grade in test_grades:
                studentTgrades[student][test_num[test_counter]] = grade[grade_counter]       
                test_counter += 1
    
    ### Create Student class objects from students list ###
    objs = []
    
    for person in students:
        first, last = person.split(' ')
        vars()[first] = Student(first, last, 11, 'programming')
        objs.append(vars()[first])
    ### Set Student objects grades ###

    for person in students:   
        for test in test_num:
            first, last = person.split(' ')
            vars()[first].set_grades(test,studentTgrades,person)
        for quiz in quiz_num:
            vars()[first].set_grades(quiz,studentQgrades,person)
    Denver = Teacher('Denver', 'Risser', "Mr.Denver", "programming")

    ### Making the GUI ###
    first_q = ['Q1','Q2','T1']
    second_q = ['Q3','Q4','T2']
    third_q = ['Q5','Q6','T3']
    fourth_q = ['Q7','Q8','T4']
    
    
    class GradeManager(tk.Tk):

        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            self.title("Grade Manager")
            self.minsize(400,400)
            self.geometry("600x450")
            self.grid()
            tk.Grid.rowconfigure(self, 0, weight=1)
            tk.Grid.columnconfigure(self, 0, weight=1)
            grade = ''
            for person in objs:
                person.text_Input = tk.StringVar()
    
            av_buttons = Grades(self)
            text_box = Results(self)
    
    
    class Grades(tk.Frame):
        
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            
            self.grid(row=1, column=0, sticky="wn")
            tk.Grid.rowconfigure(self, 0, weight=1)
            tk.Grid.columnconfigure(self, 0, weight=1)

            counter = 0
            ### Making a dict so I can iterate to make multiple Entry Boxes ###
            e = {}
            for x in range(len(objs)):
                e["string{}".format(x)]=int
            
            ### Copying dict e so I can iterate to make multiple Buttons ###
            qb = e.copy()
            qb2 = e.copy()
            qb3 = e.copy()
            qb4 = e.copy()

            l = e.copy()
            while counter < (len(objs)):
                for person in objs:
                    l[counter] = tk.Label(self, font=16, anchor="w", justify='left', text=person.first + ':'). \
                                       grid(row=[counter + 1], column=0, sticky="nsew")
                    e[counter] = tk.Entry(self,font=('arial', 12, 'bold'), width=5, textvariable=person.text_Input, bd= 3,
                                        bg="powder blue", justify='left').grid(row=[counter + 1], column=1)
                    qb[counter] = tk.Button(self, font=16, text="1 Quart", width=5, borderwidth=4, bg='coral', \
                                        command=lambda person=person :person.quart_av(*first_q)). \
                                        grid(row=[counter + 1], column=2)
                    qb2[counter] = tk.Button(self, font=16, text="2 Quart", width=5, borderwidth=4, bg='dim gray', \
                                        command=lambda person=person :person.quart_av(*second_q)). \
                                        grid(row=[counter + 1], column=3)
                    qb3[counter] = tk.Button(self,font=16, text="3 Quart", width=5, borderwidth=4, bg='medium sea green', \
                                        command=lambda person=person :person.quart_av(*third_q)). \
                                        grid(row=[counter + 1], column=4)
                    qb4[counter] = tk.Button(self, font=16, text="4 Quart", width=5, borderwidth=4, bg='dim gray', \
                                        command=lambda person=person :person.quart_av(*fourth_q)). \
                                        grid(row=[counter + 1], column=5)
                    counter += 1

            names_label = tk.Label(self, font=("Helvetica", 18, "bold italic") , fg='red', text="Students:").grid(row=0, column=0, sticky="nsew")
            grade_label = tk.Label(self, font=("Helvetica", 18, "bold italic"), fg='red', text="Grade:").grid(row=0, column=1, sticky="nsew")
            tq_label = tk.Label(self, font=("Helvetica", 18, "bold italic"), fg='red', text="Test & Quizzes:").grid(row=0, column=3, columnspan=3, sticky="nsew")
            
           
    class Results(tk.Frame):
    
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            
            self.grid(row=0, column=0, pady=5, padx=5, sticky="wn")
            tk.Grid.rowconfigure(self, 0, weight=1)
            tk.Grid.columnconfigure(self, 0, weight=1)
            self.grid(row=2, column=0, sticky="nw")
            tk.Grid.rowconfigure(self, 0, weight=1)
            tk.Grid.columnconfigure(self, 0, weight=1)
            text_box = tk.Text(self, height=10, width=52, bd= 5).grid(row=0, column =0)
    
    
    root = GradeManager()
    root.mainloop()
  
   
    #Denver.get_grade(Logan, "T1")
    #print(Denver.classes)
    