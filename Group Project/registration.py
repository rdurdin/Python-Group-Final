# ----------------------------------------------------------------
# Author: Raegan Durdin
# Date: 11/07/2023
#

# This module implements everything from the student and billing modules
# into a working program. Students may log in and choose whether to add,
# drop, or list the students courses, or show the student bill.
# ----------------------------------------------------------------------

import student
import sys
import billing

# Main function. Provides interactive interface for students and holds all
# the information needed including a list of students, in state students,
# course hours, course roster, and max size of courses. Allows the student
# to login and choose between functions.
# ------------------------------------------------------------------------
def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}

    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

    program_exit = False
    while not program_exit:
        # Checks for valid student id and password until one is given
        valid_id = False
        student_id = 0
        while not valid_id:
            input_id = input("Enter Student ID, or 0 to quit: ")
            # if input is 0, exit out of program
            if input_id == '0':
                sys.exit()
            student_id = input_id
            if login(input_id, student_list):
                valid_id = True
                break
            print("Invalid Student ID or Password")

        # Once logged in proceeds to action menu
        logout = False
        while not logout:
            # Shows the menu and asks for student input
            show_menu()
            student_input = input("What do you want to do: ")

            # adds a course
            if student_input == '1':
                student.add_course(student_id, course_roster, course_max_size)

            # drops a course
            elif student_input == '2':
                student.drop_course(student_id, course_roster)

            # lists student courses
            elif student_input == '3':
                student.list_courses(student_id, course_roster)

            # lists bill information
            elif student_input == '4':
                billing.display_bill(student_id, student_in_state, course_roster, course_hours)

            # logs out of program
            elif student_input == '0':
                logout = True

            # provides appropriate feedback with wrong choices
            else:
                print("Invalid Choice")

        # Shows that student has successfully broken out of while loop and logged out correctly
        print("Student successfully logged out")
        print("")


# Function to show the menu that students can choose from.
# ------------------------------------------------------------------------
def show_menu():
    print("")
    print("Action Menu")
    print("-----------")
    print("1: Add course")
    print("2: Drop course")
    print("3: List courses")
    print("4: Show bill")
    print("0: Logout")


# Function that allows the user to input a password and returns either
# true or false depending on whether the student id is valid and the
# student password. Two parameters include student_id which is the
# input the student gave for their id, and s_list which is a list of
# students and their passwords.
# ------------------------------------------------------------------------
def login(student_id, s_list):
    # Asks for student password, verifies if correct

    input_pin = input("Enter Student Password: ")
    for students in s_list:
        if student_id == students[0]:
            if input_pin == students[1]:
                print("Login successful")
                return True
            else:
                return False

    return False


main()
