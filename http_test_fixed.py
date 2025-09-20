#!/usr/bin/env python3
import http.client
import json
import time

def test_login():
    """Test login endpoint using http.client"""
    try:
        conn = http.client.HTTPConnection('localhost', 9007, timeout=15)

        # Prepare login data
        login_data = json.dumps({
            "username": "admin",
            "password": "password123"
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Content-Length': str(len(login_data))
        }

        print("Testing POST /api/auth/login ...")
        print(f"Sending: {login_data}")

        conn.request("POST", "/api/auth/login", body=login_data, headers=headers)
        response = conn.getresponse()
        data = response.read()

        print(f"Status: {response.status} {response.reason}")
        print(f"Headers: {dict(response.getheaders())}")
        print(f"Response: {data.decode('utf-8')}")

        conn.close()

        if response.status == 200:
            return json.loads(data.decode('utf-8'))
        else:
            return None

    except Exception as e:
        print(f"Login error: {e}")
        return None

def test_books_endpoint(token=None):
    """Test books endpoint"""
    try:
        conn = http.client.HTTPConnection('localhost', 9007, timeout=15)

        headers = {'Accept': 'application/json'}
        if token:
            headers['Authorization'] = f'Bearer {token}'

        print("Testing GET /api/books ...")
        conn.request("GET", "/api/books", headers=headers)
        response = conn.getresponse()
        data = response.read()

        print(f"Status: {response.status} {response.reason}")
        print(f"Response: {data.decode('utf-8')[:500]}...")

        conn.close()
        return response.status == 200

    except Exception as e:
        print(f"Books endpoint error: {e}")
        return False

def test_categories_endpoint(token=None):
    """Test categories endpoint"""
    try:
        conn = http.client.HTTPConnection('localhost', 9007, timeout=15)

        headers = {'Accept': 'application/json'}
        if token:
            headers['Authorization'] = f'Bearer {token}'

        print("Testing GET /api/categories ...")
        conn.request("GET", "/api/categories", headers=headers)
        response = conn.getresponse()
        data = response.read()

        print(f"Status: {response.status} {response.reason}")
        print(f"Response: {data.decode('utf-8')[:500]}...")

        conn.close()
        return response.status == 200

    except Exception as e:
        print(f"Categories endpoint error: {e}")
        return False

if __name__ == "__main__":
    print("=== Library Management System API Test ===")

    # Test login
    print("\n1. Testing Authentication...")
    login_result = test_login()

    token = None
    if login_result and 'token' in login_result:
        token = login_result['token']
        print(f"SUCCESS: Login successful! Token received.")
        print(f"Token (first 50 chars): {token[:50]}...")
    else:
        print("FAILED: Login failed")

    # Test endpoints with authentication
    if token:
        print("\n2. Testing authenticated endpoints...")

        print("\n2a. Testing Books endpoint:")
        books_success = test_books_endpoint(token)
        if books_success:
            print("SUCCESS: Books endpoint accessible")
        else:
            print("FAILED: Books endpoint failed")

        print("\n2b. Testing Categories endpoint:")
        categories_success = test_categories_endpoint(token)
        if categories_success:
            print("SUCCESS: Categories endpoint accessible")
        else:
            print("FAILED: Categories endpoint failed")

    else:
        print("\nSkipping authenticated endpoint tests due to login failure")

    print("\n=== Test Complete ===")