# Developing a Simple Webserver
Name: Lokhnath.J 
Ref: 23004865
dept: AIML

# AIM:

Develop a webserver to display about top five web application development frameworks.

# DESIGN STEPS:

## Step 1:

HTML content creation is done

## Step 2:

Design of webserver workflow

## Step 3:

Implementation using Python code

## Step 4:

Serving the HTML pages.

## Step 5:

Testing the webserver
# PROGRAM:
``````
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
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())



server_address = ('', 80)
httpd = HTTPServer(server_address, HelloHandler)
httpd.serve_forever()

``````
# OUTPUT:
![webserver][webserver1](https://github.com/Lokhnath10/Web_server/assets/138969918/ebb80a64-4e4e-48f5-8154-ebd4fd71fae7)
# RESULT:

The program is executed succesfully
