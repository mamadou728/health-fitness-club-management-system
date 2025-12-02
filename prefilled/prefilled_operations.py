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
    register_member(**MEMBER_DATA_SUCCESS)
    
    print("\n=== FAILURE CASE (Duplicate Email) ===")
    register_member(**MEMBER_DATA_FAILURE)


def prefilled_search_member_by_email():
    """OP2: Search Member by Email - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    search_member_by_email(**MEMBER_SEARCH_SUCCESS)
    
    print("\n=== FAILURE CASE (Non-existent Email) ===")
    search_member_by_email(**MEMBER_SEARCH_FAILURE)


def prefilled_log_health_metric():
    """OP3: Log Health Metric - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    log_health_metric(**HEALTH_METRIC_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Member ID) ===")
    log_health_metric(**HEALTH_METRIC_FAILURE)


def prefilled_register_for_class_session():
    """OP4: Register for Class Session - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    register_for_class_session(**CLASS_REGISTRATION_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Session ID) ===")
    register_for_class_session(**CLASS_REGISTRATION_FAILURE)


def prefilled_test_trainer_availability_validation():
    """OP5: Test Trainer Availability - Tests success and failure (TRIGGER)"""
    print("\n=== SUCCESS CASE (Valid Times) ===")
    test_trainer_availability_validation(**TRAINER_AVAILABILITY_SUCCESS)
    
    print("\n=== FAILURE CASE (Trigger Blocks Invalid Times) ===")
    test_trainer_availability_validation(**TRAINER_AVAILABILITY_FAILURE)


def prefilled_view_member_dashboard():
    """OP6: View Member Dashboard - Tests success and failure (VIEW)"""
    print("\n=== SUCCESS CASE ===")
    view_member_dashboard(**MEMBER_DASHBOARD_SUCCESS)
    
    print("\n=== FAILURE CASE (Non-existent Member) ===")
    view_member_dashboard(**MEMBER_DASHBOARD_FAILURE)


def prefilled_create_class():
    """OP7: Create Class - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    create_class(**CLASS_CREATE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Admin ID) ===")
    create_class(**CLASS_CREATE_FAILURE)


def prefilled_update_class():
    """OP7: Update Class - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    update_class(**CLASS_UPDATE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Class ID) ===")
    update_class(**CLASS_UPDATE_FAILURE)


def prefilled_schedule_class_session():
    """OP8: Schedule Class Session - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    schedule_class_session(**CLASS_SESSION_SCHEDULE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Class ID) ===")
    schedule_class_session(**CLASS_SESSION_SCHEDULE_FAILURE)


def prefilled_reschedule_class_session():
    """OP8: Reschedule Class Session - Tests success and failure"""
    print("\n=== SUCCESS CASE ===")
    reschedule_class_session(**CLASS_SESSION_RESCHEDULE_SUCCESS)
    
    print("\n=== FAILURE CASE (Invalid Session ID) ===")
    reschedule_class_session(**CLASS_SESSION_RESCHEDULE_FAILURE)
