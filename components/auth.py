import bcrypt
from init import cursor

global logged_in_user
logged_in_user = ()


def login(email, password):
    print(' ----- Login ----- ')

    user = cursor.execute(
        'SELECT * FROM Users where email=?', (email,)).fetchone()

    if user is None:
        return None

    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, user[5])

    if result:
        update_login(user)
        return user


def update_login(user):
    global logged_in_user
    if logged_in_user == () or logged_in_user == ('test') or user[0] == logged_in_user[0]:
        logged_in_user = user
