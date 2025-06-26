
import socket
import RPi.GPIO as GPIO
import time 

# socket.accept  # accept a connection from a client and we save the info as a socket and address # we wait at this line until we get a client 
# socket.bind # bind an address (server, port) to a socket 
# socket.listen   # we just enable listening 
# socket.recv  # receive data from a client through a socket # we wait at this line until we receive data


################################
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 18 as an output pin for the LED




################################
led_state = "off"

def web_page():
 html = """<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }
        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .button1 {
            background-color: #000000;
        }
    </style>
</head>
<body>
    <h2>Raspberry Pi Web Server</h2>
    <p>LED state: <strong>""" + led_state + """</strong></p>
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"led_on\"><button class="button">LED ON</button></a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#000000;"></i>
        <a href=\"led_off\"><button class="button button1">LED OFF</button></a>
    </p>
</body>
</html>"""
 return html



#ADDRESS = (server, port ) 
ADDRESS = ('', 8080)  # first par is just to allow any kind of network

def start_server():
    global led_state

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server.bind(ADDRESS)
    server.listen(1)
    while True:
        print("waiting for a client...")
        conn, addr = server.accept()
        #print(f"Connected to {addr}")
        print("IP address of client is:", addr)
        msg = conn.recv(1024).decode('utf-8') # max 1024 bytes messages can be sent, shorter messages are fine
        print("message was: ", msg)
        msg = msg.strip()
        if "GET /led_on" in msg:
           led_state = "on"
           GPIO.output(18, True)
        elif "GET /led_off" in msg:
           led_state = "off"
           GPIO.output(18,False)    
        print("led state is:", led_state)
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + web_page()
        conn.sendall(response.encode('utf-8')) # encode the response into bytes 


        conn.close()

start_server()
