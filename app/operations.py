import psycopg2
from psycopg2 import sql

# Database connection helper
def get_connection():
    return psycopg2.connect(
        dbname="fitness_club",
        user="postgres",
        password="your_password",
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


# OP2 – Update Member Profile & Goal
def update_member_profile(member_id, first_name=None, last_name=None, phone=None, goal_description=None, goal_target=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if member exists
        cur.execute("SELECT 1 FROM Member WHERE member_id = %s", (member_id,))
        if not cur.fetchone():
            print(f"Error: Member ID {member_id} not found")
            return False
        
        # Build update query dynamically
        updates = []
        values = []
        
        if first_name is not None:
            updates.append("first_name = %s")
            values.append(first_name)
        if last_name is not None:
            updates.append("last_name = %s")
            values.append(last_name)
        if phone is not None:
            updates.append("phone = %s")
            values.append(phone)
        if goal_description is not None:
            updates.append("goal_description = %s")
            values.append(goal_description)
        if goal_target is not None:
            updates.append("goal_target = %s")
            values.append(goal_target)
        
        if not updates:
            print("Error: No fields provided to update")
            return False
        
        values.append(member_id)
        query = f"UPDATE Member SET {', '.join(updates)} WHERE member_id = %s"
        
        cur.execute(query, values)
        conn.commit()
        print(f"Success! Member {member_id} profile updated")
        return True
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return False
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


# OP5 – Set Trainer Availability
def set_trainer_availability(trainer_id, day_of_week, start_time, end_time):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if trainer exists
        cur.execute("SELECT 1 FROM Trainer WHERE trainer_id = %s", (trainer_id,))
        if not cur.fetchone():
            print(f"Error: Trainer ID {trainer_id} not found")
            return None
        
        # Check overlapping availability for same trainer and day
        cur.execute("""
            SELECT 1
            FROM TrainerAvailability
            WHERE trainer_id = %s
              AND day_of_week = %s
              AND NOT (
                    %s >= end_time
                    OR
                    %s <= start_time
                  )
            LIMIT 1;
        """, (trainer_id, day_of_week, start_time, end_time))
        
        if cur.fetchone():
            print("Error: Availability overlaps with an existing time slot")
            return None
        
        cur.execute("""
            INSERT INTO TrainerAvailability (trainer_id, day_of_week, start_time, end_time)
            VALUES (%s, %s, %s, %s)
            RETURNING availability_id;
        """, (trainer_id, day_of_week, start_time, end_time))
        
        availability_id = cur.fetchone()[0]
        conn.commit()
        print(f"Success! Availability set with ID: {availability_id}")
        return availability_id
        
    except psycopg2.Error as e:
        conn.rollback()
        if "end_time must be after start_time" in str(e):
            print("Error: end_time must be after start_time")
        else:
            print(f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# OP6 – View Trainer Schedule (Upcoming Sessions)
def view_trainer_schedule(trainer_id, from_date=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if trainer exists
        cur.execute("SELECT 1 FROM Trainer WHERE trainer_id = %s", (trainer_id,))
        if not cur.fetchone():
            print(f"Error: Trainer ID {trainer_id} not found")
            return None
        
        cur.execute("""
            SELECT
                cs.session_id,
                cs.session_date,
                cs.start_time,
                cs.end_time,
                c.name AS class_name,
                r.name AS room_name,
                r.location
            FROM ClassSession cs
            JOIN Class c ON cs.class_id = c.class_id
            LEFT JOIN Room r ON cs.room_id = r.room_id
            WHERE cs.trainer_id = %s
              AND cs.session_date >= COALESCE(%s, CURRENT_DATE)
            ORDER BY cs.session_date, cs.start_time;
        """, (trainer_id, from_date))
        
        sessions = cur.fetchall()
        
        if sessions:
            print(f"\nUpcoming sessions for Trainer {trainer_id}:")
            for session in sessions:
                print(f"  Session {session[0]}: {session[1]} {session[2]}-{session[3]} | {session[4]} | Room: {session[5]} ({session[6]})")
        else:
            print(f"No upcoming sessions for Trainer {trainer_id}")
        
        return sessions
        
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


def update_class(class_id, name=None, description=None, difficulty=None, category=None, duration_minutes=None, admin_id=None):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Check if class exists
        cur.execute("SELECT 1 FROM Class WHERE class_id = %s", (class_id,))
        if not cur.fetchone():
            print(f"Error: Class ID {class_id} not found")
            return False
        
        # Build update query dynamically
        updates = []
        values = []
        
        if name is not None:
            updates.append("name = %s")
            values.append(name)
        if description is not None:
            updates.append("description = %s")
            values.append(description)
        if difficulty is not None:
            updates.append("difficulty = %s")
            values.append(difficulty)
        if category is not None:
            updates.append("category = %s")
            values.append(category)
        if duration_minutes is not None:
            updates.append("duration_minutes = %s")
            values.append(duration_minutes)
        if admin_id is not None:
            updates.append("admin_id = %s")
            values.append(admin_id)
        
        if not updates:
            print("Error: No fields provided to update")
            return False
        
        values.append(class_id)
        query = f"UPDATE Class SET {', '.join(updates)} WHERE class_id = %s"
        
        cur.execute(query, values)
        conn.commit()
        print(f"Success! Class {class_id} updated")
        return True
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return False
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
