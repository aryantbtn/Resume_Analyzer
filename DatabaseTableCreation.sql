CREATE DATABASE resumeDB;
show databases;
use resumedb;

DROP TABLE parsed_resumes;
delete from parsed_resumes where id=2;

DESCRIBE users;
describe resumes;

SELECT * FROM users;
SELECT * FROM resumes;
SELECT * FROM parsed_resumes;

ALTER TABLE parsed_resumes
ADD COLUMN version INT DEFAULT 1;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE parsed_resumes
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    resume_id INT NOT NULL,

    full_text LONGTEXT,

    parsed_json JSON NOT NULL,

    parsed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (resume_id)
    REFERENCES resumes(id)
    ON DELETE CASCADE
);

CREATE TABLE job_descriptions
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    title VARCHAR(255),

    full_text LONGTEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);

CREATE TABLE parsed_job_descriptions
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    jd_id INT NOT NULL,

    parsed_json JSON NOT NULL,

    parsed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (jd_id)
    REFERENCES job_descriptions(id)
    ON DELETE CASCADE
);