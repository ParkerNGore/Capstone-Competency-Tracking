from init import cursor, connection

from datetime import date


def add_assessment(assessment, competency_id):
    query = '''
            INSERT INTO assessments (competency_id, name, date_created)
            VALUES (?, ?, ?)
            '''
    values = (assessment[1], assessment[2], date.today())

    cursor.execute(query, values)


def add_results(assessment_results):
    query = '''
            INSERT INTO assessment_results (assessment_id, score, date_taken, manager_id)
            VALUES (?, ?, ?)
            '''
    values = (assessment_results[1], assessment_results[2],
              assessment_results[3], assessment_results[4])

    cursor.execute(query, values)


def edit_assessment(assessment):
    query = '''
            UPDATE assessments
            SET name = ?, date_created = ?, competency_id = ?
            WHERE id = ?
            '''
    cursor.execute(
        query, (assessment[1], assessment[2], assessment[3], assessment[0]))
    connection.commit()


def edit_results(assessment_results):
    query = '''
        UPDATE assessment_results
        SET assessment_id = ?, score = ?, date_taken = ?, manager_id = ?
        WHERE id = ?
        '''
    cursor.execute(query, (assessment_results[1], assessment_results[2],
                   assessment_results[3], assessment_results[4], assessment_results[0]))
    connection.commit()


def delete_result_by_id(id):
    cursor.execute('DELETE FROM assessment_results WHERE id = ?', id)
    connection.commit()
