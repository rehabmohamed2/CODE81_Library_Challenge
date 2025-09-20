# Library Management System

A comprehensive Spring Boot REST API for managing library operations with role-based access control, complete CRUD operations, and advanced book metadata management.

## 🚀 Features

### Core Functionality
- **Complete Book Management** with extended metadata (authors, publishers, categories, ISBN, edition, summary, cover images)
- **Member Management** with membership tracking and borrowing history
- **User Management** with role-based access control (Administrator, Librarian, Staff)
- **Borrowing and Return System** with transaction tracking
- **User Activity Logging** for audit trails

### Technical Features
- **JWT Authentication** with secure token-based access
- **Role-Based Authorization** with endpoint-level security
- **RESTful API Design** following best practices
- **Comprehensive Database Schema** with proper relationships
- **Sample Data** for testing and demonstration

## 🧪 API Testing

Ready to test the API? Import our comprehensive Postman collection to get started immediately:

**[📥 Download Postman Collection](https://github.com/rehabmohamed2/CODE81_Library_Challenge/blob/main/Library_Management_API.postman_collection.json)**

The collection includes:
- Pre-configured requests for all endpoints
- Authentication examples
- Sample request bodies
- Environment variables setup

## Entity Relationship Diagram
Our library management system uses a well-structured relational database design:
**[📊 View Interactive ERD](https://github.com/rehabmohamed2/CODE81_Library_Challenge/blob/main/ERD_diagram.drawio.xml)** *(Open with Draw.io)*
  
## 🏗️ Architecture & Design Choices

### Technology Stack
- **Spring Boot 3.1.6** - Modern Java framework for rapid development
- **Spring Security** - Comprehensive security framework
- **Spring Data JPA** - Database abstraction layer
- **H2 Database** - In-memory database for development/testing
- **JWT (JSON Web Tokens)** - Stateless authentication
- **BCrypt** - Secure password hashing
- **Maven** - Dependency management and build tool

### Database Design

#### Entity Relationship Design
```
Users ←→ Roles (Many-to-Many)
Books ←→ Authors (Many-to-Many)
Books ←→ Categories (Many-to-One)
Books ←→ Publishers (Many-to-One)
Members ←→ BorrowTransactions ←→ Books
Users ←→ UserActivities (One-to-Many)
```

#### Key Design Decisions

**1. Many-to-Many Book-Author Relationship**
- **Choice**: Used `@ManyToMany` with junction table `book_authors`
- **Rationale**: Books can have multiple authors, authors can write multiple books
- **Implementation**: Bidirectional relationship with proper JSON handling

**2. Separate Entities for Authors, Publishers, Categories**
- **Choice**: Normalized design with separate tables
- **Rationale**: Allows for rich metadata, prevents data duplication, enables future features
- **Benefits**: Can track publisher history, author bibliographies, category hierarchies

**3. Role-Based Security Model**
- **Choice**: Three distinct roles with hierarchical permissions
- **Rationale**: Reflects real library organizational structure
- **Implementation**:
  - **ADMINISTRATOR**: Full system access
  - **LIBRARIAN**: Book and member management
  - **STAFF**: Basic book operations only

**4. JWT Token Authentication**
- **Choice**: Stateless JWT tokens over session-based auth
- **Rationale**: Better for REST APIs, scalable, enables microservices
- **Security**: 24-hour expiration, BCrypt password hashing

### API Design Philosophy

#### RESTful Principles
- **Resource-based URLs**: `/books`, `/members`, `/users`
- **HTTP Methods**: GET (read), POST (create), PUT (update), DELETE (remove)
- **Status Codes**: 200 (OK), 201 (Created), 404 (Not Found), 401 (Unauthorized)
- **JSON Communication**: Request/response bodies in JSON format

#### Security-First Approach
- **Authentication Required**: All endpoints except `/auth/**` require valid JWT
- **Role-Based Access**: Different permission levels per endpoint
- **Input Validation**: Proper request body validation
- **Error Handling**: Graceful error responses

## 📊 Database Schema

### Core Tables

#### Books Table
```sql
CREATE TABLE books (
    id BIGINT PRIMARY KEY,
    title VARCHAR(255),
    isbn VARCHAR(255),
    publication_year INTEGER,
    edition VARCHAR(255),
    language VARCHAR(255),
    summary VARCHAR(255),
    cover_image_url VARCHAR(255),
    category_id BIGINT,
    publisher_id BIGINT
);
```

#### Junction Tables
- `book_authors` - Links books to multiple authors
- `user_roles` - Links users to multiple roles

#### Relationship Tables
- `borrow_transactions` - Tracks book borrowing history
- `user_activities` - Audit log for user actions

## 🔐 Security Implementation

### Authentication Flow
1. **Login**: POST `/auth/login` with username/password
2. **Token Generation**: Server returns JWT token
3. **API Access**: Include `Authorization: Bearer <token>` header
4. **Token Validation**: Server validates token on each request

### Authorization Matrix
| Endpoint | ADMINISTRATOR | LIBRARIAN | STAFF |
|----------|---------------|-----------|-------|
| `/users/**` | ✅ | ❌ | ❌ |
| `/books/**` | ✅ | ✅ | ✅ |
| `/members/**` | ✅ | ✅ | ❌ |
| `/authors/**` | ✅ | ✅ | ❌ |
| `/publishers/**` | ✅ | ✅ | ❌ |
| `/categories/**` | ✅ | ✅ | ❌ |
| `/borrow-transactions/**` | ✅ | ✅ | ✅ |

### Password Security
- **BCrypt Hashing**: All passwords encrypted with BCrypt
- **Salt Rounds**: Default BCrypt strength (10 rounds)
- **No Plain Text**: Passwords never stored in plain text

## 🛠️ Setup & Running

### Prerequisites
- Java 17 or higher
- Maven 3.6+

### Quick Start
```bash
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd library-management-system

# Run the application
mvn spring-boot:run
```

### Application Access
- **API Base URL**: `http://localhost:9002/api`
- **H2 Console**: `http://localhost:9002/api/h2-console`
- **Database URL**: `jdbc:h2:mem:librarydb`
- **Username**: `sa`
- **Password**: `password`

## 📝 API Documentation

### Authentication Endpoints
```bash
POST /api/auth/login
POST /api/auth/register
```

### Book Management
```bash
GET    /api/books           # Get all books
GET    /api/books/{id}      # Get book by ID
POST   /api/books           # Create new book
PUT    /api/books/{id}      # Update book
DELETE /api/books/{id}      # Delete book
```

### Member Management
```bash
GET    /api/members         # Get all members
GET    /api/members/{id}    # Get member by ID
POST   /api/members         # Create new member
PUT    /api/members/{id}    # Update member
DELETE /api/members/{id}    # Delete member
```

### User Management (Admin Only)
```bash
GET    /api/users           # Get all users
GET    /api/users/{id}      # Get user by ID
POST   /api/users           # Create new user
PUT    /api/users/{id}      # Update user
DELETE /api/users/{id}      # Delete user
```

### Borrowing System
```bash
GET    /api/borrow-transactions           # Get all transactions
POST   /api/borrow-transactions           # Create borrow transaction
PUT    /api/borrow-transactions/{id}      # Update transaction (return book)
GET    /api/borrow-transactions/member/{memberId}  # Get member's history
```

## 🧪 Sample Data

The application includes comprehensive sample data:
- **3 Users**: admin, librarian1, staff1 (password: `password123`)
- **3 Roles**: ADMINISTRATOR, LIBRARIAN, STAFF
- **10 Categories**: Fiction, Science Fiction, Mystery, etc.
- **5 Publishers**: Major publishing houses with full metadata
- **10 Authors**: Famous authors with biographies
- **10 Books**: Popular books with complete metadata
- **5 Members**: Sample library members
- **6 Borrow Transactions**: Mix of active and returned books
- **5 User Activities**: Sample audit log entries

## 🔍 Testing

### Sample Login Credentials
```json
{
  "username": "admin",
  "password": "password123"
}
```

### Sample API Calls
```bash
# Login to get token
curl -X POST http://localhost:9002/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}'

# Get all books (requires authentication)
curl -X GET http://localhost:9002/api/books \
  -H "Authorization: Bearer <your-jwt-token>"

# Create a new book (requires LIBRARIAN+ role)
curl -X POST http://localhost:9002/api/books \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"New Book","isbn":"123-456-789"}'
```

## 🚦 Configuration

### Application Properties
- **Port**: 9002
- **Context Path**: `/api`
- **Database**: H2 in-memory
- **JWT Secret**: Configurable in `application.yml`
- **Token Expiration**: 24 hours

### Environment Configuration
All configuration is in `src/main/resources/application.yml`:
- Database settings
- Security configuration
- Logging levels
- JWT settings

## 🎯 Future Enhancements

### Potential Improvements
1. **Email Notifications** - Overdue book reminders
2. **Book Reservations** - Queue system for popular books
3. **Fine Management** - Late return fee calculation
4. **Reporting Dashboard** - Analytics and statistics
5. **Book Recommendations** - Based on borrowing history
6. **API Documentation** - Swagger/OpenAPI integration
7. **Docker Support** - Containerization for deployment

### Scalability Considerations
- **Database Migration**: Easy switch from H2 to PostgreSQL/MySQL
- **Caching Layer**: Redis integration for performance
- **Microservices**: Modular design allows service separation
- **Load Balancing**: Stateless JWT enables horizontal scaling

## 👥 Contributing

### Code Style
- Follow Spring Boot best practices
- Use proper naming conventions
- Include proper error handling
- Write clear, concise code

### Security Guidelines
- Never commit secrets or passwords
- Always validate input data
- Follow principle of least privilege
- Log security-relevant events

## 📄 License

This project is developed as a coding challenge demonstration.

---

**Note**: This is a demonstration project with in-memory database. For production use, configure a persistent database and update security settings accordingly.
