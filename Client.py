import socket

def send_text_to_server(text, host='127.0.0.1', port=12345):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((host, port))
        if not text == "Disconnect":
            print(f"Connected to server at {host}:{port}")
        
        client_socket.send(text.encode('utf-8'))
        if not text == "Disconnect":
            print(f"Sent: {text}")
        
        response = client_socket.recv(1024).decode('utf-8')
        if not text == "Disconnect":
            print(f"Received: {response}")
        
        return response
        
    except ConnectionRefusedError:
        print("Could not connect to server. Make sure server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":

    while True:
        message = input("Enter text to send or 'Disconnect': ")
        if message.lower() == 'disconnect':
            send_text_to_server(message)
            print("Server disconnect")
            break
        else:
            send_text_to_server(message)