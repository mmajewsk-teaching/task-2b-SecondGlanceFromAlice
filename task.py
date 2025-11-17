# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

names = ["Mikayla", "Nicholas", "Alanna", "Donovan", "Elisabeth", "Amari", "Melanie", "Solomon", "Sloan", "Alfredo", "Jaylah", "Gael", "Melanie", "Caspian"]
surnames = ["Gray", "Shaffer", "Wolfe", "Jarvis", "Riley", "Sullivan", "Barber", "Mathews", "Stafford", "Beasley", "Fisher", "Sullivan", "Roach", "Heath", "Fuller", "Wilcox", "Russell", "McCarthy"]
subject = ["math", "physics", "chemistry", "geography"]

class Diary:
    def __init__(self, name, surname, subject, attendance, grade):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.attendance = attendance
        self.grade = grade

    def attendance_check(self, attendance):
        if attendance == 1:
            self.attendance += 1

#diary:
# For one subject
# for various students
# each students have some grades and attendance
# each class a student get attendance, but not neccesarily a grade
# each student should have their own diary, and teacher sees the attendance and average of grades

if __name__ = "__main__":
    Diary(names[0], surnames[0], subject, 1, 2)
    Diary(names[1], surnames[1], subject, 2, 1)
