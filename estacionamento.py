"""
Autor: Lucas VIeira
Data de criação: 17/06/2024
"""

def menu():
    """
    Exibe o menu de opções para o usuário.
    
    Returns:
        str: A opção escolhida pelo usuário.
    """
    print("\n----- Menu -----")  # Exibe o título do menu.
    print("1 - Estacionar veículo")  # Exibe a opção 1 do menu.
    print("2 - Retirar veículo")  # Exibe a opção 2 do menu.
    print("3 - Veículos estacionados")  # Exibe a opção 3 do menu.
    print("4 - Está estacionado?")  # Exibe a opção 4 do menu.
    print("0 - Sair")  # Exibe a opção 0 do menu, que permite sair do programa.
    return input("Escolha uma opção: ")  # Retorna a opção escolhida pelo usuário.

def estacionar_veiculo(estacionamento, default_proprietario):
    """
    Estaciona um veículo no estacionamento.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
        default_proprietario (str): O nome do proprietário padrão.
    """
    placa = input("Digite a placa do veículo: ")  # Solicita a placa do veículo.
    if placa in estacionamento:  # Verifica se a placa já está no dicionário 'estacionamento'.
        print("Veículo já está estacionado.")  # Informa que o veículo já está estacionado.
        return  # Sai da função sem fazer nada.
    marca = input("Digite a marca do veículo: ")  # Solicita a marca do veículo.
    modelo = input("Digite o modelo do veículo: ")  # Solicita o modelo do veículo.
    cor = input("Digite a cor do veículo: ")  # Solicita a cor do veículo.
    proprietario = input(f"Digite o nome do proprietário (ou pressione Enter para usar '{default_proprietario}'): ")  # Solicita o nome do proprietário ou permite usar o proprietário padrão.
    if not proprietario:  # Se o usuário não digitar nada, usa o proprietário padrão.
        proprietario = default_proprietario
    estacionamento[placa] = {  # Adiciona o veículo ao dicionário 'estacionamento' com a placa como chave e os outros dados como valores.
        'marca': marca,
        'modelo': modelo,
        'cor': cor,
        'proprietario': proprietario
    }
    print("Veículo estacionado com sucesso.")  # Informa que o veículo foi estacionado com sucesso.

def retirar_veiculo(estacionamento):
    """
    Retira um veículo do estacionamento.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
    """
    placa = input("Digite a placa do veículo: ")  # Solicita a placa do veículo.
    if placa in estacionamento:  # Verifica se a placa está no dicionário 'estacionamento'.
        del estacionamento[placa]  # Remove o veículo do dicionário 'estacionamento'.
        print("Veículo retirado com sucesso.")  # Informa que o veículo foi retirado com sucesso.
    else:
        print("Veículo não encontrado.")  # Informa que o veículo não foi encontrado.

def listar_veiculos(estacionamento):
    """
    Lista todos os veículos estacionados.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
    """
    if not estacionamento:  # Verifica se o dicionário 'estacionamento' está vazio.
        print("Nenhum veículo estacionado.")  # Informa que não há veículos estacionados.
    else:
        for placa, dados in estacionamento.items():  # Itera sobre os veículos no dicionário 'estacionamento'.
            print(f"Placa: {placa}, Marca: {dados['marca']}, Modelo: {dados['modelo']}, Cor: {dados['cor']}, Proprietário: {dados['proprietario']}")  # Exibe os dados de cada veículo.

def verificar_veiculo(estacionamento):
    """
    Verifica se um veículo está estacionado.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
    """
    placa = input("Digite a placa do veículo: ")  # Solicita a placa do veículo.
    if placa in estacionamento:  # Verifica se a placa está no dicionário 'estacionamento'.
        dados = estacionamento[placa]  # Obtém os dados do veículo.
        print(f"O veículo está estacionado. Marca: {dados['marca']}, Modelo: {dados['modelo']}, Cor: {dados['cor']}, Proprietário: {dados['proprietario']}")  # Exibe os dados do veículo.
    else:
        print("Veículo não encontrado.")  # Informa que o veículo não foi encontrado.

def main():
    """
    Função principal que gerencia o loop do menu e chama as funções apropriadas.
    """
    estacionamento = {}  # Inicializa o dicionário 'estacionamento' vazio.
    default_proprietario = "Seu Nome"  # Nome do proprietário padrão.
    while True:  # Inicia um loop infinito.
        opcao = menu()  # Exibe o menu e obtém a opção escolhida pelo usuário.
        if opcao == '1':  # Verifica se a opção é 1.
            estacionar_veiculo(estacionamento, default_proprietario)  # Chama a função para estacionar um veículo.
        elif opcao == '2':  # Verifica se a opção é 2.
            retirar_veiculo(estacionamento)  # Chama a função para retirar um veículo.
        elif opcao == '3':  # Verifica se a opção é 3.
            listar_veiculos(estacionamento)  # Chama a função para listar os veículos estacionados.
        elif opcao == '4':  # Verifica se a opção é 4.
            verificar_veiculo(estacionamento)  # Chama a função para verificar se um veículo está estacionado.
        elif opcao == '0':  # Verifica se a opção é 0.
            print("Saindo...")  # Informa que o programa está saindo.
            break  # Sai do loop infinito.
        else:
            print("Opção inválida. Tente novamente.")  # Informa que a opção é inválida.

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa.
