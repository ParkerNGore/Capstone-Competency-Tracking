import csv
from components.manage_assessments import add_results

from models.assessment_results import Assessment_Results
from init import cursor, connection


def write_to_csv(headers, data, filename="output.csv"):
    parent_dir_filename = f"../output/{filename}"

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)


def read_assessment_results(filename):

    assessment_results = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            competency_id = cursor.execute('SELECT id FROM competencies WHERE name = ?', (row[0],)).fetchone()
            assessment_id = cursor.execute('SELECT id FROM assessments WHERE competency_id = ? and name = ?', (competency_id[0], row[1])).fetchone()

            assessment_result = Assessment_Results(
                competency_id, assessment_id, row[3], row[2], row[4], row[5])
            assessment_results.append(assessment_result)
            
        for i in assessment_results:
            print(i)
            add_results(i)
            connection.commit()

    return assessment_results