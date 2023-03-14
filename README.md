# SMTP-Protocol
<p align="justify">This is a Python script for sending an email using Simple Mail Transfer Protocol (SMTP) over a TCP connection. It uses the socket module for creating a socket and establishing a connection with the mail server specified in the code. The code includes comments for finding the appropriate mail server for sending the email.</p>

Once the connection is established, the script uses a series of SMTP commands, such as HELO, MAIL FROM, RCPT TO, DATA, and QUIT, to send the email. The script sends the email message with a subject line and message body. The email addresses for the sender and receiver are specified in the code.

The script also includes code for printing the server's response to each SMTP command sent. The script closes the socket connection after sending the email. Overall, this script demonstrates how to send a basic email using SMTP over a TCP connection in Python.
