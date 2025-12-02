from operations import *
import sys
import os

# Add prefilled module to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
        print("2. Update Member Profile")
        print("3. Log Health Metric")
        print("4. Register for Class Session")
        print("5. Back to Main Menu")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            # OP1: Register Member
            mode = input("Use (1) Manual Entry or (2) Pre-filled Data? ").strip()
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
            # OP2: Update Member Profile
            mode = input("Use (1) Manual Entry or (2) Pre-filled Data? ").strip()
            if mode == "2":
                prefilled_update_member_profile()
            else:
                print("\n--- Update Member Profile ---")
                try:
                    member_id = int(input("Member ID: ").strip())
                except ValueError:
                    print("Error: Member ID must be a number.")
                    continue
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
                update_member_profile(member_id, first_name, last_name, phone, goal_description, goal_target)
        
        elif choice == "3":
            # OP3: Log Health Metric
            mode = input("Use (1) Manual Entry or (2) Pre-filled Data? ").strip()
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
            mode = input("Use (1) Manual Entry or (2) Pre-filled Data? ").strip()
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
        print("1. Set Trainer Availability")
        print("2. View Trainer Schedule")
        print("3. Back to Main Menu")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            # OP5: Set Trainer Availability
            mode = input("Use (1) Manual Entry or (2) Pre-filled Data? ").strip()
            if mode == "2":
                prefilled_set_trainer_availability()
            else:
                print("\n--- Set Trainer Availability ---")
                try:
                    trainer_id = int(input("Trainer ID: ").strip())
                except ValueError:
                    print("Error: Trainer ID must be a number.")
                    continue
                day_of_week = input("Day of week (e.g., Monday): ").strip()
                start_time = input("Start time (HH:MM:SS): ").strip()
                end_time = input("End time (HH:MM:SS): ").strip()
                set_trainer_availability(trainer_id, day_of_week, start_time, end_time)
        
        elif choice == "2":
            # OP6: View Trainer Schedule
            mode = input("Use (1) Manual Entry or (2) Pre-filled Data? ").strip()
            if mode == "2":
                prefilled_view_trainer_schedule()
            else:
                print("\n--- View Trainer Schedule ---")
                try:
                    trainer_id = int(input("Trainer ID: ").strip())
                except ValueError:
                    print("Error: Trainer ID must be a number.")
                    continue
                from_date = input("From date (YYYY-MM-DD) or press Enter for today: ").strip() or None
                view_trainer_schedule(trainer_id, from_date)
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Try again.")


def admin_menu():
    while True:
        print("\n--- ADMIN OPERATIONS ---")
        print("1. Create Class Template")
        print("2. Update Class Template")
        print("3. Schedule Class Session")
        print("4. Reschedule Class Session")
        print("5. Back to Main Menu")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            # OP7: Create Class
            prefilled_create_class()
        
        elif choice == "2":
            # OP7: Update Class
            prefilled_update_class()
        
        elif choice == "3":
            # OP8: Schedule Class Session
            prefilled_schedule_class_session()
        
        elif choice == "4":
            # OP8: Reschedule Class Session
            prefilled_reschedule_class_session()
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
