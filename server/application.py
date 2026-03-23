"""
This module provides application functionality.
"""
import http.server
import socketserver

PORT = 8000
class TestMe():
    """
    This is TestMe calss.
    """
    def take_five(self):
        """
        This is take five function.
        """
        return 5
    def port(self):
        """
        This is return port function.
        """
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("",PORT),Handler) as http:
        print("servingatport",PORT)
        http.serve_forever()
