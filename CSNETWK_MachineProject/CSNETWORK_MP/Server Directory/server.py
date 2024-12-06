# De Jesus, Andrei Zarmin D. 
# Perez, Patrick Hans A.

from datetime import datetime
import socket
import threading
import os
from pathlib import Path

HEADER = 512
FORMAT = 'utf-8'

IP_ADDRESS = "127.0.0.1"
PORT = 12345
ADDR = (IP_ADDRESS, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

list_client_names = []  # Holds the list of names of active clients in the server

def handle_client(conn, addr):
    current_client = ""
    print(f"[NEW CONNECTION] {addr} connected") # prints to server interface

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            cmd_key = msg.split()

            if cmd_key[0] == "/join":
                conn.send("Connection to the File Exchange Server is successful!".encode(FORMAT))

            elif cmd_key[0] == "/leave":
                if len(cmd_key) == 1:
                    connected = False
                    conn.send("Connection closed. Thank you!".encode(FORMAT))
                    if current_client != "":
                        list_client_names.remove(current_client)
                else:
                    conn.send("Error: Command parameters do not match or is not allowed.".encode(FORMAT))

            elif cmd_key[0] == "/register":
                if len(cmd_key) == 2 and cmd_key[1]:
                    temp_client_name = cmd_key[1]
                    if temp_client_name not in list_client_names:
                        current_client = temp_client_name
                        list_client_names.append(current_client)
                        conn.send(f"Welcome {current_client}!".encode(FORMAT))
                    else:
                        conn.send("Error: Registration failed. Handle or alias already exists.".encode(FORMAT))
                else:
                    conn.send("Error: Command parameters do not match or is not allowed.".encode(FORMAT))

            elif cmd_key[0] == "/store":
                # Define the source and destination paths
                to_path = Path.cwd() / "CSNETWORK_MP" / "Server Directory"

                store_prompt = cmd_key[0:2]  # not including 2 onwards

                if len(store_prompt) >= 2:
                    file_name = cmd_key[1]
                    file_path = to_path / file_name

                    # Assuming cmd_key is a list
                    temp = "".join(cmd_key[2:])  # Joins the elements from index 2 onward into a string

                    # Get the current date and time
                    current_time = datetime.now()
                    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

                    with open(file_path, "w") as file:
                        file.write(temp)
                    file.close()
                    # Send the message with the current date and time
                    conn.send(f"{current_client} {formatted_time}:\nUploaded\n{file_name}".encode(FORMAT))
                else:
                    conn.send("Error: Command parameters do not match or is not allowed.".encode(FORMAT))


            elif cmd_key[0] == "/dir":
                path = Path.cwd() / "CSNETWORK_MP" / "Server Directory"

                files = list(path.glob("*"))  # Get all files
                if len(cmd_key) == 1:
                    if files:
                        conn.send(("Server Directory\n" + "\n".join([file.name for file in files])).encode(FORMAT))
                    else:
                        print("No files found in the current directory.")
                        conn.send("No files found in the current directory.".encode(FORMAT))
                else:
                    conn.send("Error: Command parameters do not match or is not allowed.".encode(FORMAT))

        
            elif cmd_key[0] == "/get":
                path = Path.cwd() / "CSNETWORK_MP" / "Server Directory"
                file_path = path / cmd_key[1]
                try:
                    with open(file_path, 'rb') as file:
                        while chunk := file.read(1024):
                            conn.send(chunk)
                except FileNotFoundError:
                    print("File not found.")
                    conn.send(b"Error: File not found.")
                finally:
                    conn.send(b"EOF")
                
                    
            print(f"{addr}: {msg}")  # Optional, remove in production for cleaner output

    conn.close()


def start():
    server.listen()
    print(f"> SERVER HAS STARTED [IP ADDRESS: {IP_ADDRESS} ON PORT: {PORT}]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("\nSERVER INTERFACE")
start()
        