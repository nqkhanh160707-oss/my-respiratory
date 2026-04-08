import http.server
import socketserver
import json
from urllib.parse import urlparse

airports = {
    "LFLL": {"icao": "LFLL", "name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    "EGLL": {"icao": "EGLL", "name": "London Heathrow Airport", "city": "London", "country": "GB"},
    "KJFK": {"icao": "KJFK", "name": "John F. Kennedy International Airport", "city": "New York", "country": "US"},
    "VVNB": {"icao": "VVNB", "name": "Noi Bai International Airport", "city": "Hanoi", "country": "VN"},
   
}

class AirportHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/airport/"):
            icao = parsed.path.split("/airport/")[1].upper().strip()
            airport = airports.get(icao)
            if airport:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(airport).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
                error = {"error": f"Airport with ICAO code '{icao}' not found."}
                self.wfile.write(json.dumps(error).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

if __name__ == "__main__":
    PORT = 5000
    with socketserver.TCPServer(("", PORT), AirportHandler) as httpd:
        print(f"Airport server running on http://127.0.0.1:{PORT}")
        print("Example: http://127.0.0.1:5000/airport/LFLL")
        httpd.serve_forever()

        #i dont think PIP free or APi free will be long like this