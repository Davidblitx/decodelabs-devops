from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <html>
        <body style="font-family:sans-serif; text-align:center; padding:50px; background:#0d1117; color:#fff;">
            <h1>DecodeLabs DevOps</h1>
            <p>Containerized with Docker | Project 4</p>
            <p style="color:#f97316;">Build. Ship. Run.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        print(f"[REQUEST] {args[0]} {args[1]}")

if __name__ == '__main__':
    print("Server starting on port 8080...")
    HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
