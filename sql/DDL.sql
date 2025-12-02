-- =========
--  CORE TABLES
-- =========

-- Members of the club
CREATE TABLE Member (
    member_id       SERIAL PRIMARY KEY,
    first_name      VARCHAR(50)  NOT NULL,
    last_name       VARCHAR(50)  NOT NULL,
    date_of_birth   DATE,
    email           VARCHAR(255) NOT NULL UNIQUE,
    phone           VARCHAR(30),
    registration_date TIMESTAMP DEFAULT NOW(),
    goal_description TEXT,
    goal_target     NUMERIC(10,2)
);

-- Trainers
CREATE TABLE Trainer (
    trainer_id      SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    specialization  VARCHAR(100),
    email           VARCHAR(255) NOT NULL UNIQUE,
    phone           VARCHAR(30)
);

-- Administrative staff
CREATE TABLE AdminStaff (
    admin_id        SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    title           VARCHAR(100),
    email           VARCHAR(255) NOT NULL UNIQUE,
    phone           VARCHAR(30)
);

-- Types of fitness classes (Yoga, HIIT, etc.)
CREATE TABLE Class (
    class_id        SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    description     TEXT,
    difficulty      VARCHAR(20),
    category        VARCHAR(50),
    duration_minutes INT,
    admin_id        INT REFERENCES AdminStaff(admin_id),
    assigned_since  DATE
);

-- Physical rooms in the gym
CREATE TABLE Room (
    room_id         SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    location        VARCHAR(100)
);

-- Concrete scheduled sessions of a class
CREATE TABLE ClassSession (
    session_id      SERIAL PRIMARY KEY,
    class_id        INT NOT NULL REFERENCES Class(class_id) ON DELETE CASCADE,
    room_id         INT REFERENCES Room(room_id),
    trainer_id      INT REFERENCES Trainer(trainer_id),
    session_date    DATE NOT NULL,
    start_time      TIME NOT NULL,
    end_time        TIME NOT NULL,
    capacity        INT NOT NULL
);

-- which member registered to which class session
CREATE TABLE MemberClassRegistration (
    registration_id SERIAL PRIMARY KEY,
    member_id       INT NOT NULL REFERENCES Member(member_id) ON DELETE CASCADE,
    session_id      INT NOT NULL REFERENCES ClassSession(session_id) ON DELETE CASCADE,
    UNIQUE (member_id, session_id)
);

-- Logged health metrics for members (weight, heart rate, etc.)
CREATE TABLE HealthMetric (
    metric_id       SERIAL PRIMARY KEY,
    member_id       INT NOT NULL REFERENCES Member(member_id) ON DELETE CASCADE,
    metric_type     VARCHAR(50) NOT NULL,
    value           NUMERIC(10,2) NOT NULL,
    recorded_at     TIMESTAMP DEFAULT NOW()
);

-- Trainer weekly availability 
CREATE TABLE TrainerAvailability (
    availability_id SERIAL PRIMARY KEY,
    trainer_id      INT NOT NULL REFERENCES Trainer(trainer_id) ON DELETE CASCADE,
    day_of_week     VARCHAR(10) NOT NULL,   
    start_time      TIME NOT NULL,
    end_time        TIME NOT NULL
);

-- =========
--  INDEX: Speed up searching members by email
-- =========

CREATE INDEX idx_member_email ON Member(email);

-- =========
--  VIEW for member metrics
-- =========

CREATE VIEW MemberDashboardSimple AS
SELECT
    m.member_id,
    m.first_name,
    m.last_name,
    m.goal_description,
    m.goal_target,
   
    (
        SELECT hm.value
        FROM HealthMetric hm
        WHERE hm.member_id = m.member_id
        ORDER BY hm.recorded_at DESC
        LIMIT 1
    ) AS last_metric_value,
    (
        SELECT hm.metric_type
        FROM HealthMetric hm
        WHERE hm.member_id = m.member_id
        ORDER BY hm.recorded_at DESC
        LIMIT 1
    ) AS last_metric_type,
    (
        SELECT COUNT(*)
        FROM MemberClassRegistration r
        WHERE r.member_id = m.member_id
    ) AS total_classes_registered
FROM Member m;

-- =========
--  TRIGGER: availability end_time must be after start_time
-- =========

CREATE OR REPLACE FUNCTION check_trainer_availability_time()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.end_time <= NEW.start_time THEN
        RAISE EXCEPTION 'end_time must be after start_time';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_trainer_availability_time
BEFORE INSERT OR UPDATE ON TrainerAvailability
FOR EACH ROW
EXECUTE FUNCTION check_trainer_availability_time();
