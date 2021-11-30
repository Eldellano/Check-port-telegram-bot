from checker import port_check, get_host_ip
import port_data

ip = get_host_ip()  # get host ip


def run_rotate():
    output = []
    mass = port_data.DataBase().port_get()
    if len(mass) == 0:
        output.append('В БД нет портов для проверки!')
    else:
        for i in mass:
            port = i[0]
            name = i[1]
            output.append(port_check(ip, str(port), str(name)))
    return output
