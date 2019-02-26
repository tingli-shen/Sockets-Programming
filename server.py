import socket
# Standard socket stuff:
host = ''
port = 8084
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5) 
#check if file exists
def FileCheck(fn):
    try:
      open(fn, "r")
      return 1
    except IOError:
      return 0
# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print("Connection from: " + str(caddr))
    req = csock.recv(1024)  # get the request, 1kB max
    req=req.decode().split(" ")
    # Look in the first line of the request for a move command
    # A move command should be e.g. 'http://server/move?a=90'
    filename = req[4]
    # when server receives GET
    if req[3]=="GET":
        csock.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
        # send data per line
        if FileCheck(filename):
            f = open(filename, 'r')
            for l in f.readlines():
                print('Sent ', repr(l))
                csock.sendall(str.encode(""+l+"", 'iso-8859-1'))
                l = f.read(1024)
            f.close()
        # file not found
        else:
            csock.sendall(str.encode("404 Not Found",'iso-8859-1'))
    # when server receives PUT
    elif req[3]=="PUT":
        #write file to disk
        with open('received_file', 'wb') as f:
            csock.sendall(str.encode("200 OK File Created",'iso-8859-1'))
            while True:
                print('receiving data...')
                data = csock.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data) 
        f.close()
    csock.close()