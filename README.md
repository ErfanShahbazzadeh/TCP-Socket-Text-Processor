# TCP Socket Text Processor (Client + Server)

A lightweight, educational TCP client-server application built with Python's `socket` library. The server accepts text from a client, converts it to uppercase, and returns the transformed text — demonstrating fundamental network programming concepts.

## Features

- **TCP Socket Communication** – Reliable, connection-oriented data transfer
- **Text Transformation** – Server converts received text to uppercase
- **Reusable Address** – Server socket allows immediate restarts without "address already in use" errors
- **Graceful Error Handling** – Client displays connection errors when server is unavailable
- **Interactive Client Loop** – Send multiple messages until typing `quit`

## Requirements

- Python 3.x (No external dependencies — uses only the standard library)

## Installation

```bash
git clone https://github.com/yourusername/tcp-socket-text-processor.git
cd tcp-socket-text-processor
```

## Usage

### 1. Start the Server

```bash
python Server.py
```

Output:
```
Server listening on 127.0.0.1:12345
```

### 2. Run the Client (in a separate terminal)

```bash
python client.py
```

Example interaction:
```
Enter text to send (or 'quit' to exit): hello world
Connected to server at 127.0.0.1:12345
Sent: hello world
Received: HELLO WORLD

Enter text to send (or 'quit' to exit): python networking is fun
Connected to server at 127.0.0.1:12345
Sent: python networking is fun
Received: PYTHON NETWORKING IS FUN

Enter text to send (or 'quit' to exit): quit
```

### 3. Server Output (during client interaction)

```
Server listening on 127.0.0.1:12345
Connection from ('127.0.0.1', 54321)
Received: hello world
Sent: HELLO WORLD
Client disconnected
Connection from ('127.0.0.1', 54322)
Received: python networking is fun
Sent: PYTHON NETWORKING IS FUN
Client disconnected
```

## Architecture

```
┌─────────┐    TCP Connect     ┌─────────┐
│ Client  │ ─────────────────> │ Server  │
│         │    (Port 12345)    │         │
│         │                    │         │
│ "hello" │ ──── send() ────>  │ recv()  │
│         │                    │         │
│         │  <─── send() ────  │ upper() │
│ "HELLO" │    recv()          │         │
└─────────┘                    └─────────┘
```

## Configuration

Modify connection settings in either script:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `host` | `127.0.0.1` | Localhost (change to `0.0.0.0` for remote access) |
| `port` | `12345` | TCP port (ensure firewall allows it) |

## Error Handling

| Scenario | Client Behavior | Server Behavior |
|----------|----------------|-----------------|
| Server not running | `ConnectionRefusedError` with message | N/A |
| Client disconnects unexpectedly | N/A | Closes connection gracefully |
| Network interruption | Exception caught and displayed | Exception caught, client connection closed |

## Extending the Project

Ideas for further development:

- **Multi-client support** – Use threading to handle concurrent clients
- **Custom transformations** – Add encryption, compression, or formatting
- **File transfer** – Send and receive files over TCP
- **Protocol design** – Add headers or message delimiters
- **Asynchronous I/O** – Refactor with `asyncio` for higher concurrency

## Learning Outcomes

This project demonstrates:

- Python socket programming (AF_INET, SOCK_STREAM)
- TCP connection lifecycle: `socket()` → `bind()` → `listen()` → `accept()` (server)
- TCP connection lifecycle: `socket()` → `connect()` → `send()` → `recv()` (client)
- String encoding/decoding with UTF-8
- Socket option `SO_REUSEADDR` for port reusability
- Graceful resource cleanup with `try/finally`

## License

MIT License — free for educational and commercial use.

## Author

**Erfan Shahbazzadeh**
- GitHub: [@ErfanShahbazzadeh](https://github.com/ErfanShahbazzadeh)

---

*Built for learning, understanding, and demonstrating TCP socket communication in Python.*
