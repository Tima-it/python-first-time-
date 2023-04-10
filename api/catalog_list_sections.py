from http.server import BaseHTTPRequestHandler
import sqlite3 as sq

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # self.wfile.write('Hello, world!'.encode('utf-8'))

        con = sq.connect("db")
        cur = con.cursor()


        con.commit()
        sections = cur.execute("SELECT * FROM `catalog_sections`")
        self.wfile.write(print(*sections, sep = ", "))

        return


