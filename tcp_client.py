import socket
import subprocess

target_host = '0.0.0.0'
target_port = 9997

bashCmd = "ifconfig"
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(output)

# receieve some data - this allows you to recieve as response which is 'ACK'
response = client.recv(4096)

# The above response will also be in packets so you need to decode it. 
print(response.decode())
client.close()