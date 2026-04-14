from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    """
    Simple HTTP request handler.
    """

    def do_GET(self) -> None:
        """
        Handle GET request.
        """
        message: str = f"Hello from {self.path}"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


def run(server: ThreadingHTTPServer) -> None:
    """
    Start HTTP server.
    """
    server.serve_forever()


server: ThreadingHTTPServer = ThreadingHTTPServer(("", 8000), Handler)

if __name__ == "__main__":
    run(server)