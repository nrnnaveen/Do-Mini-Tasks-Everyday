--CREATING PERSON TABLE

CREATE TABLE person (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  country VARCHAR(20)
  );

-- INSERT 5 Rows Of DATA'S INTO PERSON TABLE 
  
INSERT INTO person (name, email, country) VALUES 
('Naveen', 'naveen@gmail.com', 'india'),
('Nithish', 'nithish@gmail.com', 'india'),
('Siva', 'siva@gmail.com', 'india'),
('Kumar', 'kumar@gmail.com', 'india'),
('Vijay', 'vijay@gmail.com', 'india'),
('Akil','akil@gmail.com','india');


