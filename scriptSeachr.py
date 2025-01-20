import requests
from urllib.parse import urljoin
import logging
from termcolor import colored

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ResponseComparer:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

    def get_response(self, url):
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            return {
                'status': response.status_code,
                'size': len(response.content),
                'content': response.text
            }
        except requests.RequestException as e:
            logging.error(f"Error accessing {url}: {str(e)}")
            return None

    def compare_endpoints(self, base_url):
        # Clean up the base URL
        if not base_url.startswith(('http://', 'https://')):
            base_url = 'http://' + base_url

        # Generate endpoint URLs
        login_url = urljoin(base_url, 'login.php')
        index_url = urljoin(base_url, 'index.php')

        # Get responses
        logging.info(colored(f"Accessing {login_url}", 'yellow'))
        login_response = self.get_response(login_url)

        logging.info(colored(f"Accessing {index_url}", 'yellow'))
        index_response = self.get_response(index_url)

        if login_response and index_response:
            # Compare sizes
            size_diff = abs(login_response['size'] - index_response['size'])
            
            # Save responses
            with open('response.txt', 'w', encoding='utf-8') as f:
                f.write(f"=== Login.php Response ===\n")
                f.write(f"Size: {login_response['size']} bytes\n")
                f.write(f"Status: {login_response['status']}\n")
                f.write(f"Content:\n{login_response['content']}\n\n")
                
                f.write(f"=== Index.php Response ===\n")
                f.write(f"Size: {index_response['size']} bytes\n")
                f.write(f"Status: {index_response['status']}\n")
                f.write(f"Content:\n{index_response['content']}\n\n")
                
                f.write(f"Size Difference: {size_diff} bytes")

            # Print results
            print(colored("\nResults:", 'green'))
            print(f"Login.php size: {login_response['size']} bytes")
            print(f"Index.php size: {index_response['size']} bytes")
            print(f"Size difference: {size_diff} bytes")
            print(colored("\nResponses saved to response.txt", 'green'))

def main():
    try:
        comparer = ResponseComparer()
        base_url = input(colored("Enter the base URL (e.g., example.com): ", 'cyan')).strip()
        comparer.compare_endpoints(base_url)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
