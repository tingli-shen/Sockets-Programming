# Sockets-Programming
HTTP client and server by socket programming in Python interface that they can
transfer files to each other and the client can get a file from a real web server on the internet.

## Client
### GET 
```
myclient host port_number GET filename
```
The basic client action should proceed as follows:

1.Connect to the server via a connection-orieted socket.

2.Submit a valid HTTP/1.0 GET request for the supplied URL.

Examples:

1.Use it to get a file of your choosing from a "real" web server on the internet.
```
myclient www.cnn.com 80 GET index.html
```
2.Use it to get a file from your own server program.
```
myclient pc1.cs.uml.edu 5678 GET index.html
```
### PUT
```
myclient host port_number PUT filename
```
The basic client action should proceed as follows:

1.Connect to the server via a connection-orieted socket.

2.Submit a PUT request for the supplied file

3.Send the file to the server.

4.Wait for server's reply.



