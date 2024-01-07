
from datetime import date
import math
from components.auth import login, logged_in_user
from components.manage_competencies import create_competency, get_all_competencies, view_competencies
from components.manage_users import create_user, hash_password, user_menu
from data.create_schema import create_schema
from models.competency import Competency
from models.user import User
from init import connection


def init():
    create_schema()
    create_user(User(None, 'Parker', 'Gore', 8011234567,
                     'parker.gore@teamsdp.com', hash_password('Password1!'), True, date.today(), date.today(), 2))
    create_user(User(None, 'Dauhson', 'Capps', 8011234567,
                     'dauhson.capps@teamsdp.com', hash_password('Password2!'), True, date.today(), date.today(), 1))

    competency_names = ["Data Types",
                        "Variables",
                        "Functions",
                        "Boolean Logic",
                        "Conditionals",
                        "Loops",
                        "Data Structures",
                        "Lists",
                        "Dictionaries",
                        "Working with Files",
                        "Exception Handling",
                        "Quality Assurance (QA)",
                        "Object-Oriented Programming",
                        "Recursion",
                        "Databases"]

    for x in range(len(competency_names)):
        create_competency(Competency(None, competency_names[x], date.today()))

    connection.commit()


def main_menu():
    global logged_in_user
    if logged_in_user == ():
        login_menu()

    while True:
        print('--- Main Menu ---')
        print('1. View Competencies')
        print('2. View User Info')
        print('3. Logout')
        print('Press enter to exit.')
        response = input()

        if not response:
            break
        elif math.isnan(int(response)):
            print(f'Response of: {response} is not valid')
            continue

        match int(response):
            case 1:
                view_competencies()
            case 2:
                user_menu()
            case 3:
                logged_in_user = ()
                login_menu()

        break


def login_menu():
    print("Please login, to return to the previous menu hit enter instead entering an option.")

    while True:
        # email = input("Please enter your email: ")
        email = 'parker.gore@teamsdp.com'
        if email == '':
            break

        # password = input("Please enter your password:")
        password = 'Password1!'

        if password == '':
            break

        user = login(email, password)

        if user is not None:
            return user

        print('Invalid email or password. Please try again.')


def competency_menu():

    competencies = get_all_competencies()

    print(f'Name')
    for i in range(1, len(competencies)):
        print(f'{1} {competencies[i][1]}')
    print()

    while True:
        print('--- Competency Menu ---')
        print('1. View Competency')
        print('2. Add Competency')
        print('Press enter to return to previous menu.')
        response = input()

        if not response:
            break
        elif math.isnan(response):
            print(f'Response of: {response} is not valid')
            continue

        match int(response):
            case 1:
                print('View')
            case 2:
                print('Add')
            case _:
                print('invalid response')


def assessment_menu(competency_id):
    print()


def assessment_results_menu(assessment_id, user_id):
    print()


def logout():
    logged_in = ()


init()
main_menu()
