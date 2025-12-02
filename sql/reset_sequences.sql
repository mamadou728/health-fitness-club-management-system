-- ============================
--  RESET SEQUENCES
--  Run this after manually inserting data with explicit IDs
-- ============================
SELECT setval('adminstaff_admin_id_seq', (SELECT MAX(admin_id) FROM AdminStaff));
SELECT setval('trainer_trainer_id_seq', (SELECT MAX(trainer_id) FROM Trainer));
SELECT setval('room_room_id_seq', (SELECT MAX(room_id) FROM Room));
SELECT setval('member_member_id_seq', (SELECT MAX(member_id) FROM Member));
SELECT setval('class_class_id_seq', (SELECT MAX(class_id) FROM Class));
SELECT setval('classsession_session_id_seq', (SELECT MAX(session_id) FROM ClassSession));
SELECT setval('memberclassregistration_registration_id_seq', (SELECT MAX(registration_id) FROM MemberClassRegistration));
SELECT setval('healthmetric_metric_id_seq', (SELECT MAX(metric_id) FROM HealthMetric));
SELECT setval('traineravailability_availability_id_seq', (SELECT MAX(availability_id) FROM TrainerAvailability));
