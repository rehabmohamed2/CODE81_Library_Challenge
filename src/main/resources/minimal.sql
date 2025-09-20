-- Minimal data for Library Management System Authentication

-- Insert Roles with explicit IDs
INSERT INTO roles (id, name) VALUES (1, 'ADMINISTRATOR');
INSERT INTO roles (id, name) VALUES (2, 'LIBRARIAN');
INSERT INTO roles (id, name) VALUES (3, 'STAFF');

-- Insert Users with explicit IDs (passwords are BCrypt encoded for 'password123')
INSERT INTO users (id, username, password) VALUES (1, 'admin', '$2a$10$EIXw8F8qCPOJ/N5YPH3Hre5rRwPUwEJQqaFKXfEJ5lQ2cOqwFTQZK');
INSERT INTO users (id, username, password) VALUES (2, 'librarian1', '$2a$10$EIXw8F8qCPOJ/N5YPH3Hre5rRwPUwEJQqaFKXfEJ5lQ2cOqwFTQZK');
INSERT INTO users (id, username, password) VALUES (3, 'staff1', '$2a$10$EIXw8F8qCPOJ/N5YPH3Hre5rRwPUwEJQqaFKXfEJ5lQ2cOqwFTQZK');

-- Assign Roles to Users
INSERT INTO user_roles (user_id, role_id) VALUES (1, 1); -- admin -> ADMINISTRATOR
INSERT INTO user_roles (user_id, role_id) VALUES (2, 2); -- librarian1 -> LIBRARIAN
INSERT INTO user_roles (user_id, role_id) VALUES (3, 3); -- staff1 -> STAFF

-- Insert Categories
INSERT INTO categories (name, description) VALUES ('Fiction', 'Literary works of imagination');
INSERT INTO categories (name, description) VALUES ('Science Fiction', 'Speculative fiction with futuristic concepts');
INSERT INTO categories (name, description) VALUES ('Mystery', 'Crime, detective and mystery novels');
INSERT INTO categories (name, description) VALUES ('Romance', 'Love stories and romantic fiction');
INSERT INTO categories (name, description) VALUES ('Non-Fiction', 'Factual and informational books');
INSERT INTO categories (name, description) VALUES ('Biography', 'Life stories of real people');
INSERT INTO categories (name, description) VALUES ('History', 'Historical events and periods');
INSERT INTO categories (name, description) VALUES ('Science', 'Scientific knowledge and research');
INSERT INTO categories (name, description) VALUES ('Technology', 'Computing and technology books');
INSERT INTO categories (name, description) VALUES ('Self-Help', 'Personal development and improvement');

-- Insert Publishers
INSERT INTO publishers (name, address, website, contact_email, established_year) VALUES ('Penguin Random House', '1745 Broadway, New York, NY 10019', 'www.penguinrandomhouse.com', 'contact@penguinrandomhouse.com', 1927);
INSERT INTO publishers (name, address, website, contact_email, established_year) VALUES ('HarperCollins', '195 Broadway, New York, NY 10007', 'www.harpercollins.com', 'info@harpercollins.com', 1989);
INSERT INTO publishers (name, address, website, contact_email, established_year) VALUES ('Simon & Schuster', '1230 Avenue of the Americas, New York, NY 10020', 'www.simonandschuster.com', 'contact@simonandschuster.com', 1924);
INSERT INTO publishers (name, address, website, contact_email, established_year) VALUES ('Macmillan Publishers', '120 Broadway, New York, NY 10271', 'www.macmillan.com', 'info@macmillan.com', 1843);
INSERT INTO publishers (name, address, website, contact_email, established_year) VALUES ('Hachette Book Group', '1290 Avenue of the Americas, New York, NY 10104', 'www.hachettebookgroup.com', 'contact@hachette.com', 2006);