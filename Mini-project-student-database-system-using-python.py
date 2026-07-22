"""
Student Database Management System

A simple Python-based Student Database Management System that uses dictionaries and functions to manage student records. It allows users to add, view, search, and analyze student data through a menu-driven interface with input validation and exception handling.

Features
Add new students with marks
Prevent duplicate student entries
Search students by name
View all student records
Calculate class average
Find highest and lowest scorers (including ties)
Display grades based on marks
Input validation and error handling

Tech Stack: Python, Dictionaries, Functions, Loops, Conditional Statements, Exception Handling

"""

def add_student(students):
    name = str(input("Enter the name of the student to be added : "))
    try :
        marks = int(input(f"Enter the marks of the student {name} :"))
    except ValueError:
        print("Marks must be an integer")
        return students
    
    if name.strip() == "" or marks < 0 or marks > 100 :
        print("Enter a valid name and marks(0 - 100)")
    elif name in students:
        print("Student already exists")
        return students
    else :
        students[name] = marks
    
    return students

def view_students(students):
    
    if len(students) == 0:
        print("No students present in the database")
    else:
        for student,mark in students.items():
            print(f"{student} has scored {mark}")

def search_student(students , name):
    
    if name in students:
        print(f"{name} has scored {students[name]}")
    else:
        print("Student not found")
    

def calculate_average(students):
    
    if len(students) == 0:
        return None
    
    avg = 0
    for mark in students.values():
        avg += mark
    
    avg = avg / len(students)
    
    return avg

def highest_marks(students):
    
    if len(students) > 0 :
        highmark = float('-inf')
    
        for mark in students.values():
            if mark > highmark :
                highmark = mark
                
        return highmark
    else : 
        print("We can't find maximum value in an empty classroom")
    
def lowest_marks(students):
    
    if len(students) > 0 :
        lowmark = float('inf')
    
        for mark in students.values():
            if mark < lowmark :
                lowmark = mark
                
        return lowmark
        
    else:
        print("We can't find minimum value in an empty classroom")

def display_grades(students):
    
    if len(students) > 0 :
        for student,mark in students.items():
            if(mark >= 90):
                print(f"The {student} has scored 'O' grade")
            elif mark<90 and mark>=80 :
                print(f"The {student} has scored 'A+' grade")
            elif mark < 80 and mark >=70:
                print(f"The {student} has scored 'A' grade")
            elif mark < 70 and mark >=60:
                print(f"The {student} has scored 'B+' grade")
            elif mark < 60 and mark >=50:
                print(f"The {student} has scored 'B' grade")
            else:
                print(f"The {student} has failed and scored only {mark}")
    else:
        print("Intialized empty dictionary")


students = {}

print("Student database management system : ")
print("1.Add student" )
print("2.View Student")
print("3.Search student")
print("4.Calculate Average of the whole students ")
print("5.Highest marks of the student")
print("6.Lowest marks of the student")
print("7.Display Grades")
print("8.Exit")
print("\n")
print("\n")

try:
    n = int(input("Enter the number from the menu : "))
except ValueError:
    print("Enter a valid number from the menu")
    n = 0

while(n>0) :
    
    if(n==1):
        add_student(students)
        print(students)
        
        
    elif(n==2):
        view_students(students)
        
        
    elif(n==3):
        name = str(input("Enter the name of the student to be searched :"))
        search_student(students , name)
        
        
    elif(n==4):
        average = calculate_average(students)
        
        if average is None:
            print("No students in the database")
        else:
            print(f"The average of the class : {average:.2f}")
        
    elif(n==5):
        high_marks = highest_marks(students)
        
        if high_marks is not None:
            print(f"The following student(s) scored the highest marks ({high_marks}):")

            for student, mark in students.items():
                if mark == high_marks:
                    print(student)
        
    elif(n==6):
        low_marks = lowest_marks(students)
        
        if low_marks is not None:
            print(f"The following student(s) scored the lowest marks ({low_marks}):")
    
            for student, mark in students.items():
                if mark == low_marks:
                    print(student)
        
    elif(n==7):
        display_grades(students)
        
    elif(n==8):
        
        if len(students) == 0:
            print("No students in the database")
        else:
            print("Before exiting the database students and their marks respectively in the database is :")
            print("Students \t Marks")
            
            for student,mark in students.items():
                print(student + "\t" +str(mark))
        
        break
    
    else:
        print("Enter valid input of N:")
    
    try:
        n = int(input("Enter the number from the menu : "))
    except ValueError:
        print("Enter a valid number from the menu")
        n = 0
