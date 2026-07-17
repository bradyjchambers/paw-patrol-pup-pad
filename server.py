import http.server
import socketserver
import json

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        state = "idle"
        if "param=bad" in post_data:
            state = "bad"
        elif "param=good" in post_data:
            state = "good"
        elif "param=idle" in post_data:
            state = "idle"
            
        with open("state.json", "w") as f:
            json.dump({"state": state}, f)
            
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success", "state": state}).encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Pup Pad Server listening on port {PORT}...")
    httpd.serve_forever()
