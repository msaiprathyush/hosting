from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Aplications</title>
            <script>
                function loadApp(url) {
                    var container = document.getElementById("app-container");
                    container.innerHTML = '<iframe src="' + url + '" width="100%" height="400px" frameborder="0"></iframe>';
                }
            </script>
        </head>
        <body>
            <h1>Welcome to Prathyush's Collection of Projects</h1>
            <ul>
                <li><a href="#" onclick="loadApp('http://18.232.57.19:82'); return false;">ATS with ChatGPT</a></li>
                <li><a href="#" onclick="loadApp('http://18.232.57.19:8501'); return false;">ATS with Google Gemini</a></li>
            </ul>
            <div id="app-container"></div>
        </body>
        </html>
        """

        self.wfile.write(html.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
