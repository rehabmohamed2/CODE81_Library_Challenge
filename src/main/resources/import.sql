-- Sample Data for Library Management System

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

-- Insert Authors
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('J.K. Rowling', 'British author best known for the Harry Potter series', 'British', 1965);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Stephen King', 'American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels', 'American', 1947);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Agatha Christie', 'English writer known for her detective novels featuring Hercule Poirot and Miss Marple', 'British', 1890);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('George Orwell', 'English novelist and essayist, journalist and critic', 'British', 1903);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Jane Austen', 'English novelist known primarily for her six major novels', 'British', 1775);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Isaac Asimov', 'American writer and professor of biochemistry, known for science fiction works', 'American', 1920);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Margaret Atwood', 'Canadian poet, novelist, literary critic, essayist, teacher, environmental activist, and inventor', 'Canadian', 1939);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Ernest Hemingway', 'American novelist, short-story writer, and journalist', 'American', 1899);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Toni Morrison', 'American novelist, essayist, book editor, and college professor', 'American', 1931);
INSERT INTO authors (name, biography, nationality, birth_year) VALUES ('Paulo Coelho', 'Brazilian lyricist and novelist, best known for The Alchemist', 'Brazilian', 1947);

-- Insert Books
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('Harry Potter and the Philosopher''s Stone', '978-0747532699', 1997, '1st Edition', 'English', 'A young wizard discovers his magical heritage on his 11th birthday', 'https://example.com/covers/hp1.jpg', 1, 1);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('The Shining', '978-0307743657', 1977, 'Reprint Edition', 'English', 'A family heads to an isolated hotel where the father slowly goes insane', 'https://example.com/covers/shining.jpg', 3, 1);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('Murder on the Orient Express', '978-0062693662', 1934, 'Reissue Edition', 'English', 'Detective Hercule Poirot investigates a murder aboard the famous European train', 'https://example.com/covers/orient.jpg', 3, 2);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('1984', '978-0452284234', 1949, 'Reprint Edition', 'English', 'A dystopian social science fiction novel about totalitarian control', 'https://example.com/covers/1984.jpg', 2, 3);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('Pride and Prejudice', '978-0141439518', 1813, 'Penguin Classics', 'English', 'A romantic novel about manners, upbringing, morality, education, and marriage', 'https://example.com/covers/pride.jpg', 4, 1);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('Foundation', '978-0553293357', 1951, 'Reprint Edition', 'English', 'First novel in Isaac Asimov''s Foundation series about the fall and rise of galactic empire', 'https://example.com/covers/foundation.jpg', 2, 4);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('The Handmaid''s Tale', '978-0385490818', 1985, 'Reprint Edition', 'English', 'A dystopian novel about a totalitarian society where women are subjugated', 'https://example.com/covers/handmaid.jpg', 2, 5);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('The Old Man and the Sea', '978-0684801223', 1952, 'Reprint Edition', 'English', 'The story of an aging Cuban fisherman''s struggle with a giant marlin', 'https://example.com/covers/oldman.jpg', 1, 3);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('Beloved', '978-1400033416', 1987, 'Vintage Edition', 'English', 'A story about the legacy of slavery in post-Civil War Ohio', 'https://example.com/covers/beloved.jpg', 1, 1);
INSERT INTO books (title, isbn, publication_year, edition, language, summary, cover_image_url, category_id, publisher_id) VALUES ('The Alchemist', '978-0062315007', 1988, 'Anniversary Edition', 'English', 'A philosophical book about following your dreams and personal legend', 'https://example.com/covers/alchemist.jpg', 10, 2);

-- Link Books to Authors (Many-to-Many relationship)
INSERT INTO book_authors (book_id, author_id) VALUES (1, 1); -- Harry Potter -> J.K. Rowling
INSERT INTO book_authors (book_id, author_id) VALUES (2, 2); -- The Shining -> Stephen King
INSERT INTO book_authors (book_id, author_id) VALUES (3, 3); -- Orient Express -> Agatha Christie
INSERT INTO book_authors (book_id, author_id) VALUES (4, 4); -- 1984 -> George Orwell
INSERT INTO book_authors (book_id, author_id) VALUES (5, 5); -- Pride and Prejudice -> Jane Austen
INSERT INTO book_authors (book_id, author_id) VALUES (6, 6); -- Foundation -> Isaac Asimov
INSERT INTO book_authors (book_id, author_id) VALUES (7, 7); -- Handmaid's Tale -> Margaret Atwood
INSERT INTO book_authors (book_id, author_id) VALUES (8, 8); -- Old Man and the Sea -> Ernest Hemingway
INSERT INTO book_authors (book_id, author_id) VALUES (9, 9); -- Beloved -> Toni Morrison
INSERT INTO book_authors (book_id, author_id) VALUES (10, 10); -- The Alchemist -> Paulo Coelho

-- Insert Members
INSERT INTO members (name, email, phone, address, membership_number, membership_start_date, membership_expiry_date, is_active) VALUES ('John Smith', 'john.smith@email.com', '555-0101', '123 Main St, New York, NY 10001', 'MEM001', '2024-01-15', '2025-01-15', true);
INSERT INTO members (name, email, phone, address, membership_number, membership_start_date, membership_expiry_date, is_active) VALUES ('Emily Johnson', 'emily.johnson@email.com', '555-0102', '456 Oak Ave, Los Angeles, CA 90210', 'MEM002', '2024-02-20', '2025-02-20', true);
INSERT INTO members (name, email, phone, address, membership_number, membership_start_date, membership_expiry_date, is_active) VALUES ('Michael Brown', 'michael.brown@email.com', '555-0103', '789 Pine Rd, Chicago, IL 60601', 'MEM003', '2024-03-10', '2025-03-10', true);
INSERT INTO members (name, email, phone, address, membership_number, membership_start_date, membership_expiry_date, is_active) VALUES ('Sarah Davis', 'sarah.davis@email.com', '555-0104', '321 Elm St, Houston, TX 77001', 'MEM004', '2024-04-05', '2025-04-05', true);
INSERT INTO members (name, email, phone, address, membership_number, membership_start_date, membership_expiry_date, is_active) VALUES ('David Wilson', 'david.wilson@email.com', '555-0105', '654 Maple Dr, Phoenix, AZ 85001', 'MEM005', '2023-12-01', '2024-12-01', false);

-- Insert Borrow Transactions
INSERT INTO borrow_transactions (member_id, book_id, borrow_date, return_date) VALUES (1, 1, '2024-09-01', '2024-09-15'); -- John borrowed Harry Potter, returned
INSERT INTO borrow_transactions (member_id, book_id, borrow_date, return_date) VALUES (2, 3, '2024-09-10', NULL); -- Emily borrowed Orient Express, not returned yet
INSERT INTO borrow_transactions (member_id, book_id, borrow_date, return_date) VALUES (3, 5, '2024-09-05', '2024-09-18'); -- Michael borrowed Pride and Prejudice, returned
INSERT INTO borrow_transactions (member_id, book_id, borrow_date, return_date) VALUES (4, 7, '2024-09-12', NULL); -- Sarah borrowed Handmaid's Tale, not returned yet
INSERT INTO borrow_transactions (member_id, book_id, borrow_date, return_date) VALUES (1, 4, '2024-09-20', NULL); -- John borrowed 1984, not returned yet
INSERT INTO borrow_transactions (member_id, book_id, borrow_date, return_date) VALUES (2, 10, '2024-08-15', '2024-08-30'); -- Emily borrowed The Alchemist, returned

-- Insert User Activities (sample activity logs)
INSERT INTO user_activities (user_id, action, entity_type, entity_id, details, ip_address, timestamp) VALUES (1, 'CREATE', 'Book', 1, 'Created new book: Harry Potter', '192.168.1.100', '2024-09-01 10:30:00');
INSERT INTO user_activities (user_id, action, entity_type, entity_id, details, ip_address, timestamp) VALUES (2, 'CREATE', 'Member', 1, 'Registered new member: John Smith', '192.168.1.101', '2024-09-01 11:15:00');
INSERT INTO user_activities (user_id, action, entity_type, entity_id, details, ip_address, timestamp) VALUES (3, 'CREATE', 'BorrowTransaction', 1, 'Book borrowed by member', '192.168.1.102', '2024-09-01 14:20:00');
INSERT INTO user_activities (user_id, action, entity_type, entity_id, details, ip_address, timestamp) VALUES (2, 'UPDATE', 'BorrowTransaction', 1, 'Book returned by member', '192.168.1.101', '2024-09-15 09:45:00');
INSERT INTO user_activities (user_id, action, entity_type, entity_id, details, ip_address, timestamp) VALUES (1, 'CREATE', 'Author', 1, 'Added new author: J.K. Rowling', '192.168.1.100', '2024-09-01 10:00:00');