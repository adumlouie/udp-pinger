# UDP Pinger with No Delay and No Loss

# send the ping message using UDP
# print the response msesage from server if any was received
# calculate and print the RTT in milliseconds, of each packet if the server responds
# otherwise, print "request timed out"
# provide a sumAlice report at the end (of all pings) which includes
# - min RTT in milliseconds
# - max RTT in milliseconds
# - average RTT in milliseconds
# - percentage packet loss rate
# implement UDP client machine to send a packet of data to a remote machine, and have the remot machine send a packet of data to a remote machine, and have the remote machine return the data back to the client unchanged
#
# Ping message format
# firstname ping_number date_and_time

import time
import socket
from datetime import datetime

serverName = 'localhost'
serverPort = 12000

def udp_pinger(server_name, server_port, num_pings):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.settimeout(1)
    rtts = []
    lost_packets = 0

    for i in range(1, num_pings + 1):
        send_time = datetime.now().strftime("%a %b %H:%M:%S %Y")
        message = f"Adam {i} {send_time}"

        try:
            start_time = time.time()
            clientSocket.sendto(message.encode(), (serverName, serverPort))

            response, serverAddress = clientSocket.recvfrom(2048)
            end_time = time.time()

            # calculate rtt in milliseconds
            rtt = (end_time - start_time) * 1000
            rtts.append(rtt)

            print(f"Adam {i}: server reply: {response.decode()}, RTT = {rtt:.2f} ms  ")
        except socket.timeout:
            lost_packets += 1
            print(f"{message}: Request timed out")

    clientSocket.close()

    if rtts:
        print("\nUDP Summary")
        print(f"Min RTT: {min(rtts):.2f} ms")
        print(f"Max RTT: {max(rtts):.2f} ms")
        print(f"Avg RTT: {sum(rtts) / len(rtts):.2f} ms")
    else:
        print("All packets lost")

udp_pinger(serverName, serverPort, 10)
