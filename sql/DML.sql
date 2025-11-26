-- ============================
--  ADMIN STAFF (3 staff)
-- ============================
INSERT INTO AdminStaff (admin_id, name, title, email, phone) VALUES
  (1, 'Sarah Johnson', 'Operations Manager', 'sarah.johnson@gym.com', '613-555-1001'),
  (2, 'David Lee', 'Front Desk Supervisor', 'david.lee@gym.com', '613-555-1002'),
  (3, 'Amina Conte', 'Class Coordinator', 'amina.conte@gym.com', '613-555-1003');

-- ============================
--  TRAINERS (5 trainers)
-- ============================
INSERT INTO Trainer (trainer_id, name, specialization, email, phone) VALUES
  (1, 'Emily Carter', 'Strength & Conditioning', 'emily.carter@gym.com', '613-555-2001'),
  (2, 'James Miller', 'Yoga & Mobility', 'james.miller@gym.com', '613-555-2002'),
  (3, 'Alex Nguyen', 'HIIT & Cardio', 'alex.nguyen@gym.com', '613-555-2003'),
  (4, 'Rita Gomez', 'Pilates', 'rita.gomez@gym.com', '613-555-2004'),
  (5, 'Daniel Brooks', 'CrossFit', 'daniel.brooks@gym.com', '613-555-2005');

-- ============================
--  ROOMS (4 rooms)
-- ============================
INSERT INTO Room (room_id, name, location) VALUES
  (1, 'Studio A', 'First Floor'),
  (2, 'Studio B', 'First Floor'),
  (3, 'PT Room 1', 'Second Floor'),
  (4, 'PT Room 2', 'Second Floor');

-- ============================
--  MEMBERS (6 members)
-- ============================
INSERT INTO Member (member_id, first_name, last_name, date_of_birth, email, phone, goal_description, goal_target)
VALUES
  (1, 'Mariam', 'Diallo',  DATE '2002-05-14', 'mariam.diallo@example.com', '613-555-3001', 'Lose weight to 65kg', 65.0),
  (2, 'Owen', 'Clark',     DATE '1999-11-02', 'owen.clark@example.com', '613-555-3002', 'Improve cardio endurance', NULL),
  (3, 'Leila', 'Hassan',   DATE '2001-03-20', 'leila.hassan@example.com', '613-555-3003', 'Gain muscle to 70kg', 70.0),
  (4, 'Samuel', 'Barton',  DATE '1998-07-10', 'sam.barton@example.com',   '613-555-3004', 'Build core stability', NULL),
  (5, 'Nadia', 'Koulibaly',DATE '2003-12-01', 'nadia.koulibaly@example.com','613-555-3005', 'Reduce stress with yoga', NULL),
  (6, 'Ibrahim','Sow',     DATE '1997-09-18', 'ibrahim.sow@example.com',  '613-555-3006', 'Improve flexibility', NULL);

-- ============================
--  CLASSES (6 template classes)
-- ============================
INSERT INTO Class (class_id, name, description, difficulty, category, duration_minutes, admin_id, assigned_since)
VALUES
  (1, 'Morning Yoga', 'Gentle flexibility and breathing', 'Easy', 'Yoga', 60, 3, DATE '2024-09-01'),
  (2, 'HIIT Express', 'High intensity interval training', 'Hard', 'Cardio', 45, 1, DATE '2024-09-01'),
  (3, 'Strength Basics', 'Full-body strength for beginners', 'Medium', 'Strength', 60, 2, DATE '2024-10-01'),
  (4, 'Pilates Flow', 'Core strength and balance', 'Medium', 'Pilates', 55, 3, DATE '2024-10-10'),
  (5, 'CrossFit Starter', 'Intro to CrossFit movements', 'Hard', 'CrossFit', 50, 1, DATE '2024-11-01'),
  (6, 'Evening Relax Yoga', 'Relaxing slow breathing and stretching', 'Easy', 'Yoga', 45, 3, DATE '2024-11-05');

-- ============================
--  CLASS SESSIONS (10 scheduled sessions)
-- ============================
INSERT INTO ClassSession (session_id, class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
VALUES
  -- Yoga
  (1, 1, 1, 2, DATE '2025-11-27', TIME '09:00', TIME '10:00', 20),
  (2, 6, 1, 2, DATE '2025-11-27', TIME '19:00', TIME '19:45', 20),

  -- HIIT
  (3, 2, 2, 3, DATE '2025-11-27', TIME '18:00', TIME '18:45', 25),
  (4, 2, 2, 3, DATE '2025-11-28', TIME '18:00', TIME '18:45', 25),

  -- Strength
  (5, 3, 3, 1, DATE '2025-11-29', TIME '10:00', TIME '11:00', 12),

  -- Pilates
  (6, 4, 1, 4, DATE '2025-11-30', TIME '11:00', TIME '12:00', 15),

  -- CrossFit
  (7, 5, 2, 5, DATE '2025-11-30', TIME '09:00', TIME '09:50', 18),
  (8, 5, 2, 5, DATE '2025-12-01', TIME '09:00', TIME '09:50', 18),

  -- More strength sessions
  (9, 3, 3, 1, DATE '2025-12-02', TIME '14:00', TIME '15:00', 12),
  (10, 3, 4, 1, DATE '2025-12-03', TIME '14:00', TIME '15:00', 12);

-- ============================
--  MEMBER CLASS REGISTRATIONS (12 registrations)
-- ============================
INSERT INTO MemberClassRegistration (registration_id, member_id, session_id)
VALUES
  (1, 1, 1), (2, 2, 1), (3, 3, 1),  -- 3 members in Morning Yoga
  (4, 4, 3), (5, 5, 3),             -- HIIT
  (6, 2, 2),                        -- Owen in Evening Yoga
  (7, 1, 5), (8, 3, 5),             -- Strength Basics
  (9, 6, 2),                        -- Ibrahim in Evening Yoga
  (10, 5, 6),                       -- Nadia in Pilates
  (11, 4, 7),                       -- Samuel in CrossFit
  (12, 2, 9);                       -- Owen in another Strength session

-- ============================
--  HEALTH METRICS (15 total)
-- ============================
INSERT INTO HealthMetric (metric_id, member_id, metric_type, value, recorded_at)
VALUES
  -- Mariam
  (1, 1, 'weight', 72.5, TIMESTAMP '2025-11-01 09:00'),
  (2, 1, 'weight', 70.8, TIMESTAMP '2025-11-15 09:00'),
  (3, 1, 'weight', 69.9, TIMESTAMP '2025-11-25 09:00'),

  -- Owen
  (4, 2, 'resting_heart_rate', 78.0, TIMESTAMP '2025-11-10 08:30'),
  (5, 2, 'resting_heart_rate', 75.0, TIMESTAMP '2025-11-20 08:30'),

  -- Leila
  (6, 3, 'weight', 64.0, TIMESTAMP '2025-11-05 10:00'),
  (7, 3, 'weight', 65.5, TIMESTAMP '2025-11-20 10:00'),

  -- Samuel
  (8, 4, 'core_strength_score', 40, TIMESTAMP '2025-11-08 14:00'),
  (9, 4, 'core_strength_score', 48, TIMESTAMP '2025-11-22 14:00'),

  -- Nadia
  (10, 5, 'stress_level', 8, TIMESTAMP '2025-11-03 17:00'),
  (11, 5, 'stress_level', 6, TIMESTAMP '2025-11-18 17:00'),

  -- Ibrahim
  (12, 6, 'flexibility_score', 30, TIMESTAMP '2025-11-06 18:00'),
  (13, 6, 'flexibility_score', 35, TIMESTAMP '2025-11-20 18:00'),
  (14, 6, 'flexibility_score', 37, TIMESTAMP '2025-11-25 18:00'),
  (15, 6, 'flexibility_score', 39, TIMESTAMP '2025-11-27 18:00');

-- ============================
--  TRAINER AVAILABILITY (12 entries)
-- ============================
INSERT INTO TrainerAvailability (availability_id, trainer_id, day_of_week, start_time, end_time)
VALUES
  -- James (Yoga)
  (1, 2, 'Thursday', TIME '08:00', TIME '12:00'),
  (2, 2, 'Friday',   TIME '08:00', TIME '12:00'),

  -- Emily (Strength)
  (3, 1, 'Monday',   TIME '14:00', TIME '18:00'),
  (4, 1, 'Wednesday',TIME '14:00', TIME '18:00'),
  (5, 1, 'Saturday', TIME '09:00', TIME '13:00'),

  -- Alex (HIIT)
  (6, 3, 'Thursday', TIME '17:00', TIME '20:00'),
  (7, 3, 'Friday',   TIME '17:00', TIME '20:00'),

  -- Rita (Pilates)
  (8, 4, 'Sunday',   TIME '09:00', TIME '12:00'),
  (9, 4, 'Tuesday',  TIME '16:00', TIME '19:00'),

  -- Daniel (CrossFit)
  (10, 5, 'Monday',  TIME '06:00', TIME '09:00'),
  (11, 5, 'Wednesday',TIME '06:00', TIME '09:00'),
  (12, 5, 'Friday',  TIME '06:00', TIME '09:00');
