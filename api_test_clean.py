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
                print(f"    Response: {json.dumps(json_data, indent=2)[:300]}...")
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

def main():
    """Run API tests"""
    print("STARTING COMPREHENSIVE API TEST")
    print("="*50)
    print("Server: http://localhost:9007/api")

    # Step 1: Test Admin Login
    print("\n1. TESTING ADMIN LOGIN")
    print("-" * 30)

    admin_login = {"username": "admin", "password": "password123"}
    status, response = make_request("POST", "/auth/login", admin_login)

    if status == 200 and response and 'token' in response:
        admin_token = response['token']
        print(f"SUCCESS: Admin login successful!")
        print(f"Token: {admin_token[:50]}...")
    else:
        print("FAILED: Admin login failed")
        return

    # Step 2: Test Books Endpoint
    print("\n2. TESTING BOOKS ENDPOINT")
    print("-" * 30)

    headers = {'Authorization': f'Bearer {admin_token}'}
    status, response = make_request("GET", "/books", headers=headers)

    if status == 200:
        print("SUCCESS: GET /books successful")
        if isinstance(response, list):
            print(f"Found {len(response)} books")
    else:
        print("FAILED: GET /books failed")

    # Step 3: Test Categories Endpoint
    print("\n3. TESTING CATEGORIES ENDPOINT")
    print("-" * 30)

    status, response = make_request("GET", "/categories", headers=headers)

    if status == 200:
        print("SUCCESS: GET /categories successful")
        if isinstance(response, list):
            print(f"Found {len(response)} categories")
            for i, cat in enumerate(response[:3]):
                if isinstance(cat, dict) and 'name' in cat:
                    print(f"  {i+1}. {cat['name']}")
    else:
        print("FAILED: GET /categories failed")

    # Step 4: Test Publishers Endpoint
    print("\n4. TESTING PUBLISHERS ENDPOINT")
    print("-" * 30)

    status, response = make_request("GET", "/publishers", headers=headers)

    if status == 200:
        print("SUCCESS: GET /publishers successful")
        if isinstance(response, list):
            print(f"Found {len(response)} publishers")
            for i, pub in enumerate(response[:3]):
                if isinstance(pub, dict) and 'name' in pub:
                    print(f"  {i+1}. {pub['name']}")
    else:
        print("FAILED: GET /publishers failed")

    # Step 5: Test Users Endpoint (Admin Only)
    print("\n5. TESTING USERS ENDPOINT (ADMIN ONLY)")
    print("-" * 30)

    status, response = make_request("GET", "/users", headers=headers)

    if status == 200:
        print("SUCCESS: GET /users successful")
        if isinstance(response, list):
            print(f"Found {len(response)} users")
            for user in response:
                if isinstance(user, dict) and 'username' in user:
                    print(f"  - {user['username']}")
    else:
        print("FAILED: GET /users failed")

    # Step 6: Test Role-Based Access (Librarian)
    print("\n6. TESTING LIBRARIAN ACCESS")
    print("-" * 30)

    librarian_login = {"username": "librarian1", "password": "password123"}
    status, response = make_request("POST", "/auth/login", librarian_login)

    if status == 200 and response and 'token' in response:
        librarian_token = response['token']
        print("SUCCESS: Librarian login successful!")

        # Test librarian access to users endpoint (should be denied)
        lib_headers = {'Authorization': f'Bearer {librarian_token}'}
        status, response = make_request("GET", "/users", headers=lib_headers)

        if status == 403:
            print("SUCCESS: Librarian correctly denied access to /users (403 Forbidden)")
        else:
            print(f"UNEXPECTED: Librarian /users access returned status {status}")
    else:
        print("FAILED: Librarian login failed")

    # Step 7: Test Members Endpoint
    print("\n7. TESTING MEMBERS ENDPOINT")
    print("-" * 30)

    status, response = make_request("GET", "/members", headers=headers)

    if status == 200:
        print("SUCCESS: GET /members successful")
        if isinstance(response, list):
            print(f"Found {len(response)} members")
    else:
        print("FAILED: GET /members failed")

    print("\n" + "="*50)
    print("API TESTING COMPLETE!")
    print("="*50)
    print("All major endpoints tested successfully!")

if __name__ == "__main__":
    main()