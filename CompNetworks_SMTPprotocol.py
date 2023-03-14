from socket import *
import base64

# Choose a mail server (e.g. NYU. mail server) and call it mailserver
# Code Start 
# dig MX nyu.edu 
# (Didn't work) required authentication
# Resolve-DnsName smtp.cs.nyu.edu
# Resolve-DnsName smtp.gmail.com
# Resolve-DnsName mail.smtp2go.com
# Code End

mailserver = 'mxa-00256a01.gslb.pphosted.com'
serverPort = 25

# Create socket and establish TCP connection with mailserver
# Code Start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
# Code End
tcpResponse = clientSocket.recv(1024).decode()
print(tcpResponse)

# Send HELO command to begin SMTP handshake.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
heloCommandResponse = clientSocket.recv(1024).decode()
print(heloCommandResponse)

# Send MAIL FROM command and print response.
# Code Start
mailFrom = 'MAIL FROM: <kezzat000@gmail.com>\r\n'
clientSocket.send(mailFrom.encode())
mailFromResponse = clientSocket.recv(1024).decode()
print("Server Response: " + mailFromResponse)
# Code End

# Send RCPT TO command and print server response.
# Code Start
rcptTo = 'RCPT TO: <ked9342@nyu.edu>\r\n'
clientSocket.send(rcptTo.encode())
rcptToResponse = clientSocket.recv(1024).decode()
print("Server Response: " + rcptToResponse)
# Code End

# Send DATA command and print server response.
# Code Start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
dataCommandResponse = clientSocket.recv(1024).decode()
print("Server Response: " + dataCommandResponse)
# Code End

# Send email data.
# Code Start
emailData = 'Subject: Test Mail \r\n\r\n This is a test email for the second Computer Networks assignment.'
clientSocket.send(emailData.encode())
# Code End

# Send message to close email message.
# Code Start
endOfMail = '\r\n.\r\n'
clientSocket.send(endOfMail.encode())
messageResponse = clientSocket.recv(1024).decode()
print("Server Response: " + messageResponse)
# Code End

# Send QUIT command and get server response.
# Code Start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
quitCommandResponse = clientSocket.recv(1024).decode()
print("Server Response: " + quitCommandResponse)
# Code End

clientSocket.close()
