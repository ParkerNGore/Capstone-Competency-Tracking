class User:
    def __init__(self, user_id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.active = active
        self.date_created = date_created
        self.hire_date = hire_date
        self.user_type = user_type
