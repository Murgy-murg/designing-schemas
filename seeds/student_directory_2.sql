DROP TABLE IF EXISTS cohorts cascade;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('Maple', '1/1/1999');
INSERT INTO cohorts (name, starting_date) VALUES ('Oak', '1/1/2000');
INSERT INTO cohorts (name, starting_date) VALUES ('Birch', '1/1/2001');

INSERT INTO students(name, cohort_id) VALUES ('Sam', 1);
INSERT INTO students(name, cohort_id) VALUES ('Olivia', 1);
INSERT INTO students(name, cohort_id) VALUES ('George', 3);
INSERT INTO students(name, cohort_id) VALUES ('Will', 2);


