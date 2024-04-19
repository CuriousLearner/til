# Handle CORS in a Simple HTTP Server

This is a simple HTTP server that serves the current directory and handles CORS by adding the `Access-Control-Allow-Origin` header to the response. This is useful when you are working with frontend applications that need to make requests to a server running on a different domain.

```python
from http.server import SimpleHTTPRequestHandler
import socketserver

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

with socketserver.TCPServer(("", 8000), CORSRequestHandler) as httpd:
    print("Serving at port 8000")
    httpd.serve_forever()
```

Save this script as `server.py` and run it using `python server.py`. This will start a simple HTTP server that serves the current directory and handles CORS by allowing requests from any origin.

You can access the server at `http://localhost:8000` and make requests from your frontend application without any CORS restrictions.

This is a quick way to set up a simple HTTP server for development purposes and handle CORS without having to configure a full-fledged web server like Apache or Nginx.

**Note:** This server is not suitable for production use as it lacks security features and is not optimized for performance. It is intended for development purposes only.
