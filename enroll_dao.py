import sqlite3

class EnrollDataAccess:
    def save(self, enroll):
        with sqlite3.connect("enroll_db.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute("Insert into enrollments (id, name, family, phone_number, enroll_date, class_name, level, "
                           "teacher)" "values (?, ?, ?, ?, ?, ?, ?, ?)",
                           [enroll.id, enroll.name, enroll.family, enroll.phone_number,
                            enroll.enroll_date, enroll.class_name, enroll.level, enroll.teacher]
                           )
            connection.commit()


    def edit(self, enroll):
        with sqlite3.connect("enroll_db.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute("update enrollments set name=?, family=?, phone_number=?, enroll_date=?, class_name=?, "
                           "level=?, teacher=?" "where id=?",
                           [enroll.name, enroll.family,enroll.phone_number, enroll.enroll_date, enroll.class_name,
                            enroll.level, enroll.teacher, enroll.id]
                           )
            connection.commit()

    def remove(self, id):
        with sqlite3.connect("enroll_db.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from enrollments where id=?", [id])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("enroll_db.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from enrollments order by family, name")
            return cursor.fetchall()