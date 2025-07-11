# Spring4Shell Firewall Rule

This project is a simulation task from [Forage](https://www.theforage.com) for the Telstra Cyber Virtual Experience Program. It demonstrates how to build a simple Python firewall server that detects and blocks malicious HTTP requests, specifically those exploiting the Spring4Shell vulnerability pattern.

---

## Overview

You will find two main scripts in this repository:

- **firewall_server.py**  
  A Python HTTP server that inspects incoming requests and blocks those containing a known malicious pattern.

- **test_requests.py**  
  A test script that sends simulated malicious requests to the server to verify the firewall rule works as intended.

---

## Requirements

- Python 3.x

---

## How to Run

1. **Start the Firewall Server**

   Open a terminal and run:
   ```sh
   python firewall_server.py
   ```

   You should see output indicating the server is running on `localhost:8000`.

2. **Test the Firewall Rule**

   In a new terminal window, run:
   ```sh
   python test_requests.py
   ```

   This will send 5 POST requests containing a suspicious payload to the server.  
   If the firewall rule is working, the server will block these requests and print "Blocking request" in the console.

---

## How it Works

- The server inspects the body of each POST request.
- If the request contains the string  
  `class.module.classLoader.resources.context.parent.pipeline.first.pattern`  
  it is considered malicious and is blocked with a `403 Forbidden` response.
- All other requests receive a `200 OK` response.

---

## Learning Outcomes

- Understand how to use Python's built-in `http.server` module.
- Learn basic HTTP request handling and response codes.
- Practice writing simple security rules to detect and block malicious input.

---

