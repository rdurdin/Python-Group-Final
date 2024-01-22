# ----------------------------------------------------------------
# Author: Fernando Cartagena
# Date: 11/15/2023
#

# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------
# ------------------------------------------------------------


# This function displays all the courses, indicates which ones
# in which the student is enrolled, and counts the courses a
# student has registered for. It has two parameters: s_id is the
# ID of the student; c_roster is the list of class rosters.
# This function has no return value.
# -------------------------------------------------------------
def list_courses(s_id, c_roster):
    # Display all courses, indicating which ones the student is enrolled in
    enrolled_courses = [course for course, students in c_roster.items() if s_id in students]

    print(f"Student {s_id} is enrolled in the following courses:")
    for course in c_roster:
        if course in enrolled_courses:
            print(f"- {course} (Enrolled)")
        else:
            print(f"- {course}")

    print(f"Total number of courses: {len(c_roster)}")
    print(f"Number of courses enrolled: {len(enrolled_courses)}")


# ------------------------------------------------------------
# This function adds a student to a course.  It has three
# parameters: s_id is the ID of the student to be added; c_roster is the
# list of class rosters; c_max_size is the list of maximum class sizes.
# This function asks user to enter the course he/she wants to add.
# If the course is not offered, display error message and stop.
# If student has already registered for this course, display
# error message and stop.
# If the course is full, display error message and stop.
# If everything is okay, add student ID to the course’s
# roster and display a message if there is no problem.  This
# function has no return value.
# -------------------------------------------------------------
def add_course(s_id, c_roster, c_max_size):
    # Ask the user to enter the course to add
    course_to_add = input("Enter the course to add: ")

    # Check if the course is offered
    if course_to_add not in c_roster:
        print("Error: Course not offered.")
        return

    # Check if the student is already enrolled in the course
    if s_id in c_roster[course_to_add]:
        print("Error: Student is already enrolled in this course.")
        return

    # Check if the course is full
    if len(c_roster[course_to_add]) >= c_max_size[course_to_add]:
        print("Error: Course is full.")
        return

    # Add student ID to the course's roster
    c_roster[course_to_add].append(s_id)
    print(f"Student {s_id} has been successfully added to {course_to_add}.")


# ------------------------------------------------------------
# This function drops a student from a course.  It has two
# parameters: s_id is the ID of the student to be dropped;
# c_roster is the list of class rosters. This function asks
# the user to enter the course he/she wants to drop.  If the course
# is not offered, display error message and stop.  If the student
# is not enrolled in that course, display error message and stop.
# Remove student ID from the course’s roster and display a message
# if there is no problem.  This function has no return value.
# -------------------------------------------------------------

def drop_course(s_id, c_roster):
    # Ask the user to enter the course to drop
    course_to_drop = input("Enter the course to drop: ")

    # Check if the course is offered
    if course_to_drop not in c_roster:
        print("Error: Course not offered.")
        return

    # Check if the student is enrolled in the course
    if s_id not in c_roster[course_to_drop]:
        print("Error: Student is not enrolled in this course.")
        return

    # Remove student ID from the course's roster
    c_roster[course_to_drop].remove(s_id)
    print(f"Student {s_id} has been successfully dropped from {course_to_drop}.")
