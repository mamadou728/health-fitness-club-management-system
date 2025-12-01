Health & Fitness Club Management System

COMP 3005 – Final Project

This project implements a complete Health & Fitness Club Management System using PostgreSQL and Python.
The system models a real fitness environment with Members, Trainers, Admin Staff, Classes, Class Sessions, Rooms, Availability, Health Metrics, and Registration tracking.

The project includes:

A full ERD (included as docs/ERD.pdf)

Relational Mapping

Normalization up to 3NF

Complete DDL & DML SQL scripts

Python CLI implementing 8 required database operations

Triggers, Views, and Indexing

A demonstration video

This README contains everything the TA needs to understand, run, and evaluate the system.

1. ER Diagram

The full ERD is provided in:

/docs/ERD.pdf


It includes all entities, relationships, cardinalities, and attributes for:

Members

HealthMetric

Trainer

TrainerAvailability

AdminStaff

Class

Room

ClassSession

MemberClassRegistration

The diagram follows standard ER notation and accurately reflects the final schema implemented in SQL.

2. Relational Mapping
Members
Members(
    member_id PK,
    first_name,
    last_name,
    date_of_birth,
    gender,
    email UNIQUE,
    phone,
    goal_target,
    registration_date
)

HealthMetric
HealthMetric(
    metric_id PK,
    member_id FK → Members(member_id),
    metric_type,
    value,
    recorded_at
)

Trainer
Trainer(
    trainer_id PK,
    name,
    email,
    phone,
    specialization
)

TrainerAvailability
TrainerAvailability(
    availability_id PK,
    trainer_id FK → Trainer(trainer_id),
    day_of_week,
    start_time,
    end_time
)

AdminStaff
AdminStaff(
    admin_id PK,
    name,
    email,
    phone,
    title
)

Class
Class(
    class_id PK,
    admin_id FK → AdminStaff(admin_id),
    name,
    description,
    category,
    difficulty,
    duration,
    assigned_since
)

Room
Room(
    room_id PK,
    room,
    location
)

ClassSession
ClassSession(
    session_id PK,
    class_id FK → Class(class_id),
    trainer_id FK → Trainer(trainer_id),
    room_id FK → Room(room_id),
    start_time,
    end_time,
    capacity
)

MemberClassRegistration
MemberClassRegistration(
    registered_id PK,
    member_id FK → Members(member_id),
    session_id FK → ClassSession(session_id),
    registration_date
)

3. Normalization (Up to 3NF)

All tables satisfy:

✔ 1NF

Atomic attributes, no repeating groups.

✔ 2NF

No partial dependencies (all PKs are single-column).

✔ 3NF

No transitive dependencies — every non-key attribute depends only on the primary key.

Normalized tables include:

Members

HealthMetric

Trainer

TrainerAvailability

AdminStaff

Class

Room

ClassSession

MemberClassRegistration

Each table’s full 3NF justification is based on functional dependencies defined by the ERD and included mapping.

4. Project Structure
health-fitness-club-management-system/
│
├── app/
│   ├── main.py
│   ├── operations.py
│   └── __init__.py
│
├── sql/
│   ├── DDL.sql
│   └── DML.sql
│
├── docs/
│   └── ERD.pdf
│
├── requirements.txt
└── README.md   # (this file)


This is the final submission structure.

5. Database Setup Instructions
1. Create the database
CREATE DATABASE fitness_club;

2. Connect to it
\c fitness_club

3. Run DDL (tables, triggers, view, index)
\i 'path/to/sql/DDL.sql';

4. Run DML (sample data)
\i 'path/to/sql/DML.sql';


The DDL includes:

All entities + PK/FK constraints

A trigger ensuring valid time ranges

A view summarizing class session details

An index to improve query performance

6. Python Application
Install dependencies
pip install -r requirements.txt

Configure PostgreSQL credentials

Update inside app/operations.py:

password = "YOUR_PASSWORD"

Run the CLI
python app/main.py


Menu displayed:

HEALTH & FITNESS CLUB MANAGEMENT SYSTEM
1. Member Operations
2. Trainer Operations
3. Admin Operations
4. Exit

7. Implemented Operations (8 Required)
Member Operations

Register a new member

Update member profile / goals

Log health metric (weight, heart rate, etc., timestamped)

Register a member for a class session

Prevents duplicates

Verifies capacity

Ensures session exists

Trainer Operations

Set trainer availability

Trigger enforces valid time ranges

Prevents overlapping availability entries

View trainer schedule

Includes class name, room, session times

Admin Operations

Create / update a class template

Schedule or reschedule a class session

Prevents room double-booking

Validates trainer availability

Ensures class and room exist

All operations use SQL queries executed via psycopg2.

8. Demo Video

Add link here:
YouTube (Unlisted): your link

Video includes:

ERD diagram walkthrough

Relational mapping + normalization summary

Running DDL & DML

Demonstration of all 8 operations

Code overview (main and operations)
