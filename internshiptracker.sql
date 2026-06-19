CREATE DATABASE InternshipTrackerProject;
GO

USE InternshipTrackerProject;
GO



CREATE TABLE Student(
    StudentID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Company(
    CompanyID INT PRIMARY KEY IDENTITY(1,1),
    CompanyName VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

CREATE TABLE Application(
    ApplicationID INT PRIMARY KEY IDENTITY(1,1),

    StudentID INT NOT NULL,
    CompanyID INT NOT NULL,

    Position VARCHAR(100) NOT NULL,

    ApplyDate DATE NOT NULL,
    Deadline DATE NOT NULL,

    Status VARCHAR(50) NOT NULL,

    FOREIGN KEY(StudentID)
        REFERENCES Students(StudentID),

    FOREIGN KEY(CompanyID)
        REFERENCES Companies(CompanyID)
);

CREATE TABLE Interview(
    InterviewID INT PRIMARY KEY IDENTITY(1,1),

    ApplicationID INT NOT NULL,

    InterviewDate DATE NOT NULL,

    Result VARCHAR(50) NOT NULL,

    FOREIGN KEY(ApplicationID)
        REFERENCES Applications(ApplicationID)
);

-- STUDENTS

INSERT INTO Student(Name, Email)
VALUES
('Tanvir Hasan', 'tanvir@gmail.com'),
('Rahim Ahmed', 'rahim@gmail.com'),
('Karim Islam', 'karim@gmail.com'),
('Nusrat Jahan', 'nusrat@gmail.com'),
('Sakib Hossain', 'sakib@gmail.com');


-- COMPANIES

INSERT INTO Company(CompanyName, Location)
VALUES
('Google', 'USA'),
('Microsoft', 'USA'),
('Amazon', 'USA'),
('Meta', 'USA'),
('Netflix', 'USA');


-- APPLICATIONS

INSERT INTO Application
(
    StudentID,
    CompanyID,
    Position,
    ApplyDate,
    Deadline,
    Status
)
VALUES
(1,1,'Data Analyst Intern','2026-06-01','2026-06-30','Applied'),

(2,2,'Business Analyst Intern','2026-06-05','2026-07-10','Under Review'),

(3,3,'Data Science Intern','2026-06-08','2026-07-15','Interview'),

(4,4,'Software Engineer Intern','2026-06-10','2026-07-20','Accepted'),

(5,5,'Machine Learning Intern','2026-06-12','2026-07-25','Rejected');


-- INTERVIEWS

INSERT INTO Interview
(
    ApplicationID,
    InterviewDate,
    Result
)
VALUES
(1,'2026-06-20','Pending'),

(2,'2026-06-25','Passed'),

(3,'2026-06-28','Pending'),

(4,'2026-06-30','Passed'),

(5,'2026-07-01','Failed');

SELECT * FROM Student;

SELECT * FROM Company;

SELECT * FROM Application;

SELECT * FROM Interview;