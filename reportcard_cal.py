# Written by Denver Risser 1/16/18 - 1/ /18
# Script to average school grades from spreadsheet

### Take care of any necessary imports ###
import csv
from students import Student, School

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
    
    ''' Start with getting our Stdents:Quiz_grades Dict '''
    
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
   
    ''' Next get our Stdents:Text_grades Dict '''
    
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
    
    ''' Make Students Objects to simplifiy calculations '''
    
    ### Create Student class objects from students list ###
    for person in students:
        first, last = person.split(' ')
        vars()[first] = Student(first, last, 11, 'programming')
    
    ### Set Student objects grades ###
    for person in students:   
        for test in test_num:
            first, last = person.split(' ')
            vars()[first].set_grades(test,studentTgrades,person)
        for quiz in quiz_num:
            vars()[first].set_grades(quiz,studentQgrades,person)

    
    print(Stephanie.school)
