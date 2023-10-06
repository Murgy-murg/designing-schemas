from lib.cohort import Cohort
from lib.student import Student
from lib.cohort_repository import CohortRepository

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    students = repository.find_with_students(3)
    assert students == Cohort(3, 'Birch', '1/1/2001', [Student(3, 'George', 3),]) 