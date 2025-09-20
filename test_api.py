#!/usr/bin/env python3
import urllib.request
import urllib.error
import json
import sys

def test_login():
    """Test the login API endpoint"""
    try:
        # Prepare login data
        login_data = {
            "username": "admin",
            "password": "password123"
        }

        # Convert to JSON and encode
        data = json.dumps(login_data).encode('utf-8')

        # Create request
        req = urllib.request.Request(
            'http://localhost:9007/api/auth/login',
            data=data,
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            method='POST'
        )

        print("Testing login endpoint...")
        print(f"URL: http://localhost:9007/api/auth/login")
        print(f"Data: {login_data}")

        # Make request with timeout
        with urllib.request.urlopen(req, timeout=30) as response:
            response_data = response.read().decode('utf-8')
            print(f"Status: {response.status}")
            print(f"Response: {response_data}")
            return json.loads(response_data)

    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        error_response = e.read().decode('utf-8')
        print(f"Error response: {error_response}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def test_books_endpoint(token=None):
    """Test the books endpoint"""
    try:
        headers = {'Accept': 'application/json'}
        if token:
            headers['Authorization'] = f'Bearer {token}'

        req = urllib.request.Request(
            'http://localhost:9007/api/books',
            headers=headers,
            method='GET'
        )

        print("\nTesting books endpoint...")
        print(f"URL: http://localhost:9007/api/books")

        with urllib.request.urlopen(req, timeout=30) as response:
            response_data = response.read().decode('utf-8')
            print(f"Status: {response.status}")
            print(f"Response: {response_data}")
            return response_data

    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        error_response = e.read().decode('utf-8')
        print(f"Error response: {error_response}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print("=== Library Management System API Test ===\n")

    # Test login
    login_result = test_login()

    # Extract token if login successful
    token = None
    if login_result and 'token' in login_result:
        token = login_result['token']
        print(f"✅ Login successful! Token: {token[:50]}...")
    else:
        print("❌ Login failed or no token received")

    # Test books endpoint
    books_result = test_books_endpoint(token)

    if books_result:
        print("✅ Books endpoint accessible")
    else:
        print("❌ Books endpoint failed")

    print("\n=== Test Complete ===")