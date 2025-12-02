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
    """OP1: Register Member - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Registering: {MEMBER_DATA_SUCCESS['first_name']} {MEMBER_DATA_SUCCESS['last_name']} ({MEMBER_DATA_SUCCESS['email']})")
    register_member(**MEMBER_DATA_SUCCESS)
    
    print("\n=== FAILURE CASE (Duplicate Email) ===")
    print(f"Attempting: {MEMBER_DATA_FAILURE['first_name']} {MEMBER_DATA_FAILURE['last_name']} ({MEMBER_DATA_FAILURE['email']})")
    register_member(**MEMBER_DATA_FAILURE)


def prefilled_search_member_by_email():
    """OP2: Search Member by Email - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Searching for: {MEMBER_SEARCH_SUCCESS['email']}")
    search_member_by_email(**MEMBER_SEARCH_SUCCESS)
    
    print("\n=== FAILURE CASE (Non-existent Email) ===")
    print(f"Searching for: {MEMBER_SEARCH_FAILURE['email']}")
    search_member_by_email(**MEMBER_SEARCH_FAILURE)


def prefilled_log_health_metric():
    """OP3: Log Health Metric - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Logging {HEALTH_METRIC_SUCCESS['metric_type']}={HEALTH_METRIC_SUCCESS['value']} for Member ID {HEALTH_METRIC_SUCCESS['member_id']}")
    log_health_metric(**HEALTH_METRIC_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Member ID) ===")
    print(f"Logging {HEALTH_METRIC_FAILURE['metric_type']}={HEALTH_METRIC_FAILURE['value']} for Member ID {HEALTH_METRIC_FAILURE['member_id']}")
    log_health_metric(**HEALTH_METRIC_FAILURE)


def prefilled_register_for_class_session():
    """OP4: Register for Class Session - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Registering Member ID {CLASS_REGISTRATION_SUCCESS['member_id']} for Session ID {CLASS_REGISTRATION_SUCCESS['session_id']}")
    register_for_class_session(**CLASS_REGISTRATION_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Session ID) ===")
    print(f"Registering Member ID {CLASS_REGISTRATION_FAILURE['member_id']} for Session ID {CLASS_REGISTRATION_FAILURE['session_id']}")
    register_for_class_session(**CLASS_REGISTRATION_FAILURE)


def prefilled_test_trainer_availability_validation():
    """OP5: Test Trainer Availability - Tests success and failure (TRIGGER)"""
    print("\n=== SUCCESS CASE (Valid Times) ===")
    print(f"Setting Trainer ID {TRAINER_AVAILABILITY_SUCCESS['trainer_id']} availability: {TRAINER_AVAILABILITY_SUCCESS['day_of_week']} {TRAINER_AVAILABILITY_SUCCESS['start_time']}-{TRAINER_AVAILABILITY_SUCCESS['end_time']}")
    test_trainer_availability_validation(**TRAINER_AVAILABILITY_SUCCESS)
    
    print("\n=== FAILURE CASE (Trigger Blocks Invalid Times) ===")
    print(f"Setting Trainer ID {TRAINER_AVAILABILITY_FAILURE['trainer_id']} availability: {TRAINER_AVAILABILITY_FAILURE['day_of_week']} {TRAINER_AVAILABILITY_FAILURE['start_time']}-{TRAINER_AVAILABILITY_FAILURE['end_time']}")
    test_trainer_availability_validation(**TRAINER_AVAILABILITY_FAILURE)


def prefilled_view_member_dashboard():
    """OP6: View Member Dashboard - Tests success and failure (VIEW)"""
    print("\n=== SUCCESS CASE ===")
    print(f"Viewing dashboard for Member ID {MEMBER_DASHBOARD_SUCCESS['member_id']}")
    view_member_dashboard(MEMBER_DASHBOARD_SUCCESS['member_id'])
    
    print("\n=== FAILURE CASE (Non-existent Member) ===")
    print(f"Viewing dashboard for Member ID {MEMBER_DASHBOARD_FAILURE['member_id']}")
    view_member_dashboard(MEMBER_DASHBOARD_FAILURE['member_id'])


def prefilled_create_class():
    """OP7: Create Class - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Creating class '{CLASS_CREATE_SUCCESS['name']}' by Admin ID {CLASS_CREATE_SUCCESS['admin_id']}")
    create_class(**CLASS_CREATE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Admin ID) ===")
    print(f"Creating class '{CLASS_CREATE_FAILURE['name']}' by Admin ID {CLASS_CREATE_FAILURE['admin_id']}")
    create_class(**CLASS_CREATE_FAILURE)


def prefilled_update_class():
    """OP7: Update Class - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Updating Class ID {CLASS_UPDATE_SUCCESS['class_id']} to '{CLASS_UPDATE_SUCCESS['name']}'")
    update_class(**CLASS_UPDATE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Class ID) ===")
    print(f"Updating Class ID {CLASS_UPDATE_FAILURE['class_id']} to '{CLASS_UPDATE_FAILURE['name']}'")
    update_class(**CLASS_UPDATE_FAILURE)


def prefilled_schedule_class_session():
    """OP8: Schedule Class Session - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Scheduling Class ID {CLASS_SESSION_SCHEDULE_SUCCESS['class_id']} on {CLASS_SESSION_SCHEDULE_SUCCESS['session_date']} at {CLASS_SESSION_SCHEDULE_SUCCESS['start_time']}")
    schedule_class_session(**CLASS_SESSION_SCHEDULE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Class ID) ===")
    print(f"Scheduling Class ID {CLASS_SESSION_SCHEDULE_FAILURE['class_id']} on {CLASS_SESSION_SCHEDULE_FAILURE['session_date']} at {CLASS_SESSION_SCHEDULE_FAILURE['start_time']}")
    schedule_class_session(**CLASS_SESSION_SCHEDULE_FAILURE)


def prefilled_reschedule_class_session():
    """OP8: Reschedule Class Session - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    print(f"Rescheduling Session ID {CLASS_SESSION_RESCHEDULE_SUCCESS['session_id']} to {CLASS_SESSION_RESCHEDULE_SUCCESS['session_date']} at {CLASS_SESSION_RESCHEDULE_SUCCESS['start_time']}")
    reschedule_class_session(**CLASS_SESSION_RESCHEDULE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Session ID) ===")
    print(f"Rescheduling Session ID {CLASS_SESSION_RESCHEDULE_FAILURE['session_id']} to {CLASS_SESSION_RESCHEDULE_FAILURE['session_date']} at {CLASS_SESSION_RESCHEDULE_FAILURE['start_time']}")
    reschedule_class_session(**CLASS_SESSION_RESCHEDULE_FAILURE)
