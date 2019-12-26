from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        path = self.path
        if path == "/":
            path = "/index"
        try:
            file = open("pages"+path+".html","r")
        except FileNotFoundError:
            file = open("pages/404.html", "r")
        message = file.read()
        file.close()
        
        self.wfile.write(bytes(message, "cp1251"))
        return

    def do_POST(self):
        self.send_response(301)
        self.send_header('Location','/support')
        self.end_headers()
        path = self.path
        if path == "/email":
            content_len = int(self.headers.get('Content-Length'))
            post = self.rfile.read(content_len)
            email = post.decode().replace("email=","").replace("%40","@")
            print(email)
        return

server = HTTPServer(("", 8000), RequestHandler)
print("Server working...")
server.serve_forever()














