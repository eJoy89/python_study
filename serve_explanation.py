import http.server
import socketserver

PORT = 8000  # Port can be any available port
DIRECTORY = "/mnt/python_study_h"  # Directory to serve

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

