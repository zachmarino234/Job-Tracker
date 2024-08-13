DROP DATABASE IF EXISTS TalentTrace;


CREATE DATABASE TalentTrace;
USE TalentTrace;


CREATE TABLE applicants (
   appID INT AUTO_INCREMENT PRIMARY KEY,
   fName VARCHAR(30) NOT NULL,
   lName VARCHAR(30) NOT NULL,
   email VARCHAR(50) UNIQUE NOT NULL,
   prospectPos VARCHAR(200)
);


CREATE TABLE industry (
   indID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(200) UNIQUE NOT NULL,
   size INT
);


CREATE TABLE company (
   companyID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(200) NOT NULL,
   numEmployees INT,
   foundingDate DATE,
   empBenefits VARCHAR(1000),
   value INT,
   indID INT NOT NULL,
   FOREIGN KEY (indID) REFERENCES industry(indID)
   ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE jobRecords (
   jobID INT AUTO_INCREMENT PRIMARY KEY,
   appID INT NOT NULL,
   indID INT NOT NULL,
   companyID INT NOT NULL,
   jobTitle VARCHAR(200) NOT NULL,
   salary INT,
   dateApplied DATETIME DEFAULT CURRENT_TIMESTAMP,
   description VARCHAR(2000),
   posLevel VARCHAR(200),
   jobType VARCHAR(50),
   jobAddress VARCHAR(200),
   jobCity VARCHAR(100),
   jobCountry VARCHAR(100),
   FOREIGN KEY (appID) REFERENCES applicants(appID)
   ON UPDATE CASCADE ON DELETE CASCADE,
   FOREIGN KEY (indID) REFERENCES industry(indID)
   ON UPDATE CASCADE ON DELETE CASCADE,
   FOREIGN KEY (companyID) REFERENCES company(companyID)
   ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE departments (
   deptID INT AUTO_INCREMENT PRIMARY KEY,
   companyID INT NOT NULL,
   deptName VARCHAR(100) NOT NULL,
   FOREIGN KEY (companyID) REFERENCES company(companyID)
   ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE recruiters (
   recruiterID INT AUTO_INCREMENT PRIMARY KEY,
   deptID INT NOT NULL,
   fName VARCHAR(30) NOT NULL,
   lName VARCHAR(30) NOT NULL,
   username VARCHAR(50) NOT NULL,
   email VARCHAR(50) NOT NULL,
   phone varchar(20) NOT NULL,
   FOREIGN KEY (deptID) REFERENCES departments(deptID)
   ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE interviewRecords (
   interviewID INT AUTO_INCREMENT PRIMARY KEY,
   jobID INT NOT NULL,
   appID INT NOT NULL,
   recruiterID INT NOT NULL,
   date DATE,
   FOREIGN KEY (jobID) REFERENCES jobRecords(jobID)
   ON UPDATE CASCADE ON DELETE CASCADE,
   FOREIGN KEY (appID) REFERENCES applicants(appID)
   ON UPDATE CASCADE ON DELETE CASCADE,
   FOREIGN KEY (recruiterID) REFERENCES recruiters(recruiterID)
   ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE applicantIntNotes (
   interviewID INT NOT NULL,
   appID INT NOT NULL,
   content TEXT,
   PRIMARY KEY(interviewID, appID),
   FOREIGN KEY (interviewID) REFERENCES interviewRecords(interviewID)
   ON UPDATE CASCADE ON DELETE RESTRICT,
   FOREIGN KEY (appID) REFERENCES applicants(appID)
   ON UPDATE CASCADE ON DELETE RESTRICT
);


CREATE TABLE recruiterIntNotes (
   interviewID INT NOT NULL,
   recruiterID INT NOT NULL,
   compensation_range decimal(10, 2),
   role varchar(50),
   popularSkill TEXT,
   popularCertificates TEXT,
   PRIMARY KEY(interviewID, recruiterID),
   FOREIGN KEY (interviewID) REFERENCES interviewRecords(interviewID)
   ON UPDATE CASCADE ON DELETE RESTRICT,
   FOREIGN KEY (recruiterID) REFERENCES recruiters(recruiterID)
   ON UPDATE CASCADE ON DELETE RESTRICT
);
