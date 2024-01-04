import csv

from models.assessment_results import Assessment_Results


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
            assessment_result = Assessment_Results(
                None, row[0], row[1], row[2], row[3])
            assessment_results.append(assessment_result)

    return assessment_results


assessment_results_list = read_csv_to_model('input.csv')

for ar in assessment_results_list:
    print(vars(ar))
