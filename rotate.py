from checker import port_check, get_host_ip

ports = [8123, 51413, 9091, 9998, 22]  # add ports for check TODO: add sqlite database
ip = get_host_ip()[1]  # get host ip

def run_rotate():
    output = []
    for port in ports:
        output.append(port_check(ip, str(port)))
    return output


def show_ports():
    return ports