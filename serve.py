from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

def stress_cpu():
    # Run the stress_cpu.py script in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])

@app.route("/", methods=["POST", "GET"])
def handle_requests():
    if request.method == "POST":
        # Handle POST request to stress the CPU
        stress_cpu()
        return str("CPU stress initiated")
    elif request.method == "GET":
        # Handle GET request to return private IP address
        ip_address = socket.gethostbyname(socket.gethostname())
        return str("private_ip" + str(ip_address))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
