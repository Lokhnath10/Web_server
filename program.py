from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
</head>
<body>
<h1>Top Five Web Application development frameworks </h1>
<h2>1.Django<h2>
<h2>2.MEAN stack<h2>
<h2>3.React<h2>
</body>
</html>
"""
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())



server_address = ('', 80)
httpd = HTTPServer(server_address, HelloHandler)
httpd.serve_forever()