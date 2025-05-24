from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
from os import path

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        # Get names from query parameters
        names = params.get('name', [])
        
        # Load marks data
        file_path = path.join(path.dirname(__file__), '..', 'q-vercel-python.json')
        with open(file_path) as f:
            marks_data = json.load(f)
        
        # Prepare response
        response_marks = []
        for name in names:
            response_marks.append(marks_data.get(name, None))
        
        # Set headers for CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.end_headers()
        
        # Send response
        self.wfile.write(json.dumps({"marks": response_marks}).encode('utf-8'))
        return