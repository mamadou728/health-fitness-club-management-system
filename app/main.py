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
            # OP1: Register Member
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_register_member()
            else:
                print("\n--- Register New Member ---")
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
                register_member(first_name, last_name, date_of_birth, email, phone, goal_description, goal_target)
        
        elif choice == "2":
            # OP2: Search Member by Email
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_search_member_by_email()
            else:
                print("\n--- Search Member by Email ---")
                email = input("Email address: ").strip()
                search_member_by_email(email)
        
        elif choice == "3":
            # OP3: Log Health Metric
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_log_health_metric()
            else:
                print("\n--- Log Health Metric ---")
                try:
                    member_id = int(input("Member ID: ").strip())
                    metric_type = input("Metric type (e.g., weight, heart_rate): ").strip()
                    value = float(input("Value: ").strip())
                except ValueError:
                    print("Error: Invalid input. Member ID and Value must be numbers.")
                    continue
                recorded_at = input("Recorded at (YYYY-MM-DD HH:MM:SS) or press Enter for now: ").strip() or None
                log_health_metric(member_id, metric_type, value, recorded_at)
        
        elif choice == "4":
            # OP4: Register for Class Session
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_register_for_class_session()
            else:
                print("\n--- Register for Class Session ---")
                try:
                    member_id = int(input("Member ID: ").strip())
                    session_id = int(input("Session ID: ").strip())
                except ValueError:
                    print("Error: Member ID and Session ID must be numbers.")
                    continue
                register_for_class_session(member_id, session_id)
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Try again.")


def trainer_menu():
    while True:
        print("\n--- TRAINER OPERATIONS ---")
        print("1. Test Trainer Availability Validation")
        print("2. View Member Dashboard")
        print("3. Back to Main Menu")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            # OP5: Test Trainer Availability Validation
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_test_trainer_availability_validation()
            else:
                print("\n--- Test Trainer Availability Time Validation ---")
                try:
                    trainer_id = int(input("Trainer ID: ").strip())
                except ValueError:
                    print("Error: Trainer ID must be a number.")
                    continue
                day_of_week = input("Day of week (e.g., Monday): ").strip()
                start_time = input("Start time (HH:MM:SS): ").strip()
                end_time = input("End time (HH:MM:SS): ").strip()
                test_trainer_availability_validation(trainer_id, day_of_week, start_time, end_time)
        
        elif choice == "2":
            # OP6: View Member Dashboard
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_view_member_dashboard()
            else:
                print("\n--- View Member Dashboard ---")
                try:
                    member_id = int(input("Member ID: ").strip())
                except ValueError:
                    print("Error: Member ID must be a number.")
                    continue
                view_member_dashboard(member_id)
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Try again.")


def admin_menu():
    while True:
        print("\n--- ADMIN OPERATIONS ---")
        print("1. Create Class Template")
        print("2. Schedule Class Session")
        print("3. Reschedule Class Session")
        print("4. Back to Main Menu")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            # OP7: Create Class
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_create_class()
            else:
                print("\n--- Create Class Template ---")
                try:
                    admin_id = int(input("Admin ID: ").strip())
                except ValueError:
                    print("Error: Admin ID must be a number.")
                    continue
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
                create_class(admin_id, name, description, difficulty, category, duration_minutes)
        
        elif choice == "2":
            # OP8: Schedule Class Session
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_schedule_class_session()
            else:
                print("\n--- Schedule Class Session ---")
                try:
                    class_id = int(input("Class ID: ").strip())
                    room_id = int(input("Room ID: ").strip())
                    trainer_id = int(input("Trainer ID: ").strip())
                except ValueError:
                    print("Error: IDs must be numbers.")
                    continue
                session_date = input("Session date (YYYY-MM-DD): ").strip()
                start_time = input("Start time (HH:MM:SS): ").strip()
                end_time = input("End time (HH:MM:SS): ").strip()
                try:
                    capacity = int(input("Capacity: ").strip())
                except ValueError:
                    print("Error: Capacity must be a number.")
                    continue
                schedule_class_session(class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
        
        elif choice == "3":
            # OP8: Reschedule Class Session
            print("1. Manual Entry")
            print("2. Pre-filled Data")
            mode = input("Select mode: ").strip()
            if mode == "2":
                prefilled_reschedule_class_session()
            else:
                print("\n--- Reschedule Class Session ---")
                try:
                    session_id = int(input("Session ID: ").strip())
                except ValueError:
                    print("Error: Session ID must be a number.")
                    continue
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
                reschedule_class_session(session_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
