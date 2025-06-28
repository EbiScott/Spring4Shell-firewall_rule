# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler


from http.server import BaseHTTPRequestHandler, HTTPServer


host = "localhost"
port = 8000


#########
# Handle the response here 
def block_request(self):
    print("Blocking request")


def handle_request(self):
    if self.command == "POST":
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
    else:
        body = ""

    malicious_pattern = "class.module.classLoader.resources.context.parent.pipeline.first.pattern"
    if malicious_pattern in body:
        block_request(self)
        self.send_response(403)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "blocked"}')
        return

    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(b'{"status": "allowed"}')


#########




class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request(self)


    def do_POST(self):
        handle_request(self)


if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))


    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)