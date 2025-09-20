#!/usr/bin/env python3
import http.client
import json
import time

BASE_URL = "localhost"
PORT = 9007
BASE_PATH = "/api"

def make_request(method, endpoint, data=None, headers=None, timeout=30):
    """Make HTTP request with proper error handling"""
    try:
        conn = http.client.HTTPConnection(BASE_URL, PORT, timeout=timeout)

        if headers is None:
            headers = {}

        if data and isinstance(data, dict):
            data = json.dumps(data)
            headers['Content-Type'] = 'application/json'
            headers['Content-Length'] = str(len(data))

        headers.setdefault('Accept', 'application/json')

        print(f"\n>>> {method} {BASE_PATH}{endpoint}")
        if data:
            print(f"    Data: {data}")

        conn.request(method, f"{BASE_PATH}{endpoint}", body=data, headers=headers)
        response = conn.getresponse()
        response_data = response.read().decode('utf-8')

        print(f"    Status: {response.status} {response.reason}")

        if response_data:
            try:
                json_data = json.loads(response_data)
                print(f"    Response: {json.dumps(json_data, indent=2)[:500]}...")
                conn.close()
                return response.status, json_data
            except json.JSONDecodeError:
                print(f"    Response: {response_data[:200]}...")
                conn.close()
                return response.status, response_data
        else:
            print("    Response: (empty)")
            conn.close()
            return response.status, None

    except Exception as e:
        print(f"    Error: {e}")
        return None, None

def test_authentication():
    """Test authentication endpoints"""
    print("\n" + "="*50)
    print("TESTING AUTHENTICATION")
    print("="*50)

    # Test admin login
    admin_login = {
        "username": "admin",
        "password": "password123"
    }

    status, response = make_request("POST", "/auth/login", admin_login)

    if status == 200 and response and 'token' in response:
        admin_token = response['token']
        print(f"✅ Admin login successful! Token: {admin_token[:50]}...")
        return admin_token
    else:
        print("❌ Admin login failed")
        return None

def test_books_endpoint(token):
    """Test books endpoint"""
    print("\n" + "="*50)
    print("TESTING BOOKS ENDPOINT")
    print("="*50)

    headers = {'Authorization': f'Bearer {token}'}

    # Get all books
    status, response = make_request("GET", "/books", headers=headers)

    if status == 200:
        print("✅ GET /books successful")
        if isinstance(response, list):
            print(f"   Found {len(response)} books")
        return True
    else:
        print("❌ GET /books failed")
        return False

def test_categories_endpoint(token):
    """Test categories endpoint"""
    print("\n" + "="*50)
    print("TESTING CATEGORIES ENDPOINT")
    print("="*50)

    headers = {'Authorization': f'Bearer {token}'}

    # Get all categories
    status, response = make_request("GET", "/categories", headers=headers)

    if status == 200:
        print("✅ GET /categories successful")
        if isinstance(response, list):
            print(f"   Found {len(response)} categories")
            for cat in response[:3]:  # Show first 3 categories
                if isinstance(cat, dict) and 'name' in cat:
                    print(f"   - {cat['name']}")
        return True
    else:
        print("❌ GET /categories failed")
        return False

def test_publishers_endpoint(token):
    """Test publishers endpoint"""
    print("\n" + "="*50)
    print("TESTING PUBLISHERS ENDPOINT")
    print("="*50)

    headers = {'Authorization': f'Bearer {token}'}

    # Get all publishers
    status, response = make_request("GET", "/publishers", headers=headers)

    if status == 200:
        print("✅ GET /publishers successful")
        if isinstance(response, list):
            print(f"   Found {len(response)} publishers")
            for pub in response[:3]:  # Show first 3 publishers
                if isinstance(pub, dict) and 'name' in pub:
                    print(f"   - {pub['name']}")
        return True
    else:
        print("❌ GET /publishers failed")
        return False

def test_members_endpoint(token):
    """Test members endpoint"""
    print("\n" + "="*50)
    print("TESTING MEMBERS ENDPOINT")
    print("="*50)

    headers = {'Authorization': f'Bearer {token}'}

    # Get all members
    status, response = make_request("GET", "/members", headers=headers)

    if status == 200:
        print("✅ GET /members successful")
        if isinstance(response, list):
            print(f"   Found {len(response)} members")
        return True
    else:
        print("❌ GET /members failed")
        return False

def test_users_endpoint(token):
    """Test users endpoint (admin only)"""
    print("\n" + "="*50)
    print("TESTING USERS ENDPOINT (ADMIN ONLY)")
    print("="*50)

    headers = {'Authorization': f'Bearer {token}'}

    # Get all users
    status, response = make_request("GET", "/users", headers=headers)

    if status == 200:
        print("✅ GET /users successful")
        if isinstance(response, list):
            print(f"   Found {len(response)} users")
            for user in response:
                if isinstance(user, dict) and 'username' in user:
                    print(f"   - {user['username']}")
        return True
    else:
        print("❌ GET /users failed")
        return False

def test_role_based_access():
    """Test different user roles"""
    print("\n" + "="*50)
    print("TESTING ROLE-BASED ACCESS")
    print("="*50)

    # Test librarian login
    librarian_login = {
        "username": "librarian1",
        "password": "password123"
    }

    status, response = make_request("POST", "/auth/login", librarian_login)

    if status == 200 and response and 'token' in response:
        librarian_token = response['token']
        print(f"✅ Librarian login successful!")

        # Test librarian access to users endpoint (should fail)
        headers = {'Authorization': f'Bearer {librarian_token}'}
        status, response = make_request("GET", "/users", headers=headers)

        if status == 403:
            print("✅ Librarian correctly denied access to /users (403 Forbidden)")
            return True
        else:
            print(f"❌ Unexpected response for librarian /users access: {status}")
            return False
    else:
        print("❌ Librarian login failed")
        return False

def test_create_operations(token):
    """Test CREATE operations"""
    print("\n" + "="*50)
    print("TESTING CREATE OPERATIONS")
    print("="*50)

    headers = {'Authorization': f'Bearer {token}'}

    # Try to create a new member
    new_member = {
        "name": "Test Member",
        "email": "test@example.com",
        "phone": "1234567890",
        "address": "123 Test Street",
        "membershipNumber": "MEM001",
        "membershipStartDate": "2024-01-01",
        "membershipExpiryDate": "2024-12-31",
        "isActive": True
    }

    status, response = make_request("POST", "/members", new_member, headers)

    if status in [200, 201]:
        print("✅ POST /members successful")
        return True
    else:
        print(f"❌ POST /members failed with status {status}")
        return False

def run_comprehensive_test():
    """Run all tests"""
    print("🚀 STARTING COMPREHENSIVE API TEST")
    print("Server: http://localhost:9007/api")

    # Test authentication
    token = test_authentication()
    if not token:
        print("\n❌ Cannot proceed without authentication token")
        return

    # Test all endpoints with authentication
    results = []
    results.append(test_books_endpoint(token))
    results.append(test_categories_endpoint(token))
    results.append(test_publishers_endpoint(token))
    results.append(test_members_endpoint(token))
    results.append(test_users_endpoint(token))
    results.append(test_role_based_access())
    results.append(test_create_operations(token))

    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)

    passed = sum(results)
    total = len(results)

    print(f"✅ Tests Passed: {passed}/{total}")
    print(f"❌ Tests Failed: {total - passed}/{total}")

    if passed == total:
        print("\n🎉 ALL TESTS PASSED! API is working correctly!")
    else:
        print(f"\n⚠️  Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    run_comprehensive_test()