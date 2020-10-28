from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()

        output = ""
        output += "I am working!"

        self.wfile.write(output.encode())

def main():
    PORT = 8081
    server_address = ("localhost", PORT)
    server = HTTPServer(server_address, requestHandler)
    print("Server running on port %s" % PORT)
    server.serve_forever()

if __name__ == "__main__":
    main()
