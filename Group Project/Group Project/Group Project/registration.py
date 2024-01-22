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



    # Checks for valid student id and password
    valid_id = False
    while valid_id == False:
        input_id = input("Enter student ID: ")
        for students in student_list:
            if input_id == students[0]:
                if login(students[1], student_list):
                    valid_id = True;
                    break
                
    
    # Once logged in proceeds to action menu
    show_menu()

def show_menu():
    print("Action Menu")
    print("-----------")
    print("1: Add course")
    print("2: Drop course")
    print("3: List courses")
    print("4: Show bill")
    print("0: Logout")
    print("What do you want to do?")

def login(id, s_list):
    # Asks for student password, verifies if correct
    valid_id = False
    
    input_pin = input("Enter student pin: ")
    for students in s_list:
        if input_pin == id:
            print("Login successful")
            return True
        else:
            return False

main()