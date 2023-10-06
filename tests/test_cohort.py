from lib.cohort import Cohort

def test_constructor():
    cohort = Cohort(1, 'test name', 22/9/1993, 'test_students')
    assert cohort.id == 1
    assert cohort.name == 'test name'
    assert cohort.starting_date == 22/9/1993

def test_equaliser():
    cohort1 = Cohort(1, 'test name', 22/9/1993, 'test_student')
    cohort2 = Cohort(1, 'test name', 22/9/1993, 'test_student')
    assert cohort1 == cohort2

def test_repr():
    cohort = Cohort(1, 'test name', '22/9/1993', 'test_student')
    assert str(cohort) == 'Cohort(test name, 22/9/1993, test_student)'