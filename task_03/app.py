from http.server import BaseHTTPRequestHandler, HTTPServer

from task_03.controller import MessageController

HOST = 'localhost'
PORT = 8000


class MyServer(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.controller = MessageController
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(code=200)
        self.send_header(keyword='Content-type', value='text/html')
        self.end_headers()
        message = self.controller.get_message()
        self.wfile.write(bytes(message, 'utf-8'))

    def do_POST(self):
        self.send_response(code=200)
        self.send_header(keyword='Content-type', value='application/json')
        self.end_headers()

        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode('utf-8')
        print(post_data_str)

        success_message = self.controller.get_success_message()
        self.wfile.write(bytes(success_message, 'utf-8'))


if __name__ == '__main__':
    web_server = HTTPServer(server_address=(HOST, PORT), RequestHandlerClass=MyServer)
    print('Server started http://%s:%s' % (HOST, PORT))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped')
