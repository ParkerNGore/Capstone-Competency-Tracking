

def create_schema(cursor):
    cursor.execute('''DROP TABLE IF EXISTS Users''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                   user_id INTEGER PRIMARY KEY,
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
