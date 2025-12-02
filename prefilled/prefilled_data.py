"""
Pre-filled sample data for testing all operations quickly.
Each entity contains one valid sample for rapid testing.
"""

# OP1: Register Member
MEMBER_DATA = {
    'first_name': 'John',
    'last_name': 'Doe',
    'date_of_birth': '1990-05-15',
    'email': 'john.doe@example.com',
    'phone': '555-0123',
    'goal_description': 'Lose weight and build muscle',
    'goal_target': 75.0
}

# OP2: Update Member Profile
MEMBER_UPDATE_DATA = {
    'member_id': 1,
    'first_name': 'Jane',
    'last_name': 'Smith',
    'phone': '555-9999',
    'goal_description': 'Improve cardiovascular health',
    'goal_target': 65.0
}

# OP3: Log Health Metric
HEALTH_METRIC_DATA = {
    'member_id': 1,
    'metric_type': 'weight',
    'value': 72.5,
    'recorded_at': None  
}

# OP4: Register for Class Session
CLASS_REGISTRATION_DATA = {
    'member_id': 1,
    'session_id': 1
}

# OP5: Set Trainer Availability
TRAINER_AVAILABILITY_DATA = {
    'trainer_id': 1,
    'day_of_week': 'Monday',
    'start_time': '09:00:00',
    'end_time': '17:00:00'
}

# OP6: View Trainer Schedule
TRAINER_SCHEDULE_DATA = {
    'trainer_id': 1,
    'from_date': None  
}

# OP7: Create Class Template
CLASS_CREATE_DATA = {
    'admin_id': 1,
    'name': 'Advanced Yoga',
    'description': 'Advanced level yoga for experienced practitioners',
    'difficulty': 'Hard',
    'category': 'Yoga',
    'duration_minutes': 60
}

# OP7: Update Class Template
CLASS_UPDATE_DATA = {
    'class_id': 1,
    'name': 'Beginner Yoga',
    'description': 'Gentle yoga for beginners',
    'difficulty': 'Easy',
    'category': 'Yoga',
    'duration_minutes': 45,
    'admin_id': 1
}

# OP8: Schedule Class Session
CLASS_SESSION_SCHEDULE_DATA = {
    'class_id': 1,
    'room_id': 1,
    'trainer_id': 1,
    'session_date': '2024-12-15',
    'start_time': '10:00:00',
    'end_time': '11:00:00',
    'capacity': 20
}

# OP8: Reschedule Class Session
CLASS_SESSION_RESCHEDULE_DATA = {
    'session_id': 1,
    'room_id': 2,
    'trainer_id': 1,
    'session_date': '2024-12-16',
    'start_time': '14:00:00',
    'end_time': '15:00:00',
    'capacity': 15
}
