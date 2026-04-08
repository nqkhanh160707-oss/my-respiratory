import http.server
import socketserver
import json
import math
from urllib.parse import urlparse

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class PrimeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/prime_number/"):
            try:
                number_str = parsed.path.split("/prime_number/")[1]
                number = int(number_str)
                result = {
                    "Number": number,
                    "isPrime": is_prime(number)
                }
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result).encode("utf-8"))
            except ValueError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid number"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

if __name__ == "__main__":
    PORT = 5000
    with socketserver.TCPServer(("", PORT), PrimeHandler) as httpd:
        print(f"Prime checker server running on http://127.0.0.1:{PORT}")
        print("Example: http://127.0.0.1:5000/prime_number/31")
        httpd.serve_forever()
        # sdajsdj i dont know what to say about this