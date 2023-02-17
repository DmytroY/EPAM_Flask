CREATE TABLE IF NOT EXISTS doctors(
    doctor_id       INT(5)      NOT NULL AUTO_INCREMENT,
    first_name      VARCHAR(30) NOT NULL,
    last_name       VARCHAR(30) NOT NULL,
    grade           VARCHAR(5)  NOT NULL,
    specialization  VARCHAR(30) NOT NULL,
    email           VARCHAR(50) NOT NULL,
	PRIMARY KEY (doctor_id)
);

CREATE TABLE IF NOT EXISTS patients(
    patient_id      INT(6)     NOT NULL AUTO_INCREMENT,
    first_name      VARCHAR(30) NOT NULL,
    last_name       VARCHAR(30) NOT NULL,
    gender          VARCHAR(5)  NOT NULL,
                    CONSTRAINT gender_variants
                    CHECK(gender='Male' OR gender='Female'),
    birthday        DATE        NOT NULL,
    health_state    VARCHAR(255),
    email           VARCHAR(50) NOT NULL,
    doctor_id       INT(5)      NOT NULL,
    PRIMARY KEY (patient_id),    
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);