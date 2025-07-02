-- Step 1: Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS plotera_db;

-- Step 2: Use the created database
USE plotera_db;

DROP TABLE IF EXISTS leads;
DROP TABLE IF EXISTS salespersons;
DROP TABLE IF EXISTS users;

-- Step 3: Create salespersons table
CREATE TABLE IF NOT EXISTS salespersons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL
);

-- Step 4: Create leads table
CREATE TABLE IF NOT EXISTS leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    interest VARCHAR(100),
    visit_date DATE,
    status VARCHAR(50) DEFAULT 'pending',
    assigned_to INT,
    FOREIGN KEY (assigned_to) REFERENCES salespersons(id)
);

-- Step 5: Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'admin'
);


-- Insert into salespersons
INSERT INTO salespersons (name, phone) VALUES
('Amit Sharma', '9876543210'),
('Priya Mehra', '9811122233');

-- Insert into leads
INSERT INTO leads (name, phone, interest, visit_date, status, assigned_to) VALUES
('Ravi Kumar', '9988776655', 'Plot', '2025-06-21', 'pending', 1),
('Neha Singh', '9877890123', 'Flat', '2025-06-22', 'visited', 2);

-- Insert into users
INSERT INTO users (username, password_hash, role) VALUES
('admin', 'hashed_dummy_password', 'admin');

-- Note: Replace 'hashed_dummy_password' with an actual hashed password for security.
