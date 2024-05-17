# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   A.Acklen,4/28/2024,Created Script
#   A.Acklen,5/5/2024, Rolled Assignment 03 to Assignment 04
#   A.Acklen,5/15/2024, Rolled Assignment 04 to Assignment 05
#
# ------------------------------------------------------------------------------------------ #
# Import
import os  # Module To Clear Screen
import json

# Define the Data Constants
MENU: str = '\n\
---- Course Registration Program ----\n\
  Select from the following menu: \n\
    1. Register a Student for a Course \n\
    2. Show current data \n\
    3. Save data to a file \n\
    4. Exit the program \n\
-----------------------------------------'
FILE_NAME: str = 'Enrollments.json'
EXPECTED_KEYS = {'FirstName', 'LastName', 'CourseName'}

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
file_obj = None
menu_choice: int = 0
student_data: dict = {} # Single Student Record
students: list = [] # Holds All Student Records


# When the program starts, read the file data into a list of lists (table)
try:
    file_obj = open(FILE_NAME, 'r')
    students = json.load(file_obj)
    if not isinstance(students, list) or not all(isinstance(student, dict) for student in students):
        raise ValueError('The JSON data is not a list of dictionaries')
    for student in students:
        missing_keys = EXPECTED_KEYS - student.keys()
        if missing_keys:
            raise KeyError(f'Missing keys in student data: {missing_keys}')
        extra_keys = student.keys() - EXPECTED_KEYS
        if extra_keys:
            raise KeyError(f'Unexpected keys in student data: {extra_keys}')
    file_obj.close()
except FileNotFoundError:
    print(f'File not found. Creating {FILE_NAME}')
    open(FILE_NAME, 'w')
except Exception as e:
    print('-- Technical Error Message -- ')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file_obj and not file_obj.closed:
        file_obj.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input('What would you like to do: ')
    try:
        menu_choice = int(menu_choice)
    except ValueError:
        print('Please enter a valid number.')

    # Input User Data
    if menu_choice == 1:
        os.system('cls')
        try:
            student_first_name = input('Enter the student\'s first name: ')
            if not student_first_name.isalpha():
                raise ValueError('The first name should not contain numbers.')
            student_last_name = input('Enter the student\'s last name: ')
            if not student_last_name.isalpha():
                raise ValueError('The last name should not contain numbers.')
            course_name = input('Please enter the name of the course: ')
            student_data = {'FirstName': student_first_name,
                            'LastName': student_last_name,
                            'CourseName': course_name}
            students.append(student_data)
            os.system('cls')
            print('-' * 50)
            print('-' * 50 + '\n')
            print(f'{student_first_name} {student_last_name} has been registered for {course_name}! \n')
            print('-' * 50)
            print('-' * 50)
        except ValueError as e:
            print('-' * 50)
            print('-' * 50 + '\n')
            print(e)
            print('-' * 50)
            print('-' * 50)
        # Print The Data
    elif menu_choice == 2:
        os.system('cls')
        print('-'*50)
        print('-' * 50)
        print('The current data is:')
        for student in students:
            print(f'{student['FirstName']},{student['LastName']},{student['CourseName']}')
        print('-' * 50)
        print('-' * 50)

    # Save The Data
    elif menu_choice == 3:
        os.system('cls')
        try:
            file_obj = open(FILE_NAME,'w')
            json.dump(students, file_obj, indent=4)
            file_obj.close()
            print('Data saved successfully.')
            print('Saved Data Summary:')
            for student in students:
                print(f'{student['FirstName']},{student['LastName']},{student['CourseName']}')
        except Exception as e:
            print('Error saving data to file')
            print(e)
        finally:
            if file_obj and not file_obj.closed:
                file_obj.close()
    # Exit Loop
    elif menu_choice == 4:
        os.system('cls')
        print('Good Bye!')
        break

    # Not On The Menu
    else:
        os.system('cls')
        print('\
    \n\
    ----------------------------------------\n\
    Invalid Selecion, Please Select Again!\n\
    -----------------------------------------\n\
    \n ')

# END
