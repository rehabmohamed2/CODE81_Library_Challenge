#!/usr/bin/env python3
import http.client
import json

def test_auth_endpoint_methods():
    """Test different HTTP methods on auth endpoint"""
    print("TESTING AUTH ENDPOINT METHODS")
    print("="*40)

    methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

    for method in methods:
        try:
            conn = http.client.HTTPConnection('localhost', 9007, timeout=10)

            print(f"\n>>> {method} /api/auth/login")

            if method == "POST":
                data = json.dumps({"username": "admin", "password": "password123"})
                headers = {
                    'Content-Type': 'application/json',
                    'Content-Length': str(len(data)),
                    'Accept': 'application/json'
                }
                conn.request(method, "/api/auth/login", body=data, headers=headers)
            else:
                conn.request(method, "/api/auth/login")

            response = conn.getresponse()
            data = response.read()

            print(f"    Status: {response.status} {response.reason}")
            if data:
                print(f"    Response: {data.decode('utf-8')[:200]}...")

            conn.close()

        except Exception as e:
            print(f"    Error: {e}")

def test_h2_console():
    """Test H2 console access"""
    print("\n" + "="*40)
    print("TESTING H2 CONSOLE")
    print("="*40)

    try:
        conn = http.client.HTTPConnection('localhost', 9007, timeout=10)

        print(">>> GET /h2-console")
        conn.request("GET", "/h2-console")
        response = conn.getresponse()
        data = response.read()

        print(f"Status: {response.status} {response.reason}")
        if response.status == 200:
            print("H2 Console is accessible!")
        else:
            print("H2 Console access issue")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")

def test_different_auth_paths():
    """Test different auth-related paths"""
    print("\n" + "="*40)
    print("TESTING AUTH PATHS")
    print("="*40)

    paths = [
        "/api/auth",
        "/api/auth/",
        "/api/auth/login",
        "/api/auth/register"
    ]

    for path in paths:
        try:
            conn = http.client.HTTPConnection('localhost', 9007, timeout=5)

            print(f"\n>>> GET {path}")
            conn.request("GET", path)
            response = conn.getresponse()
            data = response.read()

            print(f"    Status: {response.status} {response.reason}")

            conn.close()

        except Exception as e:
            print(f"    Error: {e}")

if __name__ == "__main__":
    print("AUTHENTICATION ENDPOINT TESTING")
    print("Server: http://localhost:9007")

    test_auth_endpoint_methods()
    test_different_auth_paths()
    test_h2_console()

    print("\n" + "="*40)
    print("ENDPOINT DISCOVERY COMPLETE")
    print("="*40)