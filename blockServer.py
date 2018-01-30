from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import parse_qsl
from threading import Thread
#Choose how you want to Process the post data in this function
port= 80
def processPostData(post=["No Post Data"]):#Print all post data
    for field in post:
        print(field)
def terminateServer(server):
    server.shutdown()
class PostHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        print("Gathered Post Data:")
        postData=parse_qsl(self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8"))#Read and Decode Post Data
        Thread(target=processPostData, args=[postData]).start()#Send Post Data to Process
        return SimpleHTTPRequestHandler.do_GET(self) #Handle as no Post Request was given
    def do_GET(self):
        if self.path.endswith("exit.html"):#Terminate Server in Thread
            self.send_response(200, 'OK')
            print("blockServer Terminated")
            self.wfile.write(bytes("<h1> blockServer Terminated </h1>", 'UTF-8'))
            Thread(target=terminateServer, args=[server]).start()  # Send Post Data to Process
        else:
            return SimpleHTTPRequestHandler.do_GET(self) #Handle as no Post Request was given
print("Go to http://localhost/ if PORT %s  taken change it on the line bellow" %port)
server=TCPServer(("", port), PostHandler)
server.serve_forever()
