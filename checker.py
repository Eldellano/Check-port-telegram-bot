import socket
import stun

get_ip_from_host = 1  # 0 - check for your static ip, 1 - check for host ip
static_ip = '192.168.0.1'


def get_host_ip():
    if get_ip_from_host == 1:
        return stun.get_ip_info()[1]  # get host ip (ip from net)
    else:
        return static_ip


def port_check(ip, port, name):  # via https://stackoverflow.com/a/19196218
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # second timeout
    result = sock.connect_ex((ip, int(port)))
    if result == 0:  # error 0 if success
        return 'Порт ' + str(port) + ' сервис ' + name + ' открыт ' + ip
    else:
        return 'Порт ' + str(port) + ' сервис ' + name + ' закрыт ' + ip
    sock.socket.shutdown()
    sock.close()
