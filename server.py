import socket

host = ''
port = 2304

storedValue = "Hello World"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)

    print("Socket bind complete.")

    return s

def setupConnection():
    s.listen(1) # Only one connection at a time
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    # Send/Recieve
    while True:
        # Recieve data
        data = conn.recv(1024) 
        data = data.decode('utf-8') # Python 3 needs to decode the data
        # Split data to separate the command 
        dataMessage = data.split(' ', 1)
        command = dataMessage[0] # command is the first segment
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Client Exit")
            break
        elif command == 'KILL':
            print("Server shutdown")
            s.close()
            break
        else:
            reply = 'Unknown Command'

        # Send Reply to Client
        conn.sendall(str.encode(reply))
        print("Data has been sent")

    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break