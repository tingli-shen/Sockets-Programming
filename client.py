import socket                   # Import socket module
import sys 
s = socket.socket()             # Create a socket object
#command line options
command=["myclient www.bbc.com 80 GET index.html"
         ,"myclient localhost 8084 GET index.html","myclient localhost 8084 PUT index.html"]
cmd_num=1 #command final choice
cmd=command[cmd_num].split(" ") #split command line by space
command=command[cmd_num]
host = cmd[1]  #Ip address that the TCPServer  is there
port = int(cmd[2]) # Reserve a port for your service every new transfer wants a new port or you must wait.
# when interacting with local machine
if cmd[1]=='localhost':
    s.connect((host, port))
    s.send(command.encode())
    #send command line to server so that server will know how to interact with the client
    # HTTP method GET
    if cmd[3]=="GET": 
        #write file to disk
        with open('received_file', 'wb') as f: 
            while True:
                print('receiving data...')
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data) 
        f.close()
    # HTTP method PUT
    elif cmd[3]=="PUT":
        filename=cmd[4]
        f = open(filename, 'r')
        # send data per line
        for l in f.readlines():
            print('Sent ', repr(l))
            s.sendall(str.encode(""+l+"", 'iso-8859-1'))
            l = f.read(1024)
        f.close()
        # read "200 OK File Created"
        data = s.recv(1024)
        print(data.decode())
    s.close()
    print('connection closed')
# when interacting with "real" web server on the internet
else:
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print ("Socket successfully created")
    except socket.error as err: 
        print ("socket creation failed with error %s" %(err))
    try: 
        host_ip = socket.gethostbyname(cmd[1]) 
    except socket.gaierror: 
      
        # this means could not resolve the host 
        print ("there was an error resolving the host")
        sys.exit()                 
    s.connect((cmd[1] , int(cmd[2])))
    # cmd ="GET / HTTP/1.0/index.html\r\nHost: www.bbc.com\r\n\r\n"
    cmd=cmd[3]+" / HTTP/1.0/"+cmd[4]+"\r\n"+"Host: "+cmd[1]+"\r\n\r\n"
    s.sendall(cmd.encode())
    #s.sendall("Host: 127.0.0\r\n\r\n")
    print (s.recv(4094))
    s.close


    