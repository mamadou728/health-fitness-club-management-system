"""
Pre-filled operation wrappers that use sample data from prefilled_data.py
Mode choice is handled in main.py - these functions only execute with pre-filled data.
"""

import sys
import os

# Add parent directory to path to import operations
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.operations import *
from prefilled.prefilled_data import *


def prefilled_register_member():
    """OP1: Register Member with pre-filled data"""
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


def prefilled_update_member_profile():
    """OP2: Update Member Profile with pre-filled data"""
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


def prefilled_log_health_metric():
    """OP3: Log Health Metric with pre-filled data"""
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


def prefilled_register_for_class_session():
    """OP4: Register for Class Session with pre-filled data"""
    print("\nUsing pre-filled data:")
    print(f"  Member ID: {CLASS_REGISTRATION_DATA['member_id']}")
    print(f"  Session ID: {CLASS_REGISTRATION_DATA['session_id']}")
    
    return register_for_class_session(
        CLASS_REGISTRATION_DATA['member_id'],
        CLASS_REGISTRATION_DATA['session_id']
    )


def prefilled_set_trainer_availability():
    """OP5: Set Trainer Availability with pre-filled data"""
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


def prefilled_view_trainer_schedule():
    """OP6: View Trainer Schedule with pre-filled data"""
    print("\nUsing pre-filled data:")
    print(f"  Trainer ID: {TRAINER_SCHEDULE_DATA['trainer_id']}")
    print(f"  From Date: Today")
    
    return view_trainer_schedule(
        TRAINER_SCHEDULE_DATA['trainer_id'],
        TRAINER_SCHEDULE_DATA['from_date']
    )


def prefilled_create_class():
    """OP7: Create Class Template with pre-filled data"""
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


def prefilled_update_class():
    """OP7: Update Class Template with pre-filled data"""
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


def prefilled_schedule_class_session():
    """OP8: Schedule Class Session with pre-filled data"""
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


def prefilled_reschedule_class_session():
    """OP8: Reschedule Class Session with pre-filled data"""
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
