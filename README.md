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
├── prefilled/
│   ├── prefilled_data.py         # Pre-filled test data
│   ├── prefilled_operations.py   # Pre-filled operation wrappers
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

### Run the CLI: 

```sql
psql -U postgres
```

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
\i 'C:/Users/kharo/OneDrive/Bureau/health-fitness-club-management-system/sql//DDL.sql';
```

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

### Testing with Pre-filled Data

Each operation offers two modes:
1. **Manual Entry** - Enter data interactively
2. **Pre-filled Data** - Automatically tests both SUCCESS and FAILURE cases

Every prefilled operation demonstrates:
- ✅ **SUCCESS CASE**: Valid data that executes successfully
- ❌ **FAILURE CASE**: Invalid data to show error handling

## Pre-filled Data System

### Purpose
The `prefilled/` directory provides automated testing data to quickly demonstrate all operations without manual input. This system is designed for rapid testing and demonstration of the application's functionality.

### Why Pre-filled Data?
- **Fast Testing**: Instantly test all 8 operations with a single selection
- **Success & Failure Cases**: Each operation demonstrates both valid and invalid scenarios
- **Consistency**: Same test data across all demonstrations ensures reproducible results
- **Error Handling Demo**: Shows how the system gracefully handles bad data
- **Database Features**: Specifically designed to showcase INDEX, TRIGGER, and VIEW functionality

### Structure
```
prefilled/
├── prefilled_data.py         # Test data for all operations (SUCCESS/FAILURE pairs)
├── prefilled_operations.py   # Wrapper functions that execute operations with test data
└── __init__.py
```

### How It Works
1. **Data Definition** (`prefilled_data.py`): Contains dictionaries with test data for each operation
   - Each operation has two data sets: `*_SUCCESS` and `*_FAILURE`
   - Data is based on existing records in `DML.sql` for consistency

2. **Operation Wrappers** (`prefilled_operations.py`): Functions that call actual operations with prefilled data
   - Each wrapper runs both SUCCESS and FAILURE tests automatically
   - Displays what data is being used before execution
   - Shows clear results for both cases

3. **Integration** (`main.py`): Menu system offers prefilled option for every operation
   - User selects "2. Pre-filled" instead of manual entry
   - System automatically runs both test cases
   - Results are displayed with clear success (✓) or failure (✗) indicators

### Example Usage
When you select "Pre-filled Data" for **Search Member by Email**:
```
=== SUCCESS CASE ===
Searching for: mariam.diallo@example.com
✓ Found: Jane Smith (ID: 1, Email: mariam.diallo@example.com)

=== FAILURE CASE (Non-existent Email) ===
Searching for: nonexistent@example.com
✗ Not found: nonexistent@example.com
```

This system makes it easy to demonstrate all functionality without repeatedly entering test data manually.

## Implemented Operations

### Admin Operations

1. **Schedule Class Session**
   - Create class session schedules with room booking
   - Prevents room double-booking
   - Validates trainer availability
   - Ensures class and room exist

2. **Create Class Template**
   - Create class definitions with categories, difficulty levels, and descriptions
   - Tracks admin assignments and dates

### Trainer Operations

3. **View Member Dashboard** ⭐ *Demonstrates VIEW*
   - Queries the `MemberDashboardSimple` view for a specific member
   - Displays aggregated member statistics:
     - Last recorded health metric
     - Total class registrations
     - Goal information
   - Shows benefit of pre-computed aggregations

4. **Test Trainer Availability Time Validation** ⭐ *Demonstrates TRIGGER*
   - Tests the `trg_check_trainer_availability_time` trigger
   - Validates that end_time > start_time
   - Shows both successful validation and trigger blocking invalid data
   - Demonstrates database-level data integrity enforcement

### Member Operations

5. **Register for Class Session**
   - Enroll members in scheduled classes
   - Prevents duplicate registrations
   - Verifies session capacity
   - Validates session existence

6. **Log Health Metric**
   - Record timestamped health data (weight, heart rate, etc.)
   - Supports multiple metric types

7. **Search Member by Email** ⭐ *Demonstrates INDEX*
   - Fast email-based member lookup using `idx_member_email` index
   - Returns complete member profile information
   - Shows performance benefit of indexed searches

8. **Register a New Member**
   - Create member profiles with personal information and fitness goals
   - Validates unique email constraint

All operations use parameterized SQL queries executed via `psycopg2` for security and performance.

## Demo Video

YouTube : `your_link_here`

### Video Contents:
- ERD diagram walkthrough
- Relational mapping and normalization summary
- DDL and DML execution demonstration
- Complete demonstration of all 8 operations
- Code overview (main.py and operations.py)
