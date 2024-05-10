import requests
import csv

def extrair_fatos_sobre_gatos():
    # URL da API de fatos sobre gatos
    url = "https://cat-fact.herokuapp.com/facts"

    print(f"Inicializando a requisição na url {url}")
    try:
        # Realizando a requisição GET
        response = requests.get(url)
        response.raise_for_status()

        # Convertendo a resposta para JSON
        data = response.json()

        fatos = []

        # Extraindo os fatos
        for item in data:
            fatos.append(item["text"])
            # aqui eu fiquei na dúvida de como salvar de fato. se o json inteiro ou não.
            # então eu deixei acima pegando apenas a parte de "text"
            # e abaixo comentado deixei puxando todo o json.
            # fatos.append(item)

        return fatos
    # Lançando uma exceção em caso de falha na requisição
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição:", e)
        return None


def salvar_em_csv(fatos, nome_arquivo):
    try:
        # Abre o arquivo CSV para escrita
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            # Cria um escritor CSV
            escritor_csv = csv.writer(arquivo)

            # Escreve os fatos no arquivo CSV
            for fato in fatos:
                escritor_csv.writerow([fato])

        print("Fatos sobre gatos salvos em", nome_arquivo)
    

    except IOError:
        print("Erro ao escrever no arquivo CSV")

if __name__ == "__main__":
    # Extrai os fatos sobre gatos da API
    fatos = extrair_fatos_sobre_gatos()

    if fatos:
        # Salva os fatos em um arquivo CSV local
        salvar_em_csv(fatos, "fatos_sobre_gatos.csv")
    else:
        print("Não foi possível extrair os fatos sobre gatos.")