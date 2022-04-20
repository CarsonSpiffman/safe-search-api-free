import requests

class SafeContentAPI:
    '''
    [ESP]
    Esta clase se encarga de la comunicacion con la API de SafeContent de Google
    Hacia la API carsonspiffman-safecontent-checker.000webhostapp.com
    SafeContentAPI recibe un parametro que es la Imagen URL a la cual se quiere realizar la consulta
    Envia una peticion POST con la URL que se quiere verificar
    Y devuelve un JSON con el resultado de la verificación
    
    [ENG]
    This class handles communication with Google's SafeContent API.
    To the API carsonspiffman-safecontent-checker.000webhostapp.com
    SafeContentAPI receives a parameter which is the URL image to which the query is to be made.
    Sends a POST request with the URL to be verified
    And returns a JSON with the verification result
    '''
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.data = f"imageURL={self.url}"
        self.response = requests.post('https://carsonspiffman-safecontent-checker.000webhostapp.com/s.php', headers=self.headers, data=self.data)
        self.json = self.response.json()
    
    def get_json(self):
        return self.json
