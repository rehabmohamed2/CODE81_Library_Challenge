#!/usr/bin/env python3
import http.client
import json
import time

def test_http_connection():
    """Test HTTP connection using low-level http.client"""
    try:
        # Create connection
        conn = http.client.HTTPConnection('localhost', 9007, timeout=15)

        # Test basic connectivity to root
        print("Testing GET /api/ ...")
        conn.request("GET", "/api/")
        response = conn.getresponse()
        data = response.read()
        print(f"Status: {response.status} {response.reason}")
        print(f"Headers: {dict(response.getheaders())}")
        print(f"Response: {data.decode('utf-8')[:500]}...")

        conn.close()
        return True

    except Exception as e:
        print(f"Connection error: {e}")
        return False

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

if __name__ == "__main__":
    print("=== HTTP Client Test ===\n")

    # Test basic connection
    if test_http_connection():
        print("✓ Basic HTTP connection works\n")
    else:
        print("✗ Basic HTTP connection failed\n")

    # Test login
    login_result = test_login()
    if login_result and 'token' in login_result:
        print(f"✓ Login successful! Token received.")
    else:
        print("✗ Login failed")

    print("\n=== Test Complete ===")