# Server component : Returns interventions list in JSON fields

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        #Interventions list (no database)
        items = [{'id' : 1001,'label': 'Intervention sur site A', 'description': 'Analyse du problème', 'intervenant': 'Jean', 'lieu': 'Paris', 'dateIntervention': '01/02/2024', 'interventionStatus':'Terminé'},
                 {'id' : 1002,'label': 'Intervention sur site B', 'description': 'Panne', 'intervenant': 'Pierre', 'lieu': 'Lyon', 'dateIntervention': '15/02/2024', 'interventionStatus':'Terminé'},
                 {'id' : 1003,'label': 'Intervention sur site C', 'description': 'Surchauffe', 'intervenant': '', 'lieu': 'Marseille', 'dateIntervention': '20/05/2024', 'interventionStatus':'Brouillon'},
                 {'id' : 1004,'label': 'Intervention sur site D', 'description': 'Contrôle', 'intervenant': 'Elise', 'lieu': 'Bègles', 'dateIntervention': '01/06/2024', , 'interventionStatus':'Validé'}
                ]
        try:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
        except:
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())


port = 5201
httpd = HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()