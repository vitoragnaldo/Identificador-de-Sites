import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

contador_consultas = 0


def identificar_site(url):
    global contador_consultas

    try:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        resposta = requests.get(url, timeout=10)

        soup = BeautifulSoup(resposta.text, "html.parser")

        titulo = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "Título não encontrado"
        )

        dominio = urlparse(resposta.url).netloc

        https = "Sim" if resposta.url.startswith("https://") else "Não"

        redirecionamentos = len(resposta.history)

        contador_consultas += 1

        print("\n" + "=" * 50)
        print("RESULTADO DA CONSULTA")
        print("=" * 50)
        print(f"Site identificado : {titulo}")
        print(f"Domínio           : {dominio}")
        print(f"URL final         : {resposta.url}")
        print(f"Status HTTP       : {resposta.status_code}")
        print(f"HTTPS             : {https}")
        print(f"Redirecionamentos : {redirecionamentos}")
        print(f"Consultas feitas  : {contador_consultas}")
        print("=" * 50)

        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open("historico_consultas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"{data_hora} | "
                f"{titulo} | "
                f"{dominio} | "
                f"{resposta.url} | "
                f"HTTP {resposta.status_code}\n"
            )

    except requests.exceptions.ConnectionError:
        print("\nErro: não foi possível conectar ao site.")

    except requests.exceptions.Timeout:
        print("\nErro: tempo de resposta excedido.")

    except requests.exceptions.RequestException as erro:
        print(f"\nErro: {erro}")


while True:
    print("\n")
    print("=" * 50)
    print("IDENTIFICADOR DE SITES")
    print("=" * 50)

    url = input("Digite a URL: ").strip()

    identificar_site(url)

    print("\nO que deseja fazer?")
    print("1 - Consultar outra URL")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    while opcao not in ["1", "2"]:
        opcao = input("Opção inválida. Digite 1 ou 2: ").strip()

    if opcao == "2":
        print("\nObrigado por utilizar o sistema!")
        print("Histórico salvo em 'historico_consultas.txt'.")
        break