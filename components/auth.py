import bcrypt
from main import logged_in_user, cursor


def login(email, password):
    print(' ----- Login ----- ')

    user = cursor.execute(
        'SELECT * FROM Users where email=?', (email,)).fetchone()

    if user is None:
        return None

    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, user[5])

    if result:
        return user


def update_login(user):
    global logged_in_user
    if user[0] == logged_in_user[0]:
        logged_in_user = user


def login_menu():
    print("Please login, to return to the previous menu hit enter instead entering an option.")

    while True:
        email = input("Please enter your email: ")
        if email == '':
            break

        password = input("Please enter your password:")
        if password == '':
            break

        user = login(email, password)

        if user is not None:
            return user

        print('Invalid email or password. Please try again.')
