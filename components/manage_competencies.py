
from datetime import date
from distutils.errors import CompileError
from main import cursor


def get_competency_by_id(id):
    competency = cursor.execute(
        'SELECT * FROM Competencies where id=?', (id)).fetchone()
    if competency is not None:
        return competency
    else:
        return ()


def get_competency_w_assessment_results_by_user(user_id, competency_id):
    query = '''
    SELECT * 
    FROM competencies c 
    LEFT JOIN assessments a ON c.id = a.competency_id
    LEFT JOIN assessment_results ar ON a.id = ar.assessment_id
    WHERE ar.user_id = ? and c.id = ?
    '''
    result = cursor.execute(query, (user_id, competency_id)).fetchall()


def get_all_competencies_w_assessment_results_by_user(user_id):
    query = '''
    SELECT * 
    FROM competencies c 
    LEFT JOIN assessments a ON c.id = a.competency_id
    LEFT JOIN assessment_results ar ON a.id = ar.assessment_id
    WHERE ar.user_id = ?
    ORDER BY ar.user_id
    '''
    result = cursor.execute(query, (user_id,)).fetchall()


def get_all_competencies_w_assessment_results_for_all_users():
    query = '''
    SELECT * 
    FROM competencies c 
    LEFT JOIN assessments a ON c.id = a.competency_id
    LEFT JOIN assessment_results ar ON a.id = ar.assessment_id
    ORDER BY ar.user_id
    '''
    result = cursor.execute(query).fetchall()


def create_competency(competency):
    query = 'INSERT INTO Competencies (name, date_created) VALUES (?, ?)'
    values = (competency.name, date.today())

    cursor.execute(query, values)
