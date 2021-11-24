import socket
import stun


def port_check(port):
   host_ip = stun.get_ip_info()
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   result = sock.connect_ex((host_ip[1], port))  # 51413
   if result == 0:
       print('Порт ' + str(port) + ' открыт ' + host_ip[1])
   else:
       print('Порт ' + str(port) + ' закрыт ' + host_ip[1])
   sock.close()

