# Rasp_pi_LED
# Chat_server – Raspberry Pi LED Control via Web Interface

This project is a simple **TCP-based web server** built using **Python** and deployed on a **Raspberry Pi**. It allows a user to control an LED (turn it ON or OFF) through a browser-based interface.

The project uses the `socket` module to create a custom web server and `RPi.GPIO` to interact with the Raspberry Pi’s GPIO pins.

---

# Features

- Controls an LED connected to **GPIO pin 18**
- Accessible through any browser on **the same network**
- Simple HTML interface with ON/OFF buttons
- Real-time LED status display
- Uses raw socket programming (no Flask or Django)

---

# Tools Used

- Python 3
- Raspberry Pi GPIO library (`RPi.GPIO`)
- Raw TCP sockets
- HTML/CSS (for basic UI)
- SSH + VS Code for remote development on RPI

---

# How It Works

1. The Raspberry Pi runs a Python script that creates a TCP socket server on port `8080`.
2. When a client (e.g., browser) connects and sends an HTTP GET request (e.g., `/led_on` or `/led_off`), the server:
   - Parses the request
   - Sets GPIO pin 18 to HIGH or LOW
   - Sends back a dynamically generated HTML page with the updated LED status
3. The HTML page includes styled buttons to trigger further requests.

---

## Setup Instructions

### 1. Hardware

- Raspberry Pi (any model with GPIO support)
- One LED (can be Red or RGB)
- 330Ω resistor
- Breadboard + jumper wires
- Connect LED anode to GPIO 18 through resistor; cathode to GND

### 2. Software

- Clone this repo onto your Raspberry Pi or develop using **SSH with VS Code**
- Run the script:
  ```bash
  python3 chat_server.py

