# from http.server import HTTPServer, BaseHTTPRequestHandler
# import threading
#
#
# class Serv(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         if self.path == '/':
#             self.path = '../tests/test.html'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#         except:
#             file_to_open = "File not found"
#             self.send_response(404)
#         self.end_headers()
#         self.wfile.write(bytes(file_to_open, 'utf-8'))
#
#
# def start_local_host(port=8080):
#     def thread_function():
#         httpd = HTTPServer(('localhost', port), Serv)
#         httpd.serve_forever()
#     thread = threading.Thread(target=thread_function)
#     thread.daemon = True
#     thread.start()
import eel

def start_gui():
    eel.init("src/client")
    eel.start("index.html")

