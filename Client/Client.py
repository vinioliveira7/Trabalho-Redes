import socket
import os

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Função para enviar comandos ao servidor e receber respostas
def send_request(command):
    client.send(command.encode('utf-8'))
    response = client.recv(1000000000).decode('utf-8')

    # Verifica se a resposta contém dados de arquivo
    if response.startswith('ARQUIVO'):
        parts = response.split(' ', 2)
        arquivo_nome = parts[1]
        arquivo_conteudo = parts[2]

        # Salva o conteúdo do arquivo no diretório local do cliente
        caminho_arquivo = os.path.join(os.getcwd(), arquivo_nome)
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(arquivo_conteudo.encode('utf-8'))

        return f'Arquivo {arquivo_nome} recebido e salvo localmente!'
    else:
        return response


try:
    while True:
        print("Comandos disponíveis:")
        print("1. CONSULTA")
        print("2. HORA")
        print("3. ARQUIVO <nome>")
        print("4. LISTAR")
        print("5. SAIR")

        choice = input("Escolha um comando (1-5): ")

        if choice == '1':
            response = send_request('CONSULTA')
        elif choice == '2':
            response = send_request('HORA')
        elif choice.startswith('3'):
            nome_arquivo = choice.split(' ')[1]
            response = send_request('ARQUIVO ' + nome_arquivo)
        elif choice == '4':
            response = send_request('LISTAR')
        elif choice == '5':
            response = send_request('SAIR')
            client.close()
            break
        else:
            response = 'Comando inválido.'

        print(response)

except KeyboardInterrupt:
    client.close()