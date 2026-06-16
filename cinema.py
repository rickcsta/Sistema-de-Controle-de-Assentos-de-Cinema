from assento import Assento
from pathlib import Path

FILEIRAS = ["A", "B", "C", "D", "E"]
NUMEROS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def carregar_assentos():
    dados = {}

    for fileira in FILEIRAS:
        for numero in NUMEROS:
            assento = Assento(fileira, numero)
            dados[assento.coordenada()] = assento

    if not Path("sala.txt").is_file():
        return dados

    with open("sala.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            fileira, numero, ocupado, comprador = linha.strip().split(":")

            coordenada = fileira + numero

            dados[coordenada].ocupado = ocupado == "True"

            dados[coordenada].comprador = comprador

    return dados

def salvar_assentos(dados):
    with open("sala.txt", "w", encoding="utf-8") as arquivo:
        for assento in dados.values():
            arquivo.write(assento.linha_armazenamento() + "\n")

def mostrar_menu():
    while True:
        print("\nMapa de acentos - Escolha uma opção")
        print("1. Disponibilidade de assentos")
        print("2. Vender entrada")
        print("3. Sair")

        while True:
            try:
                op = int(input("Opção: "))

                if 1 <= op <= 3:
                    return op

                print("Opção inválida. Tente novamente.")

            except ValueError:
                print("Digite apenas números.")

def exibir_disponibilidade(dados):
    print("\n     ", end="")

    for numero in NUMEROS:
        print(f"{numero:>4}", end="")
    print()

    disponiveis = 0

    for fileira in FILEIRAS:
        print(f"  {fileira}  ", end="")

        for numero in NUMEROS:
            coordenada = f"{fileira}{numero}"
            assento = dados[coordenada]

            if assento.ocupado:
                status = "O"
            else:
                status = "D"
                disponiveis += 1

            print(f"   {status}", end="")

        print()

    print(f"\nTotal de assentos disponíveis: {disponiveis}/{len(dados)}")

def vender_entrada(dados):
    exibir_disponibilidade(dados)

    coordenada = input(
        "\nDigite a coordenada do assento (Ex: B4): "
    ).strip().upper()

    if coordenada not in dados:
        print("Coordenada inválida.")
        return

    assento = dados[coordenada]

    if assento.ocupado:
        print(
            f"Assento {coordenada} já está ocupado por {assento.comprador}."
        )
        return

    comprador = input("Nome do comprador: ").strip()

    if not comprador:
        print("Nome obrigatório.")
        return

    assento.ocupado = True
    assento.comprador = comprador

    print(f"Assento {coordenada} vendido com sucesso para {comprador}!")

dados = carregar_assentos()

while True:
    opcao = mostrar_menu()

    if opcao == 1:
        exibir_disponibilidade(dados)

    elif opcao == 2:
        vender_entrada(dados)
        salvar_assentos(dados)

    elif opcao == 3:
        salvar_assentos(dados)
        print("Saindo... dados salvos em sala.txt.")
        break