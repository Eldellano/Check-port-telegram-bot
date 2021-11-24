import socket
import stun

def get_host_ip():
    return stun.get_ip_info()  # get host ip (ip from net)

def port_check(port, ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))  # 51413
    if result == 0:
        return ('Порт ' + str(port) + ' открыт ' + ip)
    else:
        return ('Порт ' + str(port) + ' закрыт ' + ip)
    sock.close()

