
from datetime import date
import math
from components.manage_assessments import view_results
from init import cursor

def get_all_competencies():
    return cursor.execute('SELECT * FROM competencies').fetchall()


def get_competency_by_id(id):
    competency = cursor.execute(
        'SELECT * FROM Competencies where id=?', (id)).fetchone()
    if competency is not None:
        return competency
    else:
        return ()


def get_competency_by_id_with_assessments(id):
    print(id)
    competency = cursor.execute(
        'SELECT * FROM Competencies c LEFT JOIN assessments a ON c.id = a.competency_id where c.id=?', (id,)).fetchall()
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
    SELECT c.name, a.name, ar.date_taken, ar.score, ar.manager_id, ar.user_id 
    FROM competencies c 
    LEFT JOIN assessments a ON c.id = a.competency_id
    LEFT JOIN assessment_results ar ON a.id = ar.assessment_id
    WHERE ar.user_id > 0
    ORDER BY ar.user_id
    '''
    result = cursor.execute(query).fetchall()
    return result


def view_competencies(logged_in_user):
    comeptencies = get_all_competencies()
    while True:
        for i in range(1, len(comeptencies) + 1):
            print(f'{i}. {comeptencies[i - 1][1]}')

        print()
        print('Select the corresponding number to view Competency or hit enter to return')

        response = input()

        if not response:
            break
        elif math.isnan(int(response)):
            print(f'Response of: {response} is not valid')
            continue

        view_competency_w_assessments(comeptencies[int(response) - 1][0], logged_in_user)


def view_competency_w_assessments(id, logged_in_user):
    competency_with_assessments = get_competency_by_id_with_assessments(id)
    print(competency_with_assessments)
    while True:
        print(competency_with_assessments[0][1])
        print(f'Name Date Created')
        for i in range(len(competency_with_assessments)):
            print(f'{i+1}. {competency_with_assessments[i][5]} {competency_with_assessments[i][6]}')

        print()
        print('Select a number to view your results or hit enter to return')
        response = input()

        if not response:
            break
        elif math.isnan(int(response)):
            print(f'Response of: {response} is not valid')
            continue
        view_assessment_results(int(response), logged_in_user[0])

def view_assessment_results(id, user_id):
    print(view_results(id, user_id))

def create_competency(competency):
    query = 'INSERT INTO Competencies (name, date_created) VALUES (?, ?)'
    values = (competency.name[0], date.today())

    cursor.execute(query, values)
