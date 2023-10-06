from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_students(self, cohhort_id):
        rows = self._connection.execute("SELECT cohorts.id as cohort_id, cohorts.name, cohorts.starting_date, students.id AS student_id, students.name, students.cohort_id " \
                "FROM students JOIN cohorts ON cohorts.id = students.cohort_id " \
                "WHERE cohorts.id = %s", [cohhort_id])
        for row in rows:
                students =[]
                student = Student(row ["student_id"], row["name"], row["cohort_id"])
                students.append(student)
        print(students)
        result = Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students)
        print(result)