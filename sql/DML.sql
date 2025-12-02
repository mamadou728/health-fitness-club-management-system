-- ============================
--  ADMIN STAFF (3 staff)
-- ============================
INSERT INTO AdminStaff (name, title, email, phone) VALUES
  ('Sarah Johnson', 'Operations Manager', 'sarah.johnson@gym.com', '613-555-1001'),
  ('David Lee', 'Front Desk Supervisor', 'david.lee@gym.com', '613-555-1002'),
  ('Amina Conte', 'Class Coordinator', 'amina.conte@gym.com', '613-555-1003');

-- ============================
--  TRAINERS (5 trainers)
-- ============================
INSERT INTO Trainer (name, specialization, email, phone) VALUES
  ('Emily Carter', 'Strength & Conditioning', 'emily.carter@gym.com', '613-555-2001'),
  ('James Miller', 'Yoga & Mobility', 'james.miller@gym.com', '613-555-2002'),
  ('Alex Nguyen', 'HIIT & Cardio', 'alex.nguyen@gym.com', '613-555-2003'),
  ('Rita Gomez', 'Pilates', 'rita.gomez@gym.com', '613-555-2004'),
  ('Daniel Brooks', 'CrossFit', 'daniel.brooks@gym.com', '613-555-2005');

-- ============================
--  ROOMS (4 rooms)
-- ============================
INSERT INTO Room (name, location) VALUES
  ('Studio A', 'First Floor'),
  ('Studio B', 'First Floor'),
  ('PT Room 1', 'Second Floor'),
  ('PT Room 2', 'Second Floor');

-- ============================
--  MEMBERS (6 members)
-- ============================
INSERT INTO Member (first_name, last_name, date_of_birth, email, phone, goal_description, goal_target)
VALUES
  ('Mariam', 'Diallo',  DATE '2002-05-14', 'mariam.diallo@example.com', '613-555-3001', 'Lose weight to 65kg', 65.0),
  ('Owen', 'Clark',     DATE '1999-11-02', 'owen.clark@example.com', '613-555-3002', 'Improve cardio endurance', NULL),
  ('Leila', 'Hassan',   DATE '2001-03-20', 'leila.hassan@example.com', '613-555-3003', 'Gain muscle to 70kg', 70.0),
  ('Samuel', 'Barton',  DATE '1998-07-10', 'sam.barton@example.com',   '613-555-3004', 'Build core stability', NULL),
  ('Nadia', 'Koulibaly',DATE '2003-12-01', 'nadia.koulibaly@example.com','613-555-3005', 'Reduce stress with yoga', NULL),
  ('Ibrahim','Sow',     DATE '1997-09-18', 'ibrahim.sow@example.com',  '613-555-3006', 'Improve flexibility', NULL);

-- ============================
--  CLASSES (6 template classes)
-- ============================
INSERT INTO Class (name, description, difficulty, category, duration_minutes, admin_id, assigned_since)
VALUES
  ('Morning Yoga', 'Gentle flexibility and breathing', 'Easy', 'Yoga', 60, (SELECT admin_id FROM AdminStaff WHERE email = 'amina.conte@gym.com'), DATE '2024-09-01'),
  ('HIIT Express', 'High intensity interval training', 'Hard', 'Cardio', 45, (SELECT admin_id FROM AdminStaff WHERE email = 'sarah.johnson@gym.com'), DATE '2024-09-01'),
  ('Strength Basics', 'Full-body strength for beginners', 'Medium', 'Strength', 60, (SELECT admin_id FROM AdminStaff WHERE email = 'david.lee@gym.com'), DATE '2024-10-01'),
  ('Pilates Flow', 'Core strength and balance', 'Medium', 'Pilates', 55, (SELECT admin_id FROM AdminStaff WHERE email = 'amina.conte@gym.com'), DATE '2024-10-10'),
  ('CrossFit Starter', 'Intro to CrossFit movements', 'Hard', 'CrossFit', 50, (SELECT admin_id FROM AdminStaff WHERE email = 'sarah.johnson@gym.com'), DATE '2024-11-01'),
  ('Evening Relax Yoga', 'Relaxing slow breathing and stretching', 'Easy', 'Yoga', 45, (SELECT admin_id FROM AdminStaff WHERE email = 'amina.conte@gym.com'), DATE '2024-11-05');

-- ============================
--  CLASS SESSIONS (10 scheduled sessions)
-- ============================
INSERT INTO ClassSession (class_id, room_id, trainer_id, session_date, start_time, end_time, capacity)
VALUES
  -- Yoga
  ((SELECT class_id FROM Class WHERE name = 'Morning Yoga'), (SELECT room_id FROM Room WHERE name = 'Studio A'), (SELECT trainer_id FROM Trainer WHERE email = 'james.miller@gym.com'), DATE '2025-11-27', TIME '09:00', TIME '10:00', 20),
  ((SELECT class_id FROM Class WHERE name = 'Evening Relax Yoga'), (SELECT room_id FROM Room WHERE name = 'Studio A'), (SELECT trainer_id FROM Trainer WHERE email = 'james.miller@gym.com'), DATE '2025-11-27', TIME '19:00', TIME '19:45', 20),

  -- HIIT
  ((SELECT class_id FROM Class WHERE name = 'HIIT Express'), (SELECT room_id FROM Room WHERE name = 'Studio B'), (SELECT trainer_id FROM Trainer WHERE email = 'alex.nguyen@gym.com'), DATE '2025-11-27', TIME '18:00', TIME '18:45', 25),
  ((SELECT class_id FROM Class WHERE name = 'HIIT Express'), (SELECT room_id FROM Room WHERE name = 'Studio B'), (SELECT trainer_id FROM Trainer WHERE email = 'alex.nguyen@gym.com'), DATE '2025-11-28', TIME '18:00', TIME '18:45', 25),

  -- Strength
  ((SELECT class_id FROM Class WHERE name = 'Strength Basics'), (SELECT room_id FROM Room WHERE name = 'PT Room 1'), (SELECT trainer_id FROM Trainer WHERE email = 'emily.carter@gym.com'), DATE '2025-11-29', TIME '10:00', TIME '11:00', 12),

  -- Pilates
  ((SELECT class_id FROM Class WHERE name = 'Pilates Flow'), (SELECT room_id FROM Room WHERE name = 'Studio A'), (SELECT trainer_id FROM Trainer WHERE email = 'rita.gomez@gym.com'), DATE '2025-11-30', TIME '11:00', TIME '12:00', 15),

  -- CrossFit
  ((SELECT class_id FROM Class WHERE name = 'CrossFit Starter'), (SELECT room_id FROM Room WHERE name = 'Studio B'), (SELECT trainer_id FROM Trainer WHERE email = 'daniel.brooks@gym.com'), DATE '2025-11-30', TIME '09:00', TIME '09:50', 18),
  ((SELECT class_id FROM Class WHERE name = 'CrossFit Starter'), (SELECT room_id FROM Room WHERE name = 'Studio B'), (SELECT trainer_id FROM Trainer WHERE email = 'daniel.brooks@gym.com'), DATE '2025-12-01', TIME '09:00', TIME '09:50', 18),

  -- More strength sessions
  ((SELECT class_id FROM Class WHERE name = 'Strength Basics'), (SELECT room_id FROM Room WHERE name = 'PT Room 1'), (SELECT trainer_id FROM Trainer WHERE email = 'emily.carter@gym.com'), DATE '2025-12-02', TIME '14:00', TIME '15:00', 12),
  ((SELECT class_id FROM Class WHERE name = 'Strength Basics'), (SELECT room_id FROM Room WHERE name = 'PT Room 2'), (SELECT trainer_id FROM Trainer WHERE email = 'emily.carter@gym.com'), DATE '2025-12-03', TIME '14:00', TIME '15:00', 12);

-- ============================
--  MEMBER CLASS REGISTRATIONS (12 registrations)
-- ============================
INSERT INTO MemberClassRegistration (member_id, session_id)
VALUES
  -- 3 members in Morning Yoga (session 1)
  ((SELECT member_id FROM Member WHERE email = 'mariam.diallo@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Morning Yoga') AND session_date = DATE '2025-11-27' AND start_time = TIME '09:00')),
  ((SELECT member_id FROM Member WHERE email = 'owen.clark@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Morning Yoga') AND session_date = DATE '2025-11-27' AND start_time = TIME '09:00')),
  ((SELECT member_id FROM Member WHERE email = 'leila.hassan@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Morning Yoga') AND session_date = DATE '2025-11-27' AND start_time = TIME '09:00')),
  
  -- HIIT (session 3)
  ((SELECT member_id FROM Member WHERE email = 'sam.barton@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'HIIT Express') AND session_date = DATE '2025-11-27')),
  ((SELECT member_id FROM Member WHERE email = 'nadia.koulibaly@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'HIIT Express') AND session_date = DATE '2025-11-27')),
  
  -- Owen in Evening Yoga
  ((SELECT member_id FROM Member WHERE email = 'owen.clark@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Evening Relax Yoga') AND session_date = DATE '2025-11-27')),
  
  -- Strength Basics (session 5)
  ((SELECT member_id FROM Member WHERE email = 'mariam.diallo@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Strength Basics') AND session_date = DATE '2025-11-29')),
  ((SELECT member_id FROM Member WHERE email = 'leila.hassan@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Strength Basics') AND session_date = DATE '2025-11-29')),
  
  -- Ibrahim in Evening Yoga
  ((SELECT member_id FROM Member WHERE email = 'ibrahim.sow@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Evening Relax Yoga') AND session_date = DATE '2025-11-27')),
  
  -- Nadia in Pilates
  ((SELECT member_id FROM Member WHERE email = 'nadia.koulibaly@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Pilates Flow') AND session_date = DATE '2025-11-30')),
  
  -- Samuel in CrossFit
  ((SELECT member_id FROM Member WHERE email = 'sam.barton@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'CrossFit Starter') AND session_date = DATE '2025-11-30' AND start_time = TIME '09:00')),
  
  -- Owen in another Strength session
  ((SELECT member_id FROM Member WHERE email = 'owen.clark@example.com'), (SELECT session_id FROM ClassSession WHERE class_id = (SELECT class_id FROM Class WHERE name = 'Strength Basics') AND session_date = DATE '2025-12-02'));

-- ============================
--  HEALTH METRICS (15 total)
-- ============================
INSERT INTO HealthMetric (member_id, metric_type, value, recorded_at)
VALUES
  -- Mariam
  ((SELECT member_id FROM Member WHERE email = 'mariam.diallo@example.com'), 'weight', 72.5, TIMESTAMP '2025-11-01 09:00'),
  ((SELECT member_id FROM Member WHERE email = 'mariam.diallo@example.com'), 'weight', 70.8, TIMESTAMP '2025-11-15 09:00'),
  ((SELECT member_id FROM Member WHERE email = 'mariam.diallo@example.com'), 'weight', 69.9, TIMESTAMP '2025-11-25 09:00'),

  -- Owen
  ((SELECT member_id FROM Member WHERE email = 'owen.clark@example.com'), 'resting_heart_rate', 78.0, TIMESTAMP '2025-11-10 08:30'),
  ((SELECT member_id FROM Member WHERE email = 'owen.clark@example.com'), 'resting_heart_rate', 75.0, TIMESTAMP '2025-11-20 08:30'),

  -- Leila
  ((SELECT member_id FROM Member WHERE email = 'leila.hassan@example.com'), 'weight', 64.0, TIMESTAMP '2025-11-05 10:00'),
  ((SELECT member_id FROM Member WHERE email = 'leila.hassan@example.com'), 'weight', 65.5, TIMESTAMP '2025-11-20 10:00'),

  -- Samuel
  ((SELECT member_id FROM Member WHERE email = 'sam.barton@example.com'), 'core_strength_score', 40, TIMESTAMP '2025-11-08 14:00'),
  ((SELECT member_id FROM Member WHERE email = 'sam.barton@example.com'), 'core_strength_score', 48, TIMESTAMP '2025-11-22 14:00'),

  -- Nadia
  ((SELECT member_id FROM Member WHERE email = 'nadia.koulibaly@example.com'), 'stress_level', 8, TIMESTAMP '2025-11-03 17:00'),
  ((SELECT member_id FROM Member WHERE email = 'nadia.koulibaly@example.com'), 'stress_level', 6, TIMESTAMP '2025-11-18 17:00'),

  -- Ibrahim
  ((SELECT member_id FROM Member WHERE email = 'ibrahim.sow@example.com'), 'flexibility_score', 30, TIMESTAMP '2025-11-06 18:00'),
  ((SELECT member_id FROM Member WHERE email = 'ibrahim.sow@example.com'), 'flexibility_score', 35, TIMESTAMP '2025-11-20 18:00'),
  ((SELECT member_id FROM Member WHERE email = 'ibrahim.sow@example.com'), 'flexibility_score', 37, TIMESTAMP '2025-11-25 18:00'),
  ((SELECT member_id FROM Member WHERE email = 'ibrahim.sow@example.com'), 'flexibility_score', 39, TIMESTAMP '2025-11-27 18:00');

-- ============================
--  TRAINER AVAILABILITY (12 entries)
-- ============================
INSERT INTO TrainerAvailability (trainer_id, day_of_week, start_time, end_time)
VALUES
  -- James (Yoga)
  ((SELECT trainer_id FROM Trainer WHERE email = 'james.miller@gym.com'), 'Thursday', TIME '08:00', TIME '12:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'james.miller@gym.com'), 'Friday',   TIME '08:00', TIME '12:00'),

  -- Emily (Strength)
  ((SELECT trainer_id FROM Trainer WHERE email = 'emily.carter@gym.com'), 'Monday',   TIME '14:00', TIME '18:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'emily.carter@gym.com'), 'Wednesday',TIME '14:00', TIME '18:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'emily.carter@gym.com'), 'Saturday', TIME '09:00', TIME '13:00'),

  -- Alex (HIIT)
  ((SELECT trainer_id FROM Trainer WHERE email = 'alex.nguyen@gym.com'), 'Thursday', TIME '17:00', TIME '20:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'alex.nguyen@gym.com'), 'Friday',   TIME '17:00', TIME '20:00'),

  -- Rita (Pilates)
  ((SELECT trainer_id FROM Trainer WHERE email = 'rita.gomez@gym.com'), 'Sunday',   TIME '09:00', TIME '12:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'rita.gomez@gym.com'), 'Tuesday',  TIME '16:00', TIME '19:00'),

  -- Daniel (CrossFit)
  ((SELECT trainer_id FROM Trainer WHERE email = 'daniel.brooks@gym.com'), 'Monday',  TIME '06:00', TIME '09:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'daniel.brooks@gym.com'), 'Wednesday',TIME '06:00', TIME '09:00'),
  ((SELECT trainer_id FROM Trainer WHERE email = 'daniel.brooks@gym.com'), 'Friday',  TIME '06:00', TIME '09:00');

