import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')

host = 'localhost'
port = 5050

s.bind((host,port))
menssagem = 'servidor: ok'

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print('servidor eviando menssagem')
        s.sendto(dados + (menssagem.encode()),end)