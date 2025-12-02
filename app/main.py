import sys
import os

# Get the parent folder and add it to Python's search path

current_file_location = os.path.dirname(__file__)  

parent_folder = os.path.dirname(current_file_location)  

sys.path.insert(0, parent_folder)

# Import database operations and pre-filled test data functions
from app.operations import *
from prefilled.prefilled_operations import *

def main_menu():
    while True:
        print("\n" + "="*50)
        print("HEALTH & FITNESS CLUB MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Member Operations")
        print("2. Trainer Operations")
        print("3. Admin Operations")
        print("4. Exit")
        print("="*50)
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            member_menu()
        elif choice == "2":
            trainer_menu()
        elif choice == "3":
            admin_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def member_menu():
    while True:
        print("\n--- MEMBER OPERATIONS ---")
        print("1. Register New Member")
        print("2. Search Member by Email")
        print("3. Log Health Metric")
        print("4. Register for Class Session")
        print("5. Back to Main Menu")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_register_member()
            else:
                first_name = input("First name: ").strip()
                last_name = input("Last name: ").strip()
                email = input("Email: ").strip()
                dob = input("DOB (YYYY-MM-DD): ").strip()
                phone = input("Phone: ").strip()
                goal = input("Goal: ").strip()
                target = input("Target: ").strip()
                register_member(first_name, last_name, dob, email, phone, goal, float(target) if target else None)
        
        elif choice == "2":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_search_member_by_email()
            else:
                email = input("Email: ").strip()
                search_member_by_email(email)
        
        elif choice == "3":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_log_health_metric()
            else:
                member_id = input("Member ID: ").strip()
                metric_type = input("Metric type: ").strip()
                value = input("Value: ").strip()
                log_health_metric(int(member_id), metric_type, float(value), None)
        
        elif choice == "4":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_register_for_class_session()
            else:
                member_id = input("Member ID: ").strip()
                session_id = input("Session ID: ").strip()
                register_for_class_session(int(member_id), int(session_id))
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice.")


def trainer_menu():
    while True:
        print("\n--- TRAINER OPERATIONS ---")
        print("1. Test Trainer Availability")
        print("2. View Member Dashboard")
        print("3. Back to Main Menu")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_test_trainer_availability_validation()
            else:
                trainer_id = input("Trainer ID: ").strip()
                day = input("Day (e.g., Monday): ").strip()
                start = input("Start time (HH:MM:SS): ").strip()
                end = input("End time (HH:MM:SS): ").strip()
                test_trainer_availability_validation(int(trainer_id), day, start, end)
        
        elif choice == "2":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_view_member_dashboard()
            else:
                member_id = input("Member ID: ").strip()
                view_member_dashboard(int(member_id))
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice.")


def admin_menu():
    while True:
        print("\n--- ADMIN OPERATIONS ---")
        print("1. Create Class Template")
        print("2. Schedule Class Session")
        print("3. Back to Main Menu")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_create_class()
            else:
                admin_id = input("Admin ID: ").strip()
                name = input("Class name: ").strip()
                desc = input("Description: ").strip()
                diff = input("Difficulty: ").strip()
                cat = input("Category: ").strip()
                dur = input("Duration (min): ").strip()
                create_class(int(admin_id), name, desc, diff, cat, int(dur) if dur else None)
        
        elif choice == "2":
            mode = input("1. Manual | 2. Pre-filled: ").strip()
            if mode == "2":
                prefilled_schedule_class_session()
            else:
                class_id = input("Class ID: ").strip()
                room_id = input("Room ID: ").strip()
                trainer_id = input("Trainer ID: ").strip()
                date = input("Date (YYYY-MM-DD): ").strip()
                start = input("Start (HH:MM:SS): ").strip()
                end = input("End (HH:MM:SS): ").strip()
                cap = input("Capacity: ").strip()
                schedule_class_session(int(class_id), int(room_id), int(trainer_id), date, start, end, int(cap))
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
