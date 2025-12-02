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

# OP1: Register Member (NEW member - will get ID 7)
MEMBER_DATA = {
    'first_name': 'Fatima',
    'last_name': 'Ahmed',
    'date_of_birth': '2000-08-22',
    'email': 'fatima.ahmed@example.com',
    'phone': '613-555-3007',
    'goal_description': 'Build strength and endurance',
    'goal_target': 68.0
}

# OP2: Update Member Profile (Update existing member #1 - Mariam)
MEMBER_UPDATE_DATA = {
    'member_id': 1,  # Mariam Diallo
    'first_name': 'Mariam',
    'last_name': 'Diallo',
    'phone': '613-555-3099',
    'goal_description': 'Maintain weight at 65kg',
    'goal_target': 65.0
}

# OP3: Log Health Metric (For existing member #2 - Owen)
HEALTH_METRIC_DATA = {
    'member_id': 2,  # Owen Clark
    'metric_type': 'resting_heart_rate',
    'value': 72.0,
    'recorded_at': None  # Will use current timestamp
}

# OP4: Register for Class Session (Member #3 for Session #4)
CLASS_REGISTRATION_DATA = {
    'member_id': 3,  # Leila Hassan
    'session_id': 4  # HIIT Express on 2025-11-28
}

# OP5: Set Trainer Availability (NEW availability for Trainer #1 - Emily)
TRAINER_AVAILABILITY_DATA = {
    'trainer_id': 1,  # Emily Carter (Strength & Conditioning)
    'day_of_week': 'Tuesday',
    'start_time': '10:00:00',
    'end_time': '14:00:00'
}

# OP6: View Trainer Schedule (View for Trainer #2 - James)
TRAINER_SCHEDULE_DATA = {
    'trainer_id': 2,  # James Miller (Yoga & Mobility)
    'from_date': None  # Will use current date
}

# OP7: Create Class Template (NEW class - will get ID 7)
CLASS_CREATE_DATA = {
    'admin_id': 1,  # Sarah Johnson (Operations Manager)
    'name': 'Spin Class',
    'description': 'High-energy indoor cycling workout',
    'difficulty': 'Medium',
    'category': 'Cardio',
    'duration_minutes': 45
}

# OP7: Update Class Template (Update existing class #1 - Morning Yoga)
CLASS_UPDATE_DATA = {
    'class_id': 1,  # Morning Yoga
    'name': 'Morning Yoga Plus',
    'description': 'Enhanced flexibility and breathing with meditation',
    'difficulty': 'Easy',
    'category': 'Yoga',
    'duration_minutes': 75,
    'admin_id': 3  # Amina Conte (Class Coordinator)
}

# OP8: Schedule Class Session (NEW session for Class #2 - HIIT Express)
CLASS_SESSION_SCHEDULE_DATA = {
    'class_id': 2,  # HIIT Express
    'room_id': 2,   # Studio B
    'trainer_id': 3,  # Alex Nguyen (HIIT & Cardio)
    'session_date': '2025-12-05',
    'start_time': '18:00:00',
    'end_time': '18:45:00',
    'capacity': 25
}

# OP8: Reschedule Class Session (Reschedule existing session #10)
CLASS_SESSION_RESCHEDULE_DATA = {
    'session_id': 10,  # Strength Basics session
    'room_id': 3,      # PT Room 1
    'trainer_id': 1,   # Emily Carter
    'session_date': '2025-12-04',
    'start_time': '15:00:00',
    'end_time': '16:00:00',
    'capacity': 15
}
