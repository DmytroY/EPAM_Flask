INSERT INTO doctors(first_name, last_name, grade, specialization, email)
    VALUES('John', 'Watson', 'BM', 'Combat medic', 'jh_watson@micropeutist.com');

INSERT INTO patients(first_name, last_name, gender, birthday, health_state, email, doctor_id)
    VALUES('Andy', 'Bay', 'Male', '1956.05.05', 'Gunshot wound', 'jh_watson@micropeutist.com', 1);
