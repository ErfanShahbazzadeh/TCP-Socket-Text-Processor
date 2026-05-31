import socket

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((host, port))
    
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        try:
            data = client_socket.recv(1024).decode('utf-8')
            
            if not data == "Disconnect":
                print(f"Received: {data}")
                
                response = data.upper()
                
                client_socket.send(response.encode('utf-8'))
                print(f"Sent: {response}")
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if data == "Disconnect":
                client_socket.close()
                print("Client disconnected")

if __name__ == "__main__":
    start_server()