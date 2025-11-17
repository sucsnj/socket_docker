import socket

HOST = "0.0.0.0" 
PORT = 5000 

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Escutando em {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Mensagem recebida: {data.decode()}")
        conn.sendall(b"Mensagem recebida")

    conn.close()

if __name__ == "__main__":
    main()
