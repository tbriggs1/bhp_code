# A socket is simply an endpoint, an address that can recieve data
import socket
import threading

IP = '0.0.0.0'
PORT = 9997

def main():
    # Creates an object of type socket and specifies that server should be IPV4 (AF_INET) and TCP (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind() assigns an IP and PORT to a socket instance
    server.bind((IP, PORT))
    # Listens to incoming traffic, if one request hasn't finished processing, a second request goes into a queue. 5 is the maxium requests in a queue
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # Address is the address which the client is coming from, this will be sent in a object of IP and PORT
        # Client will be the entire object including socket type, data sent etc...
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # The threading library allows you to run threads, so if multiple clients sent data at the sametime it wouldn't bug out 
        # threading.Thread creates a new thread object, you pass it the function you want to run, and any arguments that function has.
        # threading.Thread(target=handle_client, args=(client,)) is the same as handle_client(client) - client_handler.start() runs the function
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    # Passes through the client socket object and stores it in the sock variable
    with client_socket as sock:
        # The below receives the message that has been sent from the client socket object and stores it in request
        request = sock.recv(1024)
        # The message will be encoded into packets and bytes, the decode method will decode the message into utf-8
        print(f'[*] Recieved: {request.decode("utf-8")}')
        # sock.send, sends a message back to the client as needed in TCP. 
        sock.send(b'ACK')

if __name__ == '__main__':
    main()