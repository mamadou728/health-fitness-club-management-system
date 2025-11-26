from operations import *

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
            print("\n--- Register New Member ---")
            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            email = input("Email: ").strip()
            date_of_birth = input("Date of birth (YYYY-MM-DD) or press Enter to skip: ").strip() or None
            phone = input("Phone or press Enter to skip: ").strip() or None
            goal_description = input("Goal description or press Enter to skip: ").strip() or None
            goal_target = input("Goal target (numeric) or press Enter to skip: ").strip()
            goal_target = float(goal_target) if goal_target else None
            
            register_member(first_name, last_name, date_of_birth, email, phone, goal_description, goal_target)
        
        elif choice == "2":
            # OP2: Update Member Profile
            print("\n--- Update Member Profile ---")
            member_id = int(input("Member ID: ").strip())
            print("Leave blank to keep current value:")
            first_name = input("New first name: ").strip() or None
            last_name = input("New last name: ").strip() or None
            phone = input("New phone: ").strip() or None
            goal_description = input("New goal description: ").strip() or None
            goal_target = input("New goal target: ").strip()
            goal_target = float(goal_target) if goal_target else None
            
            update_member_profile(member_id, first_name, last_name, phone, goal_description, goal_target)
        
        elif choice == "3":
            # OP3: Log Health Metric
            print("\n--- Log Health Metric ---")
            member_id = int(input("Member ID: ").strip())
            metric_type = input("Metric type (e.g., weight, heart_rate): ").strip()
            value = float(input("Value: ").strip())
            recorded_at = input("Recorded at (YYYY-MM-DD HH:MM:SS) or press Enter for now: ").strip() or None
            
            log_health_metric(member_id, metric_type, value, recorded_at)
        
        elif choice == "4":
            # OP4: Register for Class Session
            print("\n--- Register for Class Session ---")
            member_id = int(input("Member ID: ").strip())
            session_id = int(input("Session ID: ").strip())
            
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
            print("\n--- Set Trainer Availability ---")
            trainer_id = int(input("Trainer ID: ").strip())
            day_of_week = input("Day of week (e.g., Monday): ").strip()
            start_time = input("Start time (HH:MM:SS): ").strip()
            end_time = input("End time (HH:MM:SS): ").strip()
            
            set_trainer_availability(trainer_id, day_of_week, start_time, end_time)
        
        elif choice == "2":
            # OP6: View Trainer Schedule
            print("\n--- View Trainer Schedule ---")
            trainer_id = int(input("Trainer ID: ").strip())
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
            print("\n--- Create Class Template ---")
            admin_id = int(input("Admin ID: ").strip())
            name = input("Class name: ").strip()
            description = input("Description or press Enter to skip: ").strip() or None
            difficulty = input("Difficulty (Easy/Medium/Hard) or press Enter to skip: ").strip() or None
            category = input("Category or press Enter to skip: ").strip() or None
            duration = input("Duration (minutes) or press Enter to skip: ").strip()
            duration_minutes = int(duration) if duration else None
            
            create_class(admin_id, name, description, difficulty, category, duration_minutes)
        
        elif choice == "2":
            # OP7: Update Class
            print("\n--- Update Class Template ---")
            class_id = int(input("Class ID: ").strip())
            print("Leave blank to keep current value:")
            name = input("New class name: ").strip() or None
            description = input("New description: ").strip() or None
            difficulty = input("New difficulty: ").strip() or None
            category = input("New category: ").strip() or None
            duration = input("New duration (minutes): ").strip()
            duration_minutes = int(duration) if duration else None
            admin_id = input("New admin ID: ").strip()
            admin_id = int(admin_id) if admin_id else None
            
            update_class(class_id, name, description, difficulty, category, duration_minutes, admin_id)
        
        elif choice == "3":
            # OP8: Schedule Class Session
            print("\n--- Schedule Class Session ---")
            class_id = int(input("Class ID: ").strip())
            room_id = int(input("Room ID: ").strip())
            trainer_id = int(input("Trainer ID: ").strip())
            session_date = input("Session date (YYYY-MM-DD): ").strip()
            start_time = input("Start time (HH:MM:SS): ").strip()
            end_time = input("End time (HH:MM:SS): ").strip()
            capacity = int(input("Capacity: ").strip())
            
            schedule_class_session(class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
        
        elif choice == "4":
            # OP8: Reschedule Class Session
            print("\n--- Reschedule Class Session ---")
            session_id = int(input("Session ID: ").strip())
            print("Leave blank to keep current value:")
            room_id = input("New room ID: ").strip()
            room_id = int(room_id) if room_id else None
            trainer_id = input("New trainer ID: ").strip()
            trainer_id = int(trainer_id) if trainer_id else None
            session_date = input("New session date (YYYY-MM-DD): ").strip() or None
            start_time = input("New start time (HH:MM:SS): ").strip() or None
            end_time = input("New end time (HH:MM:SS): ").strip() or None
            capacity = input("New capacity: ").strip()
            capacity = int(capacity) if capacity else None
            
            reschedule_class_session(session_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
