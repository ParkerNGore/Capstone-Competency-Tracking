
from main import cursor


def get_competencies(id):
    user = cursor.execute('SELECT * FROM Users where id=?', (id)).fetchone()
    if user is not None:
        return user
    else:
        return ()
