from lib.student import Student

def test_constructor():
    student = Student(1,'test name', 2)
    assert student.id == 1
    assert student.name == 'test name'
    assert student.cohort_id == 2

def test_equaliser():
    student1 = Student(1, 'test name', 2)
    student2 = Student(1, 'test name', 2)
    assert student1 == student2

def test_repr():
    student = Student(1, 'test name', 2)
    assert str(student) == 'Cohort(test name, 2)'