import math
import bcrypt
from components.auth import update_login
from components.manage_assessments import add_results
from components.manage_competencies import get_all_competencies, get_all_competencies_w_assessment_results_for_all_users, get_competency_w_assessment_results_by_user, view_competencies
from init import cursor, connection
from models.assessment_results import Assessment_Results
from utils.csv_utils import read_assessment_results, write_to_csv


def user_menu(logged_in_user):

    while True:
        print('--- User Menu ---')
        print('1. View My Information')
        print('2. View My Competencies')
        if logged_in_user[9] == 2:
            print('3. View All Users')
            print('4. Search Users')
            print('5. Get All Users Competency Report')
            print('6. Import results from CSV')


            print('Please select an option by number or hit enter to return.')
            response = input()

            if not response:
                break
            if (logged_in_user[9] != 2 and int(response) > 2):
                print('Invalid Option')
                continue
            match int(response):
                case 1:
                    user_info(logged_in_user, logged_in_user)
                case 2:
                    view_competencies(logged_in_user)
                case 3:
                    get_all_users(logged_in_user)
                case 4:
                    user_search(logged_in_user)
                case 5:
                    arrange_data()
                case 6:
                    import_data()
                case _:
                    print('invalid response')

def import_data():
    read_assessment_results('input.csv')

def arrange_data():
    results = get_all_competencies_w_assessment_results_for_all_users()
    print(results)
    headers = ['Competency Name', 'Assessment Name', 'Date Taken', 'Score', 'Manager', 'User']
    write_to_csv(headers, results)

def get_all_users(logged_in_user):
    users = cursor.execute("SELECT * FROM Users").fetchall()

    print(f'{"ID":<2} {"First Name":<12} {"Last Name":<12} {"Phone":<10} {"Email":<25}')

    for x in users:
        print(
            f'{x[0]:<2} {x[1]:<12} {x[2]:<12} {x[3]:<10} {x[4]:<25}')

    while True:
        print('')
        print(
            'Please enter the ID of the user you would like to view or hit enter to return')
        response = input()

        if not response:
            break
        if math.isnan(response):
            print('invalid response')
            continue

        user = get_user_by_id(response, logged_in_user)
        if user == ():
            print('invalid response')
            continue

def user_search(logged_in_user):
    while True:
        search_term = input('Enter the first or last name you would like to search by or hit enter to return: ')
        if search_term == '':
            return
        users = search_user_by_first_or_last(search_term)

        if len(users) < 1:
            print('No users found.')
        else:
            for x in users:
                print(f'{x[0]:<2} {x[1]:<12} {x[2]:<12} {x[3]:<10} {x[4]:<25}')
            while True:
                print('')
                print(
                    'Please enter the ID of the user you would like to view or hit enter to return')
                response = input()

                if not response:
                    break

                user = get_user_by_id(response, logged_in_user)
                if user == ():
                    print('invalid response')
                    continue

                user_info(user, logged_in_user)

def search_user_by_first_or_last(search_term):



    query = '''
            SELECT * 
            FROM users 
            WHERE first_name LIKE ? OR last_name LIKE ?
            '''

    return cursor.execute(query, (search_term, search_term)).fetchall()

def get_user_by_id(id, logged_in_user):
    user = cursor.execute('SELECT * FROM Users where id=?', (id)).fetchone()
    if user is not None:
        return user
    else:
        return ()


def user_info(user, logged_in_user):
    while True:
        print(f'1. First Name: {user[1]}')
        print(f'2. Last Name: {user[2]}')
        print(f'3. Phone: {user[3]}')
        print(f'4. Email: {user[4]}')
        print('5. Password')
        if logged_in_user[9] == 2:
            print('6. Assessment Results')

        print('Enter the corresponding number to update the field or hit enter to return to the previous menu.')
        response = input()

        if not response:
            break

        match int(response):
            case 1:
                user[1] = input('Please enter a new First Name: ')
                update_user(user, logged_in_user)
            case 2:
                user[2] = input('Please enter a new Last Name: ')
                update_user(user, logged_in_user)
            case 3:
                user[3] = input('Please enter a new Phone Number: ')
                update_user(user, logged_in_user)
            case 4:
                user[4] = input('Please enter a new Email: ')
                update_user(user, logged_in_user)
            case 5:
                user[5] = hash_password(
                    input('Please enter a new Password: '))
                update_user(user, logged_in_user)
            case 6:
                update_assessment_results(user)

def update_assessment_results(user):
    competencies = get_all_competencies()
    while True:
        for i in range(len(competencies)):
            print(f'{i+1}. {competencies[i]}')

        print('Select a competency to view assessments for.')
        
        competency_response = input()

        if not competency_response:
            break
        if int(competency_response) > len(competency_response):
            print('invalid response')
            continue
        
        assessments = cursor.execute('SELECT * FROM assessments WHERE competency_id = ?', (competency_response,)).fetchall()

        for i in range(len(assessments)):
            print(f'{i+1}. {assessments[i]}')

        print('Select an assessment to add results for.')
        
        assessment_response = input()

        if not assessment_response:
            break
        if int(assessment_response) > len(assessment_response):
            print('invalid response')
            continue

        


        results = get_competency_w_assessment_results_by_user(user[0], competency_response)
        print(results)
        if results is None:
            print('Results are missing. Adding results')
            score = input('What score should be used? (0-4): ')
            date_taken = input('What date was this taken? (yyyy-mm-dd): ')
            manager = input('Enter the manager name who facilitated the test or leave blank: ')
            manager_result = ''
            if manager != '':
                manager_result = cursor.execute('SELECT id from users WHERE first_name = ? and user_type = 2', (manager,))

            if manager_result is None:
                print('manager was not found or user is not a manager. Leaving blank')
                add_results(Assessment_Results(None, assessment_response, score, date_taken, None, user[0]))
                connection.commit()
                return
            else:
                print('manager was not found or user is not a manager. Leaving blank')
                add_results(Assessment_Results(None, assessment_response, score, date_taken, manager_result, user[0]))
                connection.commit()
                return




                

def update_user(user, logged_in_user):
    if logged_in_user[9] == 2 or logged_in_user[0] == user[0]:
        query = 'UPDATE Users SET (first_name=?, last_name=?, phone=?, email=?, password=?) WHERE id=?'
        values = (user[1], user[2],
                  user[3], user[4], user[5])

        cursor.execute(query, values)
        connection.commit()

        update_login(user)
    else:
        print('You do not have permission to edit this user.')
        return


def create_user(user):

    query = 'INSERT INTO Users (first_name, last_name, phone, email, password, active, date_created, hire_date, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    values = (user.first_name, user.last_name, user.phone, user.email, user.password,
              user.active, user.date_created, user.hire_date, user.user_type)

    cursor.execute(query, values)

# Utilities - move to user_utils.py?


def hash_password(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
