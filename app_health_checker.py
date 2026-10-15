import requests
import sys

# Target application URL
APP_URL = "http://localhost:4499"  # Replace with your deployed application URL

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        
        # Check if HTTP status code indicates success (200-399 range)
        if 200 <= response.status_code < 400:
            print(f"Status: UP | Application is functioning correctly. HTTP Status Code: {response.status_code}")
            sys.exit(0)
        else:
            print(f"Status: DOWN | Application responded with failure code: {response.status_code}")
            sys.exit(2)
            
    except requests.exceptions.ConnectionError:
        print(f"Status: DOWN | Connection refused. The application at {url} is unreachable or offline.")
        sys.exit(2)
    except requests.exceptions.Timeout:
        print(f"Status: DOWN | Request timed out while trying to reach {url}.")
        sys.exit(2)
    except Exception as e:
        print(f"Status: DOWN | An unexpected error occurred: {e}")
        sys.exit(2)

if __name__ == "__main__":
    check_application_health(APP_URL)