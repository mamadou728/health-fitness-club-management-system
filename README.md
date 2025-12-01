# Health & Fitness Club Management System

**COMP 3005 – Final Project**

A complete Health & Fitness Club Management System built with PostgreSQL and Python. This system models a real fitness environment with comprehensive management of members, trainers, administrators, classes, sessions, and health tracking.

## Table of Contents

- [Features](#features)
- [System Components](#system-components)
- [ER Diagram](#er-diagram)
- [Relational Schema](#relational-schema)
- [Normalization](#normalization)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Implemented Operations](#implemented-operations)
- [Demo Video](#demo-video)

## Features

- Full relational database design with ERD
- Normalized to 3NF
- Complete DDL & DML SQL scripts
- Python CLI with 8 core database operations
- Database triggers for data validation
- Views and indexes for performance optimization
- Comprehensive health metrics tracking
- Class registration and scheduling system

## System Components

The system includes the following key entities:

- **Members**: User profiles with goals and personal information
- **HealthMetric**: Timestamped health tracking (weight, heart rate, etc.)
- **Trainer**: Training staff with specializations
- **TrainerAvailability**: Scheduling and availability management
- **AdminStaff**: Administrative personnel
- **Class**: Fitness class templates with categories and difficulty levels
- **Room**: Facility rooms and locations
- **ClassSession**: Scheduled class instances
- **MemberClassRegistration**: Member enrollment tracking

## ER Diagram

The complete Entity-Relationship Diagram is available at:

```
/docs/ERD.pdf
```

The diagram follows standard ER notation and includes all entities, relationships, cardinalities, and attributes that reflect the implemented SQL schema.

## Relational Schema

### Members
```sql
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
```

### HealthMetric
```sql
HealthMetric(
    metric_id PK,
    member_id FK → Members(member_id),
    metric_type,
    value,
    recorded_at
)
```

### Trainer
```sql
Trainer(
    trainer_id PK,
    name,
    email,
    phone,
    specialization
)
```

etc...

## Normalization

All tables are normalized to **Third Normal Form (3NF)**:

### First Normal Form (1NF)
- All attributes contain atomic values
- No repeating groups

### Second Normal Form (2NF)
- Satisfies 1NF
- No partial dependencies

### Third Normal Form (3NF)
- Satisfies 2NF
- No transitive dependencies
- Every non-key attribute depends only on the primary key

## Project Structure

```
health-fitness-club-management-system/
│
├── app/
│   ├── main.py              # Main application entry point
│   ├── operations.py        # Database operations implementation
│   └── __init__.py
│
├── sql/
│   ├── DDL.sql             # Data Definition Language (schema)
│   └── DML.sql             # Data Manipulation Language (sample data)
│
├── docs/
│   └── ERD.pdf             # Entity-Relationship Diagram, Relational Mapping and Normalization
│
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Setup Instructions

### 1. Create the Database

```sql
CREATE DATABASE fitness_club;
```

### 2. Connect to the Database

```sql
\c fitness_club
```

### 3. Run DDL Script

Execute the Data Definition Language script to create tables, triggers, views, and indexes:

```sql
\i 'path/to/sql/DDL.sql';
```

The DDL includes:
- All entity tables with primary and foreign key constraints
- Trigger for validating time ranges
- View for summarizing class session details
- Index for query performance optimization

### 4. Run DML Script

Load sample data:

```sql

\i 'C:/Users/kharo/OneDrive/Bureau/health-fitness-club-management-system/sql/DML.sql';

```

## Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Application

```bash
python app/main.py
```

### Menu Interface

```
HEALTH & FITNESS CLUB MANAGEMENT SYSTEM
1. Member Operations
2. Trainer Operations
3. Admin Operations
4. Exit
```

## Implemented Operations

### Member Operations

1. **Register a New Member**
   - Create member profiles with personal information and fitness goals

2. **Update Member Profile/Goals**
   - Modify member information and goal targets

3. **Log Health Metric**
   - Record timestamped health data (weight, heart rate, etc.)

4. **Register for Class Session**
   - Enroll members in scheduled classes
   - Prevents duplicate registrations
   - Verifies session capacity
   - Validates session existence

### Trainer Operations

5. **Set Trainer Availability**
   - Define trainer schedule by day and time
   - Trigger enforces valid time ranges
   - Prevents overlapping availability entries

6. **View Trainer Schedule**
   - Display complete schedule with class names, rooms, and session times

### Admin Operations

7. **Create/Update Class Template**
   - Manage class definitions with categories, difficulty levels, and descriptions

8. **Schedule/Reschedule Class Session**
   - Create or modify class session schedules
   - Prevents room double-booking
   - Validates trainer availability
   - Ensures class and room exist

All operations use parameterized SQL queries executed via `psycopg2` for security and performance.

## Demo Video

YouTube : `your_link_here`

### Video Contents:
- ERD diagram walkthrough
- Relational mapping and normalization summary
- DDL and DML execution demonstration
- Complete demonstration of all 8 operations
- Code overview (main.py and operations.py)
