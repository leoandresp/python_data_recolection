from Information import information
import wmi
import subprocess
import pyautogui

class hostname:
    def __init__(self, info: information):
        self.info = info

    def create_name(self, mac):
        try:
            # Asignamos una variable por parte del nombre
            equip = self.info.getLineAndWord("Equipo:")
            role = self.info.getLineAndWord("Funciones:")
            ubication = self.info.getLineAndWord("Sede:")
            floor = self.info.getLineAndWord("Piso:")
            city = self.info.getLineAndWord("Ciudad:")
            wallet = self.info.getLineAndWord("Cartera:")
            departament = self.info.getLineAndWord("Departamento:")

            equip_mapping = {"Laptop": "LP", "PC de escritorio": "PC"}
            equip = equip_mapping.get(equip)
            role_mapping = {"Operaciones": "1", "Administrativo": "2"}
            role = role_mapping.get(role)
            ubication_mapping = {"Independencia": "IN", "San Isidro": "SI",
                                 "Provincia": "PR", "Remoto": "RE"}
            ubication = ubication_mapping.get(ubication)
            city_ab = city[:2].upper()
            wallet_ab = wallet[:2].upper()
            depart_ab = departament[:2].upper()
            mac = mac.replace("-", "")

            if (ubication == "IN" or ubication == "SI"):
                name = f'{equip}{role}{ubication}P{floor}-{mac}'
                return name
            elif (ubication == "PR" or ubication == "RE"):
                name = f'{equip}{role}{depart_ab}{city_ab}{wallet_ab}-{mac}'
                return name
        except Exception as e:
            pyautogui.alert(f'Ocurrió un error: {str(e)}',"Error")
            
    def change_hostname(self,new_hostname):
        try:
            c = wmi.WMI()

            for system in c.Win32_ComputerSystem():
                system.Rename(new_hostname,"","")
        except Exception as e:
            pyautogui.alert(f'Ocurrió un error: {str(e)}',"Error")

    def change_admin_password(self, domain:bool):
        
        if domain == False:
            command = f"net user administrator 123456789 "
            subprocess.run(command, shell=True, check=True)




    











