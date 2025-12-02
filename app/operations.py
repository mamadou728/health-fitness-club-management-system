import psycopg2
from psycopg2 import sql

# Database connection helper
def get_connection():
    return psycopg2.connect(
        dbname="fitness_club",
        user="postgres",
        password="NewPassword123",
        host="localhost",
        port="5432"
    )


# OP1 – Member Registration
def register_member(first_name, last_name, date_of_birth, email, phone, goal_description, goal_target):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO Member (first_name, last_name, date_of_birth, email, phone, goal_description, goal_target)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING member_id;
        """, (first_name, last_name, date_of_birth, email, phone, goal_description, goal_target))
        
        member_id = cur.fetchone()[0]
        conn.commit()
        print(f"Success! Member registered with ID: {member_id}")
        return member_id
        
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print(f"Error: Email already exists or constraint violation - {e}")
        return None
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP2 – Search Member by Email (demonstrates INDEX: idx_member_email)
def search_member_by_email(email):

    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # This query uses the idx_member_email index for optimized search
        cur.execute("""
            SELECT member_id, first_name, last_name, date_of_birth, email, 
                   phone, registration_date, goal_description, goal_target
            FROM Member
            WHERE email = %s;
        """, (email,))
        
        result = cur.fetchone()
        
        if result:
            print(f"\n✓ Member found (using indexed email search):")
            print(f"  Member ID: {result[0]}")
            print(f"  Name: {result[1]} {result[2]}")
            print(f"  Email: {result[4]}")
            print(f"  Phone: {result[5]}")
            print(f"  DOB: {result[3]}")
            print(f"  Registered: {result[6]}")
            print(f"  Goal: {result[7]} (Target: {result[8]})")
            return result
        else:
            print(f"✗ No member found with email: {email}")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP3 – Log New Health Metric
def log_health_metric(member_id, metric_type, value, recorded_at=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if member exists
        cur.execute("SELECT 1 FROM Member WHERE member_id = %s", (member_id,))
        if not cur.fetchone():
            print(f"Error: Member ID {member_id} not found")
            return None
        
        cur.execute("""
            INSERT INTO HealthMetric (member_id, metric_type, value, recorded_at)
            VALUES (%s, %s, %s, COALESCE(%s, NOW()))
            RETURNING metric_id;
        """, (member_id, metric_type, value, recorded_at))
        
        metric_id = cur.fetchone()[0]
        conn.commit()
        print(f"Success! Health metric logged with ID: {metric_id}")
        return metric_id
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP4 – Register Member for a Class Session
def register_for_class_session(member_id, session_id):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if member exists
        cur.execute("SELECT 1 FROM Member WHERE member_id = %s", (member_id,))
        if not cur.fetchone():
            print(f"Error: Member ID {member_id} not found")
            return False
        
        # Check if session exists
        cur.execute("SELECT 1 FROM ClassSession WHERE session_id = %s", (session_id,))
        if not cur.fetchone():
            print(f"Error: Session ID {session_id} not found")
            return False
        
        # Check if already registered
        cur.execute("""
            SELECT 1 FROM MemberClassRegistration
            WHERE member_id = %s AND session_id = %s
        """, (member_id, session_id))
        if cur.fetchone():
            print("Error: Member already registered for this session")
            return False
        
        # Check capacity
        cur.execute("""
            SELECT capacity - COUNT(r.registration_id) AS remaining_spots
            FROM ClassSession cs
            LEFT JOIN MemberClassRegistration r ON cs.session_id = r.session_id
            WHERE cs.session_id = %s
            GROUP BY cs.capacity
        """, (session_id,))
        
        result = cur.fetchone()
        if result[0] <= 0:
            print("Error: No remaining spots - class is full")
            return False
        
        # Register member
        cur.execute("""
            INSERT INTO MemberClassRegistration (member_id, session_id)
            VALUES (%s, %s)
            RETURNING registration_id;
        """, (member_id, session_id))
        
        registration_id = cur.fetchone()[0]
        conn.commit()
        print(f"Success! Registered with ID: {registration_id}")
        return True
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return False
    finally:
        cur.close()
        conn.close()


# OP5 – Trainer Availability Time Validation (demonstrates TRIGGER)
def test_trainer_availability_validation(trainer_id, day_of_week, start_time, end_time):
    """
    Demonstrates the trg_check_trainer_availability_time trigger.
    The trigger validates that end_time > start_time.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if trainer exists
        cur.execute("SELECT name FROM Trainer WHERE trainer_id = %s", (trainer_id,))
        trainer = cur.fetchone()
        if not trainer:
            print(f"Error: Trainer ID {trainer_id} not found")
            return None
        
        print(f"\n→ Attempting to set availability for Trainer {trainer_id} ({trainer[0]})")
        print(f"  Day: {day_of_week}, Time: {start_time} - {end_time}")
        
        # This INSERT will trigger the validation
        cur.execute("""
            INSERT INTO TrainerAvailability (trainer_id, day_of_week, start_time, end_time)
            VALUES (%s, %s, %s, %s)
            RETURNING availability_id;
        """, (trainer_id, day_of_week, start_time, end_time))
        
        availability_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ SUCCESS! Trigger validation passed. Availability ID: {availability_id}")
        print(f"  The trigger confirmed: end_time ({end_time}) > start_time ({start_time})")
        return availability_id
        
    except psycopg2.Error as e:
        conn.rollback()
        error_msg = str(e)
        if "end_time must be after start_time" in error_msg:
            print(f"✗ TRIGGER BLOCKED: end_time must be after start_time")
            print(f"  The trigger prevented invalid data: {end_time} <= {start_time}")
        else:
            print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP6 – View Member Dashboard (demonstrates the VIEW operation)
def view_member_dashboard(member_id):
    """
    Query the MemberDashboardSimple view to display member statistics.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT member_id, first_name, last_name, goal_description, 
                   goal_target, last_metric_value, total_classes_registered
            FROM MemberDashboardSimple
            WHERE member_id = %s;
        """, (member_id,))
        
        result = cur.fetchone()
        
        if result:
            print(f"\n=== Member Dashboard (from MemberDashboardSimple VIEW) ===")
            print(f"Member ID: {result[0]}")
            print(f"Name: {result[1]} {result[2]}")
            print(f"Goal: {result[3]}")
            print(f"Target: {result[4]}")
            print(f"Last Metric Value: {result[5] if result[5] else 'No metrics logged'}")
            print(f"Total Classes Registered: {result[6]}")
            print("=" * 60)
            return result
        else:
            print(f"✗ No member found with ID: {member_id}")
            return None
                
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP7 – Admin: Create or Update a Class Template
def create_class(admin_id, name, description=None, difficulty=None, category=None, duration_minutes=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if admin exists
        cur.execute("SELECT 1 FROM AdminStaff WHERE admin_id = %s", (admin_id,))
        if not cur.fetchone():
            print(f"Error: Admin ID {admin_id} not found")
            return None
        
        cur.execute("""
            INSERT INTO Class (name, description, difficulty, category, duration_minutes, admin_id, assigned_since)
            VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE)
            RETURNING class_id;
        """, (name, description, difficulty, category, duration_minutes, admin_id))
        
        class_id = cur.fetchone()[0]
        conn.commit()
        print(f"Success! Class created with ID: {class_id}")
        return class_id
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP8 – Admin: Schedule / Reschedule Class Session (Room Booking)
def schedule_class_session(class_id, room_id, trainer_id, session_date, start_time, end_time, capacity):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if class exists
        cur.execute("SELECT 1 FROM Class WHERE class_id = %s", (class_id,))
        if not cur.fetchone():
            print(f"Error: Class ID {class_id} not found")
            return None
        
        # Check if room exists
        cur.execute("SELECT 1 FROM Room WHERE room_id = %s", (room_id,))
        if not cur.fetchone():
            print(f"Error: Room ID {room_id} not found")
            return None
        
        # Check if trainer exists
        cur.execute("SELECT 1 FROM Trainer WHERE trainer_id = %s", (trainer_id,))
        if not cur.fetchone():
            print(f"Error: Trainer ID {trainer_id} not found")
            return None
        
        # Check trainer availability
        # Get day name from session_date
        cur.execute("SELECT TO_CHAR(%s::date, 'Day')", (session_date,))
        day_name = cur.fetchone()[0].strip()
        
        cur.execute("""
            SELECT 1
            FROM TrainerAvailability
            WHERE trainer_id = %s
              AND day_of_week = %s
              AND %s >= start_time
              AND %s <= end_time
            LIMIT 1;
        """, (trainer_id, day_name, start_time, end_time))
        
        if not cur.fetchone():
            print(f"Error: Trainer not available on {day_name} at that time")
            return None
        
        # Check room conflict
        cur.execute("""
            SELECT 1
            FROM ClassSession
            WHERE room_id = %s
              AND session_date = %s
              AND NOT (
                    %s >= end_time
                    OR
                    %s <= start_time
                  )
            LIMIT 1;
        """, (room_id, session_date, start_time, end_time))
        
        if cur.fetchone():
            print("Error: Room already booked in that time range")
            return None
        
        # Insert session
        cur.execute("""
            INSERT INTO ClassSession (class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING session_id;
        """, (class_id, room_id, trainer_id, session_date, start_time, end_time, capacity))
        
        session_id = cur.fetchone()[0]
        conn.commit()
        print(f"Success! Class session scheduled with ID: {session_id}")
        return session_id
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


def reschedule_class_session(session_id, room_id=None, trainer_id=None, session_date=None, start_time=None, end_time=None, capacity=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if session exists and get current values
        cur.execute("""
            SELECT room_id, session_date, start_time, end_time
            FROM ClassSession
            WHERE session_id = %s
        """, (session_id,))
        
        result = cur.fetchone()
        if not result:
            print(f"Error: Session ID {session_id} not found")
            return False
        
        # Use current values if not provided
        current_room_id, current_date, current_start, current_end = result
        new_room_id = room_id if room_id is not None else current_room_id
        new_date = session_date if session_date is not None else current_date
        new_start = start_time if start_time is not None else current_start
        new_end = end_time if end_time is not None else current_end
        
        # Check trainer availability if trainer_id is being changed or date/time is being changed
        if trainer_id is not None or session_date is not None or start_time is not None or end_time is not None:
            # Get the trainer_id to check (new or current)
            check_trainer_id = trainer_id if trainer_id is not None else None
            if check_trainer_id is None:
                cur.execute("SELECT trainer_id FROM ClassSession WHERE session_id = %s", (session_id,))
                check_trainer_id = cur.fetchone()[0]
            
            # Get day name from session_date
            cur.execute("SELECT TO_CHAR(%s::date, 'Day')", (new_date,))
            day_name = cur.fetchone()[0].strip()
            
            cur.execute("""
                SELECT 1
                FROM TrainerAvailability
                WHERE trainer_id = %s
                  AND day_of_week = %s
                  AND %s >= start_time
                  AND %s <= end_time
                LIMIT 1;
            """, (check_trainer_id, day_name, new_start, new_end))
            
            if not cur.fetchone():
                print(f"Error: Trainer not available on {day_name} at that time")
                return False
        
        # Check room conflict (excluding current session)
        cur.execute("""
            SELECT 1
            FROM ClassSession
            WHERE room_id = %s
              AND session_date = %s
              AND session_id != %s
              AND NOT (
                    %s >= end_time
                    OR
                    %s <= start_time
                  )
            LIMIT 1;
        """, (new_room_id, new_date, session_id, new_start, new_end))
        
        if cur.fetchone():
            print("Error: Room already booked in that time range")
            return False
        
        # Build update query dynamically
        updates = []
        values = []
        
        if room_id is not None:
            updates.append("room_id = %s")
            values.append(room_id)
        if trainer_id is not None:
            updates.append("trainer_id = %s")
            values.append(trainer_id)
        if session_date is not None:
            updates.append("session_date = %s")
            values.append(session_date)
        if start_time is not None:
            updates.append("start_time = %s")
            values.append(start_time)
        if end_time is not None:
            updates.append("end_time = %s")
            values.append(end_time)
        if capacity is not None:
            updates.append("capacity = %s")
            values.append(capacity)
        
        if not updates:
            print("Error: No fields provided to update")
            return False
        
        values.append(session_id)
        query = f"UPDATE ClassSession SET {', '.join(updates)} WHERE session_id = %s"
        
        cur.execute(query, values)
        conn.commit()
        print(f"Success! Session {session_id} rescheduled")
        return True
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return False
    finally:
        cur.close()
        conn.close()
