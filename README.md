# Sockets-Programming
HTTP client and server by socket programming in Python interface that they can
transfer files to each other and the client can get a file from a real web server on the internet.

## The HTTP Client
### GET 
```
myclient host port_number GET filename
```
The basic client action should proceed as follows:

1.Connect to the server via a connection-orieted socket.

2.Submit a valid HTTP/1.0 GET request for the supplied URL.

#### Examples:

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
## The HTTP Server
Your server should take command line arguments specifying a port number.
```
myserver 5678
```
The basic server action should proceed as follows
1.Initialize the server.

2.Wait for a client connection on the port number specified by command line argument.

3.When a client connection is accepted, read the HTTP request.

4.Construct a valid HTTP response including status line, any headers you feel are appropriate, and, of course, the requested file in the response body.

5.For GET , if the server receives the "GET index.html HTTP/1.0" request, it sends out "200 OK" to the client, followed by the file index.html. If the requested file doesn't exist, the server sends out "404 Not Found" response to the client.

6.For PUT , if the server receives the "PUT test.txt" request, it will save the file as test.txt. If the received file from client is successfully created, the server sends back a "200 OK File Created" response to the client.

7.Close the client connection and loop back to wait for the next client connection to arrive.


