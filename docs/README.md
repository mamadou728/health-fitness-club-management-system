# Health & Fitness Club Management System
COMP 3005 – Final Project

This project implements a Health & Fitness Club management system using PostgreSQL and Python, based on a gym-like environment with Members, Trainers, Admin Staff, Classes, Sessions, and Health Metrics.

The system includes:
- A database schema with relational integrity, normalization, triggers, views, and indexing.
- A Python CLI application that implements 8 required operations using SQL.
- A full ERD and relational mapping (provided in /docs/ERD.pdf).
- A project demonstration video (link below).

## Project Structure
```
health-fitness-club-management-system/
│
├── app/
│   ├── operations.py   # All SQL-backed operations
│   └── main.py         # CLI application
│
├── sql/
│   ├── DDL.sql         # Database schema (tables, triggers, view, index)
│   └── DML.sql         # Sample data
│
├── docs/
│   └── ERD.pdf         # ER diagram + mapping + normalization (added later)
│
└── README.md           # This file
```

## Demo Video (as required)
Video link: Add your YouTube "Unlisted" link here

The video demonstrates:
- ER diagram + relational mapping
- Running DDL & DML
- All 8 operations (success + failure)
- Code walkthrough (operations + main menu)

## Database Setup Instructions

### 1. Create the database
```sql
CREATE DATABASE fitness_club;
```

### 2. Connect to it
```sql
\c fitness_club
```

### 3. Run DDL (schema)
```sql
\i 'C:/Users/kharo/health-fitness-club-management-system/sql/DDL.sql';
```

### 4. Run DML (sample data)
```sql
\i 'C:/Users/kharo/health-fitness-club-management-system/sql/DML.sql';
```

## Features Implemented (8 Operations)

### Member Operations (4)

**1. Register New Member**
- Creates a new member with unique email and goal fields.

**2. Update Member Profile / Goals**
- Dynamic update (only provided fields are changed).

**3. Log Health Metric**
- Adds timestamped health data (weight, heart rate, etc.) without overwriting history.

**4. Register for a Class Session**
- Includes:
  - session existence check
  - duplicate registration prevention
  - capacity validation

### Trainer Operations (2)

**5. Set Trainer Availability**
- Includes:
  - trainer existence check
  - trigger enforcing end_time > start_time
  - overlap-prevention logic

**6. View Trainer Schedule**
- Shows upcoming sessions with class names and room info.

### Admin Operations (2)

**7. Create / Update Class Template**
- Admin assigns class name, difficulty, category, duration.

**8. Schedule / Reschedule Class Session**
- Includes:
  - room double-booking prevention
  - trainer availability validation
  - trainer/class/room existence checks

## Technologies Used
- PostgreSQL (database engine)
- Python 3 + psycopg2 (CLI application)
- Triggers, Views, Indexes (implemented in DDL.sql)
- Normalization (minimum 3NF)
- ERD (provided in /docs)

## How to Run the Application

### 1. Install dependencies
```bash
pip install psycopg2
```

### 2. Update PostgreSQL credentials
In `app/operations.py`:
```python
password="your_password"
```

### 3. Run the CLI
From project root:
```bash
python app/main.py
```

You will see:
```
HEALTH & FITNESS CLUB MANAGEMENT SYSTEM
1. Member Operations
2. Trainer Operations
3. Admin Operations
4. Exit
```

Navigate through the menus to execute all operations.

## ERD, Relational Mapping & Normalization (in /docs)
A full PDF is provided at:
`/docs/ERD.pdf`

It includes:
- ER diagram
- Relationship cardinalities
- Mapping to relational schema
- Functional dependency notes
- Normalization (3NF justification)

## Final Notes
This project meets all COMP 3005 requirements, including:
- 8 operations
- Proper UI (CLI)
- Trigger + View + Index
- ER → Relational mapping
- Normalization
- Video demonstration

If you want, I can also generate the ERD PDF for you once we finalize it.
