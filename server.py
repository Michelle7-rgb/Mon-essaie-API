from http.server import BaseHTTPRequestHandler, HTTPServer
from routes import get_routes


class MonServeur(BaseHTTPRequestHandler):

    def do_GET(self):
        routes = get_routes()

        if self.path in routes:
            routes[self.path](self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Route non trouvee")


serveur = HTTPServer(("localhost", 8000), MonServeur)

print("Serveur lance sur http://localhost:8000")

serveur.serve_forever()