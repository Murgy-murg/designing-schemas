# User stores

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

# Nouns:
students, names, cohorts, starting dates.

# Record --- Properties
students     names, cohorts
cohorts      names, starting dates


# Column types

Table: Students
id: SERIAL
name: text
cohort: text

Table: Cohorts
id: SERIAL 
name: text
starting_date: int

# Can one student have many cohorts ?
NO !
# Can one cohort have many students ?
YES !

A cohort has many students therefore the student belongs to the cohort
The foreign key is on the students table



