from socket import *


def smtp_client(port=1025, mailserver='localhost'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfrom = 'MAIL FROM: <test@gmail.com>'
    clientSocket.send(mailfrom.encode())
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptto = 'RCPT TO: <test2@gmail.com>'
    clientSocket.send(rcptto.encode())
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data= 'DATA'
    clientSocket.send(data.encode())
    recvd = clientSocket.recv(1024).decode()
    if recvd[:3] != '250':
    # Fill in end

    # Send message data.
    # Fill in start
        clientSocket.send(msg.encode())
        clientSocket.send(endmsg.encode())

    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT'
    clientSocket.send(quitCommand.encode())
    recvq = clientSocket.recv(1024).decode()


if __name__ == '__main__':
    smtp_client(1025,'127.0.0.1')
