import urllib.parse
import urllib.request
import json

def recursive_fetch(attempts=10):
    if attempts == 0:
        print("Não foi possível realizar o fetch após 10 tentativas")
        return

    url = "http://localhost:3000/api/v1/auth/login"
    body = {
        "email": "me.contrate.aero@gmail.com.br",
        "password": "Aa1234567"
    }

    try:
        data = urllib.parse.urlencode(body).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            print([data.response])
    except Exception as e:
        print(f"Erro ao fazer fetch: {e}")
        recursive_fetch(attempts - 1)

if __name__ == "__main__":
    recursive_fetch()