import socket

def is_on_domain(dominio):
    try:
        direccion_ip = socket.gethostbyname(socket.gethostname())
        nombre_equipo = socket.getfqdn()
        if nombre_equipo.endswith(dominio):
            return True
        else:
            return False
    except:
        return False


