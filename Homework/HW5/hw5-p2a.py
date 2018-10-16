""" Script that prints a formatted string containing name, department,
and phone for all entries in the employee directory.

Jeffrey Liss
jefrey.liss@gmail.com
2018-10-11T12:46:16.886Z
"""


def main():

    e0001 = {'name': 'Ron Swanson',
             'age': 55,
             'department': 'Management',
             'phone': '555-1234',
             'salary': '$87,000'}
    e0002 = {'name': 'Leslie Knope',
             'age': 0,
             'department': 'Middle Management',
             'phone': '555-4321',
             'salary': ''}
    e0003 = {'name': 'Andy Dwyer',
             'age': 0,
             'department': 'Shoe Shining',
             'phone': '555-1122',
             'salary': ''}
    e0004 = {'name': 'April Ludgaye',
             'age': 0,
             'department':
             'Administration',
             'phone': '555-3345',
             'salary': ''}

    # Lol... jk, I never used one of these.
    roladex = [e0001, e0002, e0003, e0004, ]

    for d in roladex:
        print(
            "{0} in the {1} department can be reached at {2}.".format(
                d['name'],
                d['department'],
                d['phone']))


if __name__ == '__main__':
    main()
