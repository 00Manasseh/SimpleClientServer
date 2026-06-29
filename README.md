Simple Client-Server Application Using Python

Project Overview

This project demonstrates a simple client-server application developed using Python socket programming. The application runs on the localhost environment (`127.0.0.1`) and uses the TCP protocol to establish communication between the client and the server.

---

Objective

To design and implement a simple client-server application that demonstrates communication between a client and a server running on the same computer using localhost.

---

Technologies Used

Python 3.14
Visual Studio Code
TCP Socket Programming
Git & GitHub

---

Layered Architecture

| Layer             | Description                                                                             |
| ----------------- | --------------------------------------------------------------------------------------- |
| Application Layer | Contains the `client.py` and `server.py` programs.                                      |
| Socket Layer      | Uses Python's built-in `socket` library to create and manage the connection.            |
| Transport Layer   | Uses the TCP protocol to ensure reliable communication.                                 |
| Network Layer     | Uses the localhost IP address (`127.0.0.1`) for communication within the same computer. |

---

 Communication Process

1. The server starts and waits for a client connection.
2. The client connects to the server using localhost (`127.0.0.1`) on port `5000`.
3. The client sends a message to the server.
4. The server receives the message and processes it.
5. The server sends a response back to the client.
6. The client displays the server's response.

Sample Output

Server

```
Server is running...
Waiting for client to connect...
Connected by: ('127.0.0.1', 4920)
Client says: Hello Server
```

Client

```
Enter a message for the server: Hello Server
Server replied: Server received: Hello Server
```

---

Project Files

```
SimpleClientServer/
│── client.py
│── server.py
│── README.md
```

---

How to Run

1. Open the project in Visual Studio Code.
2. Open a terminal and run:

```
py server.py
```

3. Open a second terminal and run:
```
py client.py
```
4. Enter a message when prompted.



Conclusion

The project successfully demonstrates a basic client-server application using Python sockets. Communication between the client and server was established successfully over TCP on the localhost environment, demonstrating reliable message exchange between system components.
