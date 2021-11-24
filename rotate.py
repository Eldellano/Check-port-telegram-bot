from checker import port_check


ports = [8123, 51413, 9091]

def run_rotate():
    for port in ports:
        port_check(port)

def show_ports():
    for port in ports:
        return port