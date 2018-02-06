# Written by Denver Risser 1/16/18 - 1/ /18
# Script to average school grades from spreadsheet

### Take care of any necessary imports ###
import csv
from school import  School, Student, Teacher
from tkinter import *



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
with open('E:\\Documents\\School\\Grades\\Quizes\\Quiz_grades.csv', 'r') as quizgrades, \
    open('E:\\Documents\\School\\Grades\\Tests\\Tests_grades.csv', 'r') as testgrades:
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
    
    
    root = Tk()
    grade = ''
    for person in objs:
        person.text_Input = StringVar()
    
    
    class Buttons():
        
        def __init__(self, master):
            frame = Frame(root)
            frame.grid(sticky=N+S+E+W)
            
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
                    l[counter] = Label(frame, anchor=W, text=person.first + ':').grid(row=[counter], column=0, stick=N+S+E+W)
                    e[counter] =Entry(frame,font=('arial', 12, 'bold'),width=5, textvariable=person.text_Input, bd= 3,
                                        bg="powder blue", justify='left').grid(row=[counter], column=1, stick=N+S+E+W)
                    qb[counter] = Button(frame, text="1 Quart", width=5, borderwidth=4, bg='coral', \
                                        command=lambda person=person :person.quart_av(*first_q)).grid(row=[counter], column=2, sticky=N+S+E+W)
                    qb2[counter] = Button(frame, text="2 Quart", width=5, borderwidth=4, bg='dim gray', \
                                        command=lambda person=person :person.quart_av(*second_q)).grid(row=[counter], column=3, sticky=N+S+E+W)
                    qb3[counter] = Button(frame, text="3 Quart", width=5, borderwidth=4, bg='medium sea green', \
                                        command=lambda person=person :person.quart_av(*third_q)).grid(row=[counter], column=4, sticky=N+S+E+W)
                    qb4[counter] = Button(frame, text="4 Quart", width=5, borderwidth=4, bg='dim gray', \
                                        command=lambda person=person :person.quart_av(*fourth_q)).grid(row=[counter], column=5, sticky=N+S+E+W)
                    counter += 1
        

        
    root.title("Grade Manager")
    root.minsize(300,300)
    root.geometry("800x600")
    root.grid()
    av_button = Buttons(root)
    
    root.mainloop()
  
   
    #Denver.get_grade(Logan, "T1")
    #print(Denver.classes)
    