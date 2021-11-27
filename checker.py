import socket
import stun

# TODO: add time checkout
def get_host_ip():
    return stun.get_ip_info()  # get host ip (ip from net)


def port_check(ip, port):  # via https://stackoverflow.com/a/19196218
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # second timeout
    result = sock.connect_ex((ip, int(port)))
    if result == 0:  # error 0 if success
        return ('Порт ' + str(port) + ' открыт ' + ip)
    else:
        return ('Порт ' + str(port) + ' закрыт ' + ip)
    sock.socket.shutdown()
    sock.close()