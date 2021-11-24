import socket
import stun


# TODO: add time checkout
def get_host_ip():
    return stun.get_ip_info()  # get host ip (ip from net)


def port_check(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # 2 second timeout
    result = sock.connect_ex((ip, int(port)))
    print(result, ip)
    if result == 0:
        return ('Порт ' + str(port) + ' закрыт ' + ip)
    else:
        return ('Порт ' + str(port) + ' открыт ' + ip)
    sock.close()
