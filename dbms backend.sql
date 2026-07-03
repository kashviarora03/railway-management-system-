-- ============================================================
-- DROP & CREATE DATABASE
-- ============================================================
DROP DATABASE IF EXISTS railway_system;
CREATE DATABASE railway_system;
USE railway_system;

-- ============================================================
-- PASSENGER
-- ============================================================
CREATE TABLE PASSENGER (
    id            INT PRIMARY KEY AUTO_INCREMENT,
    fname         VARCHAR(50)  NOT NULL,
    mname         VARCHAR(50),
    lname         VARCHAR(50)  NOT NULL,
    phone_number  VARCHAR(15)  NOT NULL,
    gender        VARCHAR(10),
    age           INT,
    address       VARCHAR(255)
);

-- ============================================================
-- TRAIN_DETAILS
-- ============================================================
CREATE TABLE TRAIN_DETAILS (
    train_number      INT PRIMARY KEY AUTO_INCREMENT,
    train_name        VARCHAR(100) NOT NULL,
    reservation       VARCHAR(50),        -- e.g. AC, Sleeper etc.
    compartment_chart VARCHAR(255),       -- coach / seat layout inf

    station           VARCHAR(100)        -- starting / main station
);

-- ============================================================
-- TECHNICAL_SUPERVISOR
-- ============================================================
CREATE TABLE TECHNICAL_SUPERVISOR (
    supervisor_id INT PRIMARY KEY AUTO_INCREMENT,
    fname         VARCHAR(50)  NOT NULL,
    mname         VARCHAR(50),
    lname         VARCHAR(50)  NOT NULL,
    phone_number  VARCHAR(15)  NOT NULL,
    email         VARCHAR(100)
);

-- ============================================================
-- TICKET  (PASSENGER issues TICKET, linked to TRAIN_DETAILS)
-- ============================================================
CREATE TABLE TICKET (
    ticket_id        INT PRIMARY KEY AUTO_INCREMENT,
    passenger_id     INT          NOT NULL,
    destination      VARCHAR(100) NOT NULL,
    date_of_journey  DATE         NOT NULL,
    time_of_journey  TIME,
    reservation      VARCHAR(50),          -- class / type of reservation
    train_number     INT,                  -- FK -> TRAIN_DETAILS
    train_details    VARCHAR(255),         -- extra description if needed

    CONSTRAINT fk_ticket_passenger
        FOREIGN KEY (passenger_id) REFERENCES PASSENGER(id),

    CONSTRAINT fk_ticket_train
        FOREIGN KEY (train_number) REFERENCES TRAIN_DETAILS(train_number)
);

-- ============================================================
-- PAYMENT  (PASSENGER makes PAYMENT for TICKET)
-- ============================================================
CREATE TABLE PAYMENT (
    payment_id     INT PRIMARY KEY AUTO_INCREMENT,
    passenger_id   INT          NOT NULL,
    ticket_id      INT          NOT NULL,
    total_payment  DECIMAL(10,2) NOT NULL,
    payment_date   DATE,
    payment_mode   VARCHAR(20),           -- UPI / Card / Cash etc.

    CONSTRAINT fk_payment_passenger
        FOREIGN KEY (passenger_id) REFERENCES PASSENGER(id),

    CONSTRAINT fk_payment_ticket
        FOREIGN KEY (ticket_id) REFERENCES TICKET(ticket_id)
);

-- ============================================================
-- CHECKS  (PASSENGER checks TRAIN_DETAILS)
-- associative entity: PASSENGER ↔ TRAIN_DETAILS
-- ============================================================
CREATE TABLE CHECKS (
    passenger_id  INT NOT NULL,
    train_number  INT NOT NULL,
    check_date    DATE,

    PRIMARY KEY (passenger_id, train_number),

    CONSTRAINT fk_checks_passenger
        FOREIGN KEY (passenger_id) REFERENCES PASSENGER(id),

    CONSTRAINT fk_checks_train
        FOREIGN KEY (train_number) REFERENCES TRAIN_DETAILS(train_number)
);

-- ============================================================
-- MANAGE  (TRAIN_DETAILS managed_by TECHNICAL_SUPERVISOR)
-- associative entity: TRAIN_DETAILS ↔ TECHNICAL_SUPERVISOR
-- ============================================================
CREATE TABLE MANAGE (
    supervisor_id INT NOT NULL,
    train_number  INT NOT NULL,

    PRIMARY KEY (supervisor_id, train_number),

    CONSTRAINT fk_manage_supervisor
        FOREIGN KEY (supervisor_id) REFERENCES TECHNICAL_SUPERVISOR(supervisor_id),

    CONSTRAINT fk_manage_train
        FOREIGN KEY (train_number) REFERENCES TRAIN_DETAILS(train_number)
);



