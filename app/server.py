from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # En-têtes de réponse
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Contenu de la réponse
        message = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Serveur HTTP Simple</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }
                h1 {
                    color: #2c3e50;
                }
                .container {
                    background-color: #ecf0f1;
                    border-radius: 5px;
                    padding: 20px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Hello, Docker!</h1>
            <div class="container">
                <p>Ceci est un serveur HTTP minimaliste créé avec le module <code>http.server</code> de Python.</p>
                <p>Le serveur fonctionne depuis un conteneur Docker.</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(message.encode("utf-8"))

# Démarrage du serveur


if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serveur démarré sur le port {PORT}...")
    httpd.serve_forever()