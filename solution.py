from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')
    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM: <mail@mail.com>\r\n'
    clientSocket.send(mailfromCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv[:3] != '250':
        print('mail from 250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO: <myemail@gmail.com>\r\n'
    clientSocket.send(rcpttoCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('rcpt to 250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'Data'
    print(dataCommand)
    clientSocket.send(dataCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('data 250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    msg = "\r\n My Message"
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    endmsg = "\r\n.\r\n"
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
    print(quitCommand)
    clientSocket.send(quitCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('quit 250 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
