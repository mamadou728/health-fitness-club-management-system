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
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING member_id;
        """, (first_name, last_name, date_of_birth, email, phone, goal_description, goal_target))
        member_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Member registered: ID {member_id}")
        return member_id
    except psycopg2.IntegrityError:
        conn.rollback()
        print("✗ Error: Email already exists")
        return None
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP2 – Search Member by Email (demonstrates INDEX: idx_member_email)
def search_member_by_email(email):

    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT member_id, first_name, last_name, email, phone
            FROM Member WHERE email = %s;
        """, (email,))
        result = cur.fetchone()
        if result:
            print(f"✓ Found: {result[1]} {result[2]} (ID: {result[0]})")
            return result
        else:
            print(f"✗ Not found: {email}")
            return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP3 – Log New Health Metric
def log_health_metric(member_id, metric_type, value, recorded_at=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO HealthMetric (member_id, metric_type, value, recorded_at)
            VALUES (%s, %s, %s, COALESCE(%s, NOW())) RETURNING metric_id;
        """, (member_id, metric_type, value, recorded_at))
        metric_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Metric logged: ID {metric_id}")
        return metric_id
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP4 – Register Member for a Class Session
def register_for_class_session(member_id, session_id):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO MemberClassRegistration (member_id, session_id)
            VALUES (%s, %s) RETURNING registration_id;
        """, (member_id, session_id))
        registration_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Registered: ID {registration_id}")
        return True
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
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
        cur.execute("""
            INSERT INTO TrainerAvailability (trainer_id, day_of_week, start_time, end_time)
            VALUES (%s, %s, %s, %s) RETURNING availability_id;
        """, (trainer_id, day_of_week, start_time, end_time))
        availability_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Availability set: ID {availability_id} (Trigger validated times)")
        return availability_id
    except psycopg2.Error as e:
        conn.rollback()
        if "end_time must be after start_time" in str(e):
            print(f"✗ Trigger blocked: Invalid time range")
        else:
            print(f"✗ Error: {e}")
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
            SELECT member_id, first_name, last_name, last_metric_value, total_classes_registered
            FROM MemberDashboardSimple WHERE member_id = %s;
        """, (member_id,))
        result = cur.fetchone()
        if result:
            print(f"✓ Dashboard: {result[1]} {result[2]} | Metric: {result[3]} | Classes: {result[4]}")
            return result
        else:
            print(f"✗ Not found: Member ID {member_id}")
            return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP7 – Admin: Create or Update a Class Template
def create_class(admin_id, name, description=None, difficulty=None, category=None, duration_minutes=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO Class (name, description, difficulty, category, duration_minutes, admin_id, assigned_since)
            VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE) RETURNING class_id;
        """, (name, description, difficulty, category, duration_minutes, admin_id))
        class_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Class created: ID {class_id}")
        return class_id
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP8 – Admin: Schedule / Reschedule Class Session (Room Booking)
def schedule_class_session(class_id, room_id, trainer_id, session_date, start_time, end_time, capacity):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO ClassSession (class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING session_id;
        """, (class_id, room_id, trainer_id, session_date, start_time, end_time, capacity))
        session_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Session scheduled: ID {session_id}")
        return session_id
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()
