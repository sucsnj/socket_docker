import socket

HOST = "server"
PORT = 5000

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Conectado")

    client_socket.sendall(b"Bem vindo, aqui fica o cliente")
    resposta = client_socket.recv(1024)
    print("Resposta:", resposta.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
