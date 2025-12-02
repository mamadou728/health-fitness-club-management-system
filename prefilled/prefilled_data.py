"""
Pre-filled sample data for testing all operations quickly.
Data is based on existing DML records to ensure compatibility.

Existing DB Data Summary:
- Members: 1-6 (Mariam, Owen, Leila, Samuel, Nadia, Ibrahim)
- Trainers: 1-5 (Emily, James, Alex, Rita, Daniel)
- Admins: 1-3 (Sarah, David, Amina)
- Rooms: 1-4 (Studio A, Studio B, PT Room 1, PT Room 2)
- Classes: 1-6 (Morning Yoga, HIIT Express, Strength Basics, Pilates Flow, CrossFit Starter, Evening Relax Yoga)
- Sessions: 1-10 (various scheduled sessions)
"""

# OP1: Register Member
MEMBER_DATA_SUCCESS = {
    'first_name': 'Fatima',
    'last_name': 'Ahmed',
    'date_of_birth': '2000-08-22',
    'email': 'fatima.ahmed@example.com',
    'phone': '613-555-3007',
    'goal_description': 'Build strength and endurance',
    'goal_target': 68.0
}

MEMBER_DATA_FAILURE = {
    'first_name': 'Duplicate',
    'last_name': 'User',
    'date_of_birth': '1990-01-01',
    'email': 'mariam.diallo@example.com',  # Duplicate email - will fail
    'phone': '613-555-9999',
    'goal_description': 'Test duplicate',
    'goal_target': 70.0
}

# OP2: Search Member by Email
MEMBER_SEARCH_SUCCESS = {
    'email': 'mariam.diallo@example.com'  # Existing member - will find
}

MEMBER_SEARCH_FAILURE = {
    'email': 'nonexistent@example.com'  # Does not exist - will fail
}

# OP3: Log Health Metric
HEALTH_METRIC_SUCCESS = {
    'member_id': 2,  # Owen Clark - exists
    'metric_type': 'resting_heart_rate',
    'value': 72.0,
    'recorded_at': None
}

HEALTH_METRIC_FAILURE = {
    'member_id': 9999,  # Does not exist - will fail
    'metric_type': 'weight',
    'value': 75.0,
    'recorded_at': None
}

# OP4: Register for Class Session
CLASS_REGISTRATION_SUCCESS = {
    'member_id': 3,  # Leila Hassan - exists
    'session_id': 4  # HIIT Express - exists
}

CLASS_REGISTRATION_FAILURE = {
    'member_id': 1,  # Mariam - exists
    'session_id': 9999  # Does not exist - will fail
}

# OP5: Test Trainer Availability Validation
TRAINER_AVAILABILITY_SUCCESS = {
    'trainer_id': 1,  # Emily Carter - exists
    'day_of_week': 'Wednesday',
    'start_time': '09:00:00',
    'end_time': '17:00:00'  # Valid: end_time > start_time
}

TRAINER_AVAILABILITY_FAILURE = {
    'trainer_id': 1,
    'day_of_week': 'Thursday',
    'start_time': '17:00:00',
    'end_time': '09:00:00'  # Invalid: trigger blocks
}

# OP6: View Member Dashboard
MEMBER_DASHBOARD_SUCCESS = {
    'member_id': 1  # Mariam Diallo - exists
}

MEMBER_DASHBOARD_FAILURE = {
    'member_id': 9999  # Does not exist - will fail
}

# OP7: Create Class Template
CLASS_CREATE_SUCCESS = {
    'admin_id': 1,  # Sarah Johnson - exists
    'name': 'Spin Class',
    'description': 'High-energy indoor cycling workout',
    'difficulty': 'Medium',
    'category': 'Cardio',
    'duration_minutes': 45
}

CLASS_CREATE_FAILURE = {
    'admin_id': 9999,  # Does not exist - will fail
    'name': 'Invalid Class',
    'description': 'Test failure',
    'difficulty': 'Easy',
    'category': 'Test',
    'duration_minutes': 30
}

# OP8: Schedule Class Session
CLASS_SESSION_SCHEDULE_SUCCESS = {
    'class_id': 2,  # HIIT Express - exists
    'room_id': 2,   # Studio B - exists
    'trainer_id': 3,  # Alex Nguyen - exists
    'session_date': '2025-12-05',
    'start_time': '18:00:00',
    'end_time': '18:45:00',
    'capacity': 25
}

CLASS_SESSION_SCHEDULE_FAILURE = {
    'class_id': 9999,  # Does not exist - will fail
    'room_id': 2,
    'trainer_id': 3,
    'session_date': '2025-12-05',
    'start_time': '19:00:00',
    'end_time': '19:45:00',
    'capacity': 20
}
