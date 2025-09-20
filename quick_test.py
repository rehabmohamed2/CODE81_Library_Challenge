#!/usr/bin/env python3
import http.client

def quick_test():
    """Quick test to check what endpoints are available"""
    try:
        conn = http.client.HTTPConnection('localhost', 9007, timeout=5)

        # Test different endpoints
        endpoints = [
            "/api/",
            "/api/auth/login",
            "/api/books",
            "/api/categories",
            "/api/health",
            "/api/actuator/health"
        ]

        for endpoint in endpoints:
            try:
                print(f"\nTesting GET {endpoint} ...")
                conn.request("GET", endpoint)
                response = conn.getresponse()
                data = response.read()
                print(f"Status: {response.status} {response.reason}")
                if data:
                    print(f"Response length: {len(data)} bytes")
                    if len(data) < 200:
                        print(f"Response: {data.decode('utf-8')}")
            except Exception as e:
                print(f"Error for {endpoint}: {e}")

        conn.close()

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    quick_test()