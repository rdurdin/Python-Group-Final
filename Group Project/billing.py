#
#   James Ferez
#   Module for printing bill of registered courses
#   for the student logged in.
#
#

from datetime import datetime as dt


def display_bill(s_id, s_in_state, c_rosters, c_hours):
    ######## Variables ########
    cth = {}
    registered_c = {}
    h_total = 0
    p_total = 0
    date = dt.now()
    f_date = date.strftime(f'%b %d, %Y at %I:%M %p')
    course_count = {'CSC101': 0,
                    'CSC102': 0,
                    'CSC103': 0,
                    'CSC104': 0,
                    'CSC105': 0}
    if s_in_state[s_id]:
        s_type = 'In-State Student'
        c_price = 225
    else:
        s_type = 'Out-of-State Student'
        c_price = 850

    ######## Create Course Count dict for student ########
    for course in c_rosters:
        for student in c_rosters[course]:
            if student == s_id:
                course_count[course] += 1

    ######## Remove courses not registered for ########
    for course in course_count:
        course_count[course] *= c_hours[course]
        if int(course_count[course]) > 0:
            registered_c[course] = course_count[course]

    ######## Combine two dicts into one dict with total credit hours and price ########
    for course, hours in registered_c.items():
        cch = []
        cost = int(hours) * c_price
        cch.append(cost)
        cch.append(registered_c[course])
        cth[course] = cch

    ######## Print Bill ########
    print(f'Tuition Summary\n'
          f'Student: {s_id}, {s_type}\n'
          f'{f_date}')
    print(f'Course    Hours     Cost    ')
    print(f'------    -----   ---------')
    for course, items in cth.items():
        print(f'{course}    {items[1]:>5}   ${items[0]:>8.2f}')
        h_total += int(items[1])
        p_total += int(items[0])
    print(f'        -------   ---------\n'
          f'Total     {h_total:>5}   ${p_total:>8.2f}')