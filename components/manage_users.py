import math
import bcrypt
from components.auth import update_login
from main import logged_in_user, cursor, connection


def user_menu():

    while True:
        print('--- User Menu ---')
        print('1. View My Information')
        print('2. View My Competencies')
        if logged_in_user[9] == 2:
            print('3. View All Users')
            print('4. Search Users')
            print('5. Get All Users Competency Report')

            print('Please select an option by number or hit enter to return.')
            response = input()

            if not response:
                break
            if (logged_in_user[9] != 2 and int(response) > 2) or math.isnan(response):
                print('Invalid Option')
                continue
            match int(response):
                case 1:
                    user_info()
                case 2:
                    print('2')
                case 3:
                    get_all_users()
                case 4:
                    print('4')
                case 5:
                    print('5')


def get_all_users():
    users = cursor.execute("SELECT * FROM Users").fetchall()

    print(f'{"ID":<2} {"First Name":<12} {"Last Name":<12} {"Phone":<10} {"Email":<25}')

    for x in users:
        print(
            f'{x[0]:<2} {x[1]:<12} {x[2]:<12} {x[3]:<10} {x[4]:<25}')

    while True:
        print('')
        print(
            'Please enter the ID of the user you would like to edit or hit enter to return')
        response = input()

        if not response:
            break
        if math.isnan(response):
            print('invalid response')
            continue

        user = get_user_by_id(response)
        if user == ():
            print('invalid response')
            continue


def get_user_by_id(id):
    user = cursor.execute('SELECT * FROM Users where id=?', (id)).fetchone()
    if user is not None:
        return user
    else:
        return ()


def user_info(user):
    while True:
        print(f'1. First Name: {user[1]}')
        print(f'2. Last Name: {user[2]}')
        print(f'3. Phone: {user[3]}')
        print(f'4. Email: {user[4]}')
        print('5. Password')

        print('Enter the corresponding number to update the field or hit enter to return to the previous menu.')
        response = input()

        if not response:
            break

        match int(response):
            case 1:
                user[1] = input('Please enter a new First Name: ')
            case 2:
                print('2')
                user[2] = input('Please enter a new Last Name: ')

            case 3:
                print('3')
                user[3] = input('Please enter a new Phone Number: ')

            case 4:
                print('4')
                user[4] = input('Please enter a new Email: ')

            case 5:
                print('5')
                user[5] = hash_password(
                    input('Please enter a new Password: '))
        update_user(user)


def update_user(user):
    query = 'UPDATE Users SET (first_name=?, last_name=?, phone=?, email=?, password=?) WHERE id=?'
    values = (user[1], user[2],
              user[3], user[4], user[5])

    cursor.execute(query, values)
    connection.commit()

    update_login(user)


def create_user(user):

    query = 'INSERT INTO Users (id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type,) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    values = (user.id, user.first_name, user.last_name, user.phone, user.email, user.password,
              user.active, user.date_created, user.hire_date, user.user_type)

    cursor.execute(query, values)

# Utilities - move to user_utils.py?


def hash_password(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
