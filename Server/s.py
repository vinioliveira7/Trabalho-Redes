import socket
import threading
import time
import os

# Função para lidar com as conexões dos clientes
def handle_client(client_socket):
    while True:
        request = client_socket.recv(10000000).decode('utf-8')
        if not request:
            break

        response = process_request(request)
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

# Função para processar a requisição do cliente
def process_request(request):
    if request == 'CONSULTA':
        return 'DADOS Informações fictícias'
    elif request == 'HORA':
        return 'HORA_ATUAL ' + time.strftime('%H:%M:%S')
    elif request.startswith('ARQUIVO'):
        arquivo_nome = request.split(' ')[1]

        # Verifica se o arquivo existe
        if os.path.exists(arquivo_nome):
            with open(arquivo_nome, 'rb') as arquivo:
                arquivo_conteudo = arquivo.read()
            return f'ARQUIVO {arquivo_nome} {arquivo_conteudo.decode("latin-1")}'

        return f'ARQUIVO {arquivo_nome} Arquivo não encontrado.'
    elif request == 'LISTAR':
        # Simula uma lista de arquivos disponíveis
        arquivos_disponiveis = 'arquivo1.txt arquivo2.txt'
        return f'ARQUIVOS {arquivos_disponiveis}'
    elif request == 'SAIR':
        return 'Conexão encerrada.'
    else:
        return 'Comando não reconhecido.'

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print('Servidor pronto para receber conexões...')

# Loop para aceitar múltiplas conexões
while True:
    client_socket, addr = server.accept()
    print(f'Conexão estabelecida com {addr}')
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()