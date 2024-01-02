from main import cursor


def create_schema():
    cursor.execute('''DROP TABLE IF EXISTS Users''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   phone TEXT
                    CHECK(length(phone) >= 10),
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL,
                   active BOOLEAN DEFAULT 1,
                   date_created TEXT,
                   hire_date TEXT,
                   user_type INTEGER
                    CHECK(user_type == 1 OR user_type == 2)
    )''')

    cursor.execute('''DROP TABLE IF EXISTS Competencies''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Competencies(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   date_created TEXT NOT NULL
    )''')

    cursor.execute('''DROP TABLE IF EXISTS Assessments''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Assessments(
                   id INTEGER PRIMARY KEY,
                   competency_id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   date_created TEXT NOT NULL,
                   FOREIGN KEY (competency_id)
                    REFERENCES Competencies (id)
    )''')

    cursor.execute('''DROP TABLE IF EXISTS Assessment_Results''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Assessment_Results(
                   id INTEGER PRIMARY KEY,
                   assessment_id INTEGER NOT NULL,
                   user_id INTEGER NOT NULL,
                   date_taken TEXT NOT NULL,
                   score INT NOT NULL,
                   FOREIGN KEY (assessment_id)
                    REFERENCES Assessments (id),
                   FOREIGN KEY (user_id)
                    REFERENCES Users (id)
    )''')
