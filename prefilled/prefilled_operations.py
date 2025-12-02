"""
Dual-mode operation wrappers that support both manual input and pre-filled data.
These functions provide a choice between manual entry and using pre-filled sample data.
"""

import sys
import os

# Add parent directory to path to import operations
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.operations import *
from prefilled.prefilled_data import *


def get_mode_choice(operation_name):
    """
    Ask user to choose between manual entry or pre-filled data.
    Returns: 'manual' or 'prefilled'
    """
    print(f"\n--- {operation_name} ---")
    print("1. Enter data manually")
    print("2. Use pre-filled data")
    choice = input("Select mode (1-2): ").strip()
    
    if choice == "2":
        return 'prefilled'
    return 'manual'


def prefilled_register_member():
    """OP1: Register Member with dual-mode support"""
    mode = get_mode_choice("Register New Member")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Name: {MEMBER_DATA['first_name']} {MEMBER_DATA['last_name']}")
        print(f"  Email: {MEMBER_DATA['email']}")
        print(f"  DOB: {MEMBER_DATA['date_of_birth']}")
        print(f"  Phone: {MEMBER_DATA['phone']}")
        print(f"  Goal: {MEMBER_DATA['goal_description']}")
        print(f"  Target: {MEMBER_DATA['goal_target']}")
        
        return register_member(
            MEMBER_DATA['first_name'],
            MEMBER_DATA['last_name'],
            MEMBER_DATA['date_of_birth'],
            MEMBER_DATA['email'],
            MEMBER_DATA['phone'],
            MEMBER_DATA['goal_description'],
            MEMBER_DATA['goal_target']
        )
    else:
        # Manual entry
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        email = input("Email: ").strip()
        date_of_birth = input("Date of birth (YYYY-MM-DD) or press Enter to skip: ").strip() or None
        phone = input("Phone or press Enter to skip: ").strip() or None
        goal_description = input("Goal description or press Enter to skip: ").strip() or None
        goal_target = input("Goal target (numeric only) or press Enter to skip: ").strip()
        try:
            goal_target = float(goal_target) if goal_target else None
        except ValueError:
            print("Error: Goal target must be a number. Setting to None.")
            goal_target = None
        
        return register_member(first_name, last_name, date_of_birth, email, phone, goal_description, goal_target)


def prefilled_update_member_profile():
    """OP2: Update Member Profile with dual-mode support"""
    mode = get_mode_choice("Update Member Profile")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Member ID: {MEMBER_UPDATE_DATA['member_id']}")
        print(f"  New Name: {MEMBER_UPDATE_DATA['first_name']} {MEMBER_UPDATE_DATA['last_name']}")
        print(f"  New Phone: {MEMBER_UPDATE_DATA['phone']}")
        print(f"  New Goal: {MEMBER_UPDATE_DATA['goal_description']}")
        print(f"  New Target: {MEMBER_UPDATE_DATA['goal_target']}")
        
        return update_member_profile(
            MEMBER_UPDATE_DATA['member_id'],
            MEMBER_UPDATE_DATA['first_name'],
            MEMBER_UPDATE_DATA['last_name'],
            MEMBER_UPDATE_DATA['phone'],
            MEMBER_UPDATE_DATA['goal_description'],
            MEMBER_UPDATE_DATA['goal_target']
        )
    else:
        # Manual entry
        try:
            member_id = int(input("Member ID: ").strip())
        except ValueError:
            print("Error: Member ID must be a number.")
            return False
        print("Leave blank to keep current value:")
        first_name = input("New first name: ").strip() or None
        last_name = input("New last name: ").strip() or None
        phone = input("New phone: ").strip() or None
        goal_description = input("New goal description: ").strip() or None
        goal_target = input("New goal target: ").strip()
        try:
            goal_target = float(goal_target) if goal_target else None
        except ValueError:
            print("Error: Goal target must be a number. Keeping current value.")
            goal_target = None
        
        return update_member_profile(member_id, first_name, last_name, phone, goal_description, goal_target)


def prefilled_log_health_metric():
    """OP3: Log Health Metric with dual-mode support"""
    mode = get_mode_choice("Log Health Metric")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Member ID: {HEALTH_METRIC_DATA['member_id']}")
        print(f"  Metric Type: {HEALTH_METRIC_DATA['metric_type']}")
        print(f"  Value: {HEALTH_METRIC_DATA['value']}")
        print(f"  Recorded At: Now")
        
        return log_health_metric(
            HEALTH_METRIC_DATA['member_id'],
            HEALTH_METRIC_DATA['metric_type'],
            HEALTH_METRIC_DATA['value'],
            HEALTH_METRIC_DATA['recorded_at']
        )
    else:
        # Manual entry
        try:
            member_id = int(input("Member ID: ").strip())
            metric_type = input("Metric type (e.g., weight, heart_rate): ").strip()
            value = float(input("Value: ").strip())
        except ValueError:
            print("Error: Invalid input. Member ID and Value must be numbers.")
            return None
        recorded_at = input("Recorded at (YYYY-MM-DD HH:MM:SS) or press Enter for now: ").strip() or None
        
        return log_health_metric(member_id, metric_type, value, recorded_at)


def prefilled_register_for_class_session():
    """OP4: Register for Class Session with dual-mode support"""
    mode = get_mode_choice("Register for Class Session")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Member ID: {CLASS_REGISTRATION_DATA['member_id']}")
        print(f"  Session ID: {CLASS_REGISTRATION_DATA['session_id']}")
        
        return register_for_class_session(
            CLASS_REGISTRATION_DATA['member_id'],
            CLASS_REGISTRATION_DATA['session_id']
        )
    else:
        # Manual entry
        try:
            member_id = int(input("Member ID: ").strip())
            session_id = int(input("Session ID: ").strip())
        except ValueError:
            print("Error: Member ID and Session ID must be numbers.")
            return False
        
        return register_for_class_session(member_id, session_id)


def prefilled_set_trainer_availability():
    """OP5: Set Trainer Availability with dual-mode support"""
    mode = get_mode_choice("Set Trainer Availability")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Trainer ID: {TRAINER_AVAILABILITY_DATA['trainer_id']}")
        print(f"  Day: {TRAINER_AVAILABILITY_DATA['day_of_week']}")
        print(f"  Time: {TRAINER_AVAILABILITY_DATA['start_time']} - {TRAINER_AVAILABILITY_DATA['end_time']}")
        
        return set_trainer_availability(
            TRAINER_AVAILABILITY_DATA['trainer_id'],
            TRAINER_AVAILABILITY_DATA['day_of_week'],
            TRAINER_AVAILABILITY_DATA['start_time'],
            TRAINER_AVAILABILITY_DATA['end_time']
        )
    else:
        # Manual entry
        try:
            trainer_id = int(input("Trainer ID: ").strip())
        except ValueError:
            print("Error: Trainer ID must be a number.")
            return None
        day_of_week = input("Day of week (e.g., Monday): ").strip()
        start_time = input("Start time (HH:MM:SS): ").strip()
        end_time = input("End time (HH:MM:SS): ").strip()
        
        return set_trainer_availability(trainer_id, day_of_week, start_time, end_time)


def prefilled_view_trainer_schedule():
    """OP6: View Trainer Schedule with dual-mode support"""
    mode = get_mode_choice("View Trainer Schedule")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Trainer ID: {TRAINER_SCHEDULE_DATA['trainer_id']}")
        print(f"  From Date: Today")
        
        return view_trainer_schedule(
            TRAINER_SCHEDULE_DATA['trainer_id'],
            TRAINER_SCHEDULE_DATA['from_date']
        )
    else:
        # Manual entry
        try:
            trainer_id = int(input("Trainer ID: ").strip())
        except ValueError:
            print("Error: Trainer ID must be a number.")
            return None
        from_date = input("From date (YYYY-MM-DD) or press Enter for today: ").strip() or None
        
        return view_trainer_schedule(trainer_id, from_date)


def prefilled_create_class():
    """OP7: Create Class Template with dual-mode support"""
    mode = get_mode_choice("Create Class Template")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Admin ID: {CLASS_CREATE_DATA['admin_id']}")
        print(f"  Name: {CLASS_CREATE_DATA['name']}")
        print(f"  Description: {CLASS_CREATE_DATA['description']}")
        print(f"  Difficulty: {CLASS_CREATE_DATA['difficulty']}")
        print(f"  Category: {CLASS_CREATE_DATA['category']}")
        print(f"  Duration: {CLASS_CREATE_DATA['duration_minutes']} minutes")
        
        return create_class(
            CLASS_CREATE_DATA['admin_id'],
            CLASS_CREATE_DATA['name'],
            CLASS_CREATE_DATA['description'],
            CLASS_CREATE_DATA['difficulty'],
            CLASS_CREATE_DATA['category'],
            CLASS_CREATE_DATA['duration_minutes']
        )
    else:
        # Manual entry
        try:
            admin_id = int(input("Admin ID: ").strip())
        except ValueError:
            print("Error: Admin ID must be a number.")
            return None
        name = input("Class name: ").strip()
        description = input("Description or press Enter to skip: ").strip() or None
        difficulty = input("Difficulty (Easy/Medium/Hard) or press Enter to skip: ").strip() or None
        category = input("Category or press Enter to skip: ").strip() or None
        duration = input("Duration (minutes) or press Enter to skip: ").strip()
        try:
            duration_minutes = int(duration) if duration else None
        except ValueError:
            print("Error: Duration must be a number. Setting to None.")
            duration_minutes = None
        
        return create_class(admin_id, name, description, difficulty, category, duration_minutes)


def prefilled_update_class():
    """OP7: Update Class Template with dual-mode support"""
    mode = get_mode_choice("Update Class Template")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Class ID: {CLASS_UPDATE_DATA['class_id']}")
        print(f"  New Name: {CLASS_UPDATE_DATA['name']}")
        print(f"  New Description: {CLASS_UPDATE_DATA['description']}")
        print(f"  New Difficulty: {CLASS_UPDATE_DATA['difficulty']}")
        print(f"  New Category: {CLASS_UPDATE_DATA['category']}")
        print(f"  New Duration: {CLASS_UPDATE_DATA['duration_minutes']} minutes")
        print(f"  New Admin ID: {CLASS_UPDATE_DATA['admin_id']}")
        
        return update_class(
            CLASS_UPDATE_DATA['class_id'],
            CLASS_UPDATE_DATA['name'],
            CLASS_UPDATE_DATA['description'],
            CLASS_UPDATE_DATA['difficulty'],
            CLASS_UPDATE_DATA['category'],
            CLASS_UPDATE_DATA['duration_minutes'],
            CLASS_UPDATE_DATA['admin_id']
        )
    else:
        # Manual entry
        try:
            class_id = int(input("Class ID: ").strip())
        except ValueError:
            print("Error: Class ID must be a number.")
            return False
        print("Leave blank to keep current value:")
        name = input("New class name: ").strip() or None
        description = input("New description: ").strip() or None
        difficulty = input("New difficulty: ").strip() or None
        category = input("New category: ").strip() or None
        duration = input("New duration (minutes): ").strip()
        try:
            duration_minutes = int(duration) if duration else None
        except ValueError:
            print("Error: Duration must be a number. Keeping current value.")
            duration_minutes = None
        admin_id = input("New admin ID: ").strip()
        try:
            admin_id = int(admin_id) if admin_id else None
        except ValueError:
            print("Error: Admin ID must be a number. Keeping current value.")
            admin_id = None
        
        return update_class(class_id, name, description, difficulty, category, duration_minutes, admin_id)


def prefilled_schedule_class_session():
    """OP8: Schedule Class Session with dual-mode support"""
    mode = get_mode_choice("Schedule Class Session")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Class ID: {CLASS_SESSION_SCHEDULE_DATA['class_id']}")
        print(f"  Room ID: {CLASS_SESSION_SCHEDULE_DATA['room_id']}")
        print(f"  Trainer ID: {CLASS_SESSION_SCHEDULE_DATA['trainer_id']}")
        print(f"  Date: {CLASS_SESSION_SCHEDULE_DATA['session_date']}")
        print(f"  Time: {CLASS_SESSION_SCHEDULE_DATA['start_time']} - {CLASS_SESSION_SCHEDULE_DATA['end_time']}")
        print(f"  Capacity: {CLASS_SESSION_SCHEDULE_DATA['capacity']}")
        
        return schedule_class_session(
            CLASS_SESSION_SCHEDULE_DATA['class_id'],
            CLASS_SESSION_SCHEDULE_DATA['room_id'],
            CLASS_SESSION_SCHEDULE_DATA['trainer_id'],
            CLASS_SESSION_SCHEDULE_DATA['session_date'],
            CLASS_SESSION_SCHEDULE_DATA['start_time'],
            CLASS_SESSION_SCHEDULE_DATA['end_time'],
            CLASS_SESSION_SCHEDULE_DATA['capacity']
        )
    else:
        # Manual entry
        try:
            class_id = int(input("Class ID: ").strip())
            room_id = int(input("Room ID: ").strip())
            trainer_id = int(input("Trainer ID: ").strip())
        except ValueError:
            print("Error: IDs must be numbers.")
            return None
        session_date = input("Session date (YYYY-MM-DD): ").strip()
        start_time = input("Start time (HH:MM:SS): ").strip()
        end_time = input("End time (HH:MM:SS): ").strip()
        try:
            capacity = int(input("Capacity: ").strip())
        except ValueError:
            print("Error: Capacity must be a number.")
            return None
        
        return schedule_class_session(class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)


def prefilled_reschedule_class_session():
    """OP8: Reschedule Class Session with dual-mode support"""
    mode = get_mode_choice("Reschedule Class Session")
    
    if mode == 'prefilled':
        print("\nUsing pre-filled data:")
        print(f"  Session ID: {CLASS_SESSION_RESCHEDULE_DATA['session_id']}")
        print(f"  New Room ID: {CLASS_SESSION_RESCHEDULE_DATA['room_id']}")
        print(f"  New Trainer ID: {CLASS_SESSION_RESCHEDULE_DATA['trainer_id']}")
        print(f"  New Date: {CLASS_SESSION_RESCHEDULE_DATA['session_date']}")
        print(f"  New Time: {CLASS_SESSION_RESCHEDULE_DATA['start_time']} - {CLASS_SESSION_RESCHEDULE_DATA['end_time']}")
        print(f"  New Capacity: {CLASS_SESSION_RESCHEDULE_DATA['capacity']}")
        
        return reschedule_class_session(
            CLASS_SESSION_RESCHEDULE_DATA['session_id'],
            CLASS_SESSION_RESCHEDULE_DATA['room_id'],
            CLASS_SESSION_RESCHEDULE_DATA['trainer_id'],
            CLASS_SESSION_RESCHEDULE_DATA['session_date'],
            CLASS_SESSION_RESCHEDULE_DATA['start_time'],
            CLASS_SESSION_RESCHEDULE_DATA['end_time'],
            CLASS_SESSION_RESCHEDULE_DATA['capacity']
        )
    else:
        # Manual entry
        try:
            session_id = int(input("Session ID: ").strip())
        except ValueError:
            print("Error: Session ID must be a number.")
            return False
        print("Leave blank to keep current value:")
        room_id = input("New room ID: ").strip()
        try:
            room_id = int(room_id) if room_id else None
        except ValueError:
            print("Error: Room ID must be a number. Keeping current value.")
            room_id = None
        trainer_id = input("New trainer ID: ").strip()
        try:
            trainer_id = int(trainer_id) if trainer_id else None
        except ValueError:
            print("Error: Trainer ID must be a number. Keeping current value.")
            trainer_id = None
        session_date = input("New session date (YYYY-MM-DD): ").strip() or None
        start_time = input("New start time (HH:MM:SS): ").strip() or None
        end_time = input("New end time (HH:MM:SS): ").strip() or None
        capacity = input("New capacity: ").strip()
        try:
            capacity = int(capacity) if capacity else None
        except ValueError:
            print("Error: Capacity must be a number. Keeping current value.")
            capacity = None
        
        return reschedule_class_session(session_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
