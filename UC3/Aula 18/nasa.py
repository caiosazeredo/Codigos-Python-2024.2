import requests

def get_apod():
    """
    Obter a imagem astronômica do dia (APOD) da API da NASA e exibir no terminal.
    """
    NASA_API_URL = "https://api.nasa.gov/planetary/apod"
    API_KEY = "kRbLNOGzY0fC3kWDfcZmOYF5xVXfVViUaXf1vKsM"  # Substitua por sua própria chave de API 

    params = {
        'api_key': API_KEY,  # Chave de API fornecida pela NASA
    }

    response = requests.get(NASA_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Título: {data['title']}")
        print(f"Data: {data['date']}")
        print(f"Descrição: {data['explanation']}")
        print(f"URL da imagem: {data['url']}")
    else:
        print("Erro: Não foi possível obter os dados da NASA.")

if __name__ == '__main__':
    get_apod()