from checker import port_check, get_host_ip

ports = [8123, 51413, 9091]  # add ports for check TODO: add sqlite database
ip = get_host_ip()[1]

def run_rotate():
    for port in ports:
        return port_check(port, ip)


def show_ports():
    return ports
