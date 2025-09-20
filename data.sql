-- Insert sample roles
INSERT INTO role (name) VALUES ('ROLE_ADMIN');
INSERT INTO role (name) VALUES ('ROLE_USER');

-- Insert sample users
INSERT INTO users (username, password) VALUES ('admin', '{noop}admin123');
INSERT INTO users (username, password) VALUES ('john', '{noop}password');

-- Assign roles to users
INSERT INTO user_roles (user_id, role_id) VALUES (1, 1); -- admin -> ROLE_ADMIN
INSERT INTO user_roles (user_id, role_id) VALUES (2, 2); -- john -> ROLE_USER

-- Insert authors
INSERT INTO author (name) VALUES ('George Orwell');
INSERT INTO author (name) VALUES ('J.K. Rowling');

-- Insert publishers
INSERT INTO publisher (name) VALUES ('Penguin Books');
INSERT INTO publisher (name) VALUES ('Bloomsbury');

-- Insert categories
INSERT INTO category (name) VALUES ('Fiction');
INSERT INTO category (name) VALUES ('Fantasy');

-- Insert books
INSERT INTO book (title, isbn, publication_year, edition, language, summary, author_id, publisher_id, category_id)
VALUES ('1984', '9780451524935', 1949, '1st', 'English', 'Dystopian social science fiction novel.', 1, 1, 1);

INSERT INTO book (title, isbn, publication_year, edition, language, summary, author_id, publisher_id, category_id)
VALUES ('Harry Potter and the Philosopher''s Stone', '9780747532699', 1997, '1st', 'English', 'Fantasy novel about a young wizard.', 2, 2, 2);

-- Insert members
INSERT INTO member (name, email) VALUES ('Alice Smith', 'alice@example.com');
INSERT INTO member (name, email) VALUES ('Bob Johnson', 'bob@example.com');

-- Insert borrow transactions
INSERT INTO borrow_transaction (member_id, book_id, borrow_date, return_date)
VALUES (1, 1, '2025-09-01', '2025-09-15');

INSERT INTO borrow_transaction (member_id, book_id, borrow_date, return_date)
VALUES (2, 2, '2025-09-05', NULL);
