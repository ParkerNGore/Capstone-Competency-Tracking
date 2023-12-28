

import bcrypt


def create_user(cursor, user):

    query = 'INSERT INTO Users (id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type,) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    values = (user.id, user.first_name, user.last_name, user.phone, user.email, user.password,
              user.active, user.date_created, user.hire_date, user.user_type)

    cursor.execute('INSERT INTO Users (id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (user.id, user.first_name, user.last_name, user.phone, user.email, user.password,
                    user.active, user.date_created, user.hire_date, user.user_type))


def edit_user(cursor, user):
    print()

# Utilities - move to user_utils.py?


def hash_password(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
