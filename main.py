
from datetime import date
import sqlite3
from components.auth import login_menu
from components.manage_users import create_user, hash_password
from data.create_schema import create_schema
from models.user import User

# Database
connection = sqlite3.connect("capstone.db")
cursor = connection.cursor()


# Variables
logged_in_user = {}


def init():
    create_schema(cursor)
    create_user(cursor, User(1, 'Parker', 'Gore', 8011234567,
                             'parker.gore@teamsdp.com', hash_password('Password1!'), True, date.today(), date.today(), 2))
    create_user(cursor, User(2, 'Dauhson', 'Capps', 8011234567,
                             'dauhson.capps@teamsdp.com', hash_password('Password2!'), True, date.today(), date.today(), 1))
    connection.commit()


def main_menu():

    if logged_in_user == {}:
        login_menu(cursor)

    # if logged_in_user[9] == 2:

    while True:
        print('main menu')
        break


def logout():
    logged_in = {}


init()
main_menu()
