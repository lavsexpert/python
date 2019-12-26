from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib

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
        global answer
        htmltext = file.read().format(answer = answer)
        file.close()
        
        self.wfile.write(bytes(htmltext, "cp1251"))
        return

    def do_POST(self):
        self.send_response(301)
        self.send_header('Location','/support')
        self.end_headers()
        path = self.path
        if path == "/email":
            content_len = int(self.headers.get('Content-Length'))
            post = self.rfile.read(content_len)
            words = post.decode().split("&")
            email = words[0].replace("email=","").replace("%40","@")
            message = urllib.parse.unquote(words[1].replace("message=",""))
            print(email)
            print(message)
            global answer
            answer = "Мы ответим вам на email: {email}"
            answer = answer.encode('utf-8').decode('cp1251').format(email=email)
        return

answer = ""
server = HTTPServer(("", 8000), RequestHandler)
print("Server working...")
server.serve_forever()














