from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import requests

class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        json_response = None
        if self.path == '/':
            json_response = {'service': 'Device simulator: Smart light', 'received': 'ok'}
        if self.path == '/status':
            json_response = {'service': 'Device simulator: Smart light', 'status': 'ON'}
        if (json_response == None):
            self.send_response(404)
            self.end_headers()
        else :
            self._set_headers()
            self.wfile.write(bytes(json.dumps(json_response, ensure_ascii=False), 'utf-8'))

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['Content-Type'])

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length =   content_length = int(self.headers['Content-Length'])
        payload = json.loads(self.rfile.read(length))

        # add a property to the object, just to mess with data
        payload['received'] = 'ok'

        if self.path == '/status':
            # send the message back
            self._set_headers()
            self.wfile.write(bytes(json.dumps(payload), 'utf-8'))
        else:
            notFoundMesage =  {'service': 'Device simulator: Smart light', 'message': 'Not Found'}
            self._set_headers()
            self.wfile.write(bytes(json.dumps(notFoundMesage), 'utf-8'))

httpd = HTTPServer(('0.0.0.0', 8001), Server)
httpd.serve_forever()
