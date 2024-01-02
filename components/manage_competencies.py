
from main import cursor


def get_competencies(id):
    user = cursor.execute('SELECT * FROM Users where id=?', (id)).fetchone()
    if user is not None:
        return user
    else:
        return ()


def create_competency(competency):
    query = 'INSERT INTO Competencies (id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type,) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    values = (user.id, user.first_name, user.last_name, user.phone, user.email, user.password,
              user.active, user.date_created, user.hire_date, user.user_type)

    cursor.execute(query, values)
