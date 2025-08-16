import csv
from pathlib import Path

ARQUIVO = Path("dados_escola.csv")
CAMPOS = ["ID_Aluno", "Nome", "Idade", "Ano_Serie", "Nota"]

def carregar_arquivo():
    """Carregar o arquivo existente"""
    if not ARQUIVO.exists():
        return [],1

    with ARQUIVO.open(newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = list(leitor)

    return dados, len(dados)

def salvar(dados):
    """Salvar os dados no CSV"""
    with ARQUIVO.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(dados)

def main():
    dados, proximo_id = carregar_arquivo()
    print("Arquivo:", ARQUIVO.resolve())
    print("Campos: ", CAMPOS)

    print("Para parar o sistema, deixe o nome em branco e pressona enter...")

    while True:
        nome = input("Nome: ")
        if nome == "":
            break
        idade = input("Idade: ")
        serie = input("Serie: ")
        nota = input("Nota: ")

        registro = {
            "ID_Aluno": str(proximo_id),
            "Nome": nome,
            "Idade": idade,
            "Serie": serie,
            "Nota": nota
        }

        dados.append(registro)
        proximo_id += 1
        print("Adicionado com sucesso!")

    salvar(dados)
    print("Dados salvos com sucesso! Em: ", ARQUIVO.resolve())

if __name__ ==  "__main__":
    main()