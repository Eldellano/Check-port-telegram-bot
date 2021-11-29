from checker import port_check, get_host_ip
import port_data

ip = get_host_ip()  # get host ip


def run_rotate():
    output = []
    for i in port_data.DataBase().port_get():
        port = i[0]
        name = i[1]
        output.append(port_check(ip, str(port), str(name)))
    return output
