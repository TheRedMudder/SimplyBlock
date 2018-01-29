from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import parse_qsl
from threading import Thread
#Choose how you want to Process the post data in this function
def processPostData(post=["No Post Data"]):#Print all post data
    for field in post:
        print(field)
class PostHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        print("Gathered Post Data:")
        postData=parse_qsl(self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8"))#Read and Decode Post Data
        Thread(target=processPostData, args=[postData]).start()#Send Post Data to Process
        return SimpleHTTPRequestHandler.do_GET(self) #Handle as no Post Request was given
print("Go to http://localhost/ if PORT 80 taken change it on the line bellow")
TCPServer(("", 80), PostHandler).serve_forever()