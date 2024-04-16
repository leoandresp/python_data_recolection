from readtxt import readtxt
from write import set_googleSheets
from programInstall import get_installed_programs
from Information import information
from license import isLicensed
from domain import is_on_domain
from hostname import hostname as h
import datetime
import pyautogui

try:
    info = readtxt("respuestas.txt")
    licensetext = readtxt("licencia.txt")
    if not info or not licensetext:
        raise FileNotFoundError("No se pudo leer uno o ambos archivos")

    # Eliminamos los espacios nulos por el formato errado
    licensetext = [i.replace('\x00', '') for i in licensetext]
    info = [i.replace('\x00', '') for i in info]
    generalInformation = information(info)
    licenseInfo = information(licensetext)

    #Añadimos el dia y hora de ejecucion
    finalData = []
    current_date = datetime.datetime.today().isoformat()
    finalData.append(current_date)
    # Añadimos los primeros 5 elementos
    
    firstElements = ["Nombre y Apellido", "DNI", "Telefono", "Funciones", "Equipo", "Proveedor","etiqueta_proveedor"]
    for i in firstElements:
        data = generalInformation.getLineAndWord(i)
        finalData.append(data)

    #Agregamos la ip del Equipo
    ip_information = generalInformation.getIP()
    finalData.append(ip_information)

    # Buscamos los datos de Red
    redLineInit = generalInformation.getLine("Info de Red")
    redInfo = info[redLineInit:]
    redInformation = information(redInfo)
    mac_lan = redInformation.getMAC("Ethernet")
    mac_wifi = redInformation.getMAC("mbrica Wi-Fi")

    # los añadimos a la lista
    finalData.append(mac_lan)
    finalData.append(mac_wifi)

    # Añadimos los siguientes Elementos
    secondElements = ["Propiedad", "Sede", "Piso", "Cartera", "Jefe", "Departamento", "Ciudad",
                      "Nombre del sistema operativo"]
    for i in secondElements:
        data = generalInformation.getLineAndWord(i)
        finalData.append(data)

    # Verificamos la licencia
    lisc = isLicensed(licensetext)
    finalData.append(lisc)

    # Añadimos los programas
    programs = get_installed_programs()
    finalData.append(programs)

    #Añadimos el codigo de Anydesk
    anydeskID = generalInformation.getLineAndWord("La ID de AnyDesk es")
    finalData.append(anydeskID)  # Anydesk

    # Obtenemos las carpetas compartidas
    shared_folders = generalInformation.getSharedFolder()
    finalData.append(shared_folders)

    # Validamos si esta en el dominio
    domain = is_on_domain("domkobsa.local")
    finalData.append(domain)

    # Agregamos el hostname Actual
    current_hostname = generalInformation.getLineAndWord("Nombre de host")
    finalData.append(current_hostname)

    # Agregamos el Nuevo Hostname
    this_pc = h(generalInformation)
    new_hostname = this_pc.create_name(mac_lan)
    finalData.append(new_hostname)
    
    #this_pc.change_hostname(new_hostname)
    #this_pc.change_admin_password(domain)
    
    #Agregamos el espacio en disco
    disk = generalInformation.get_disk_memory()
    finalData.append(disk)

    #Agregamos el espacio en memoria RAM
    ram = generalInformation.get_RAM_memory()
    finalData.append(ram)

    #Agregamos el modelo del procesador
    processor = generalInformation.get_processor_info()
    finalData.append(processor)

    # Agregamos el Fabricante
    manofacturer = generalInformation.getLineAndWord("Modelo el sistema")
    finalData.append(manofacturer)

    set_googleSheets(finalData)

except FileNotFoundError as e:
    pyautogui.alert(f'Error al leer archivos: Consulte con el administrador del sistema',"Error")

except Exception as e:
    pyautogui.alert(f'Ocurrió un error: Consulte con el administrador del sistema',"Error")
