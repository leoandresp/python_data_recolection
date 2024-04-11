from Information import information
import re
import pyautogui

def isLicensed(info):
    try:
        patron = r'[A-HJ-NP-Y0-9]{5}-[A-HJ-NP-Y0-9]{5}-[A-HJ-NP-Y0-9]{5}-[A-HJ-NP-Y0-9]{5}-[A-HJ-NP-Y0-9]{5}'
        for cadena in info:
            if re.search(patron, cadena):
                return "SI"  # Si se encuentra una licencia válida, se devuelve "SI"
        return "NO"  # Si no se encuentra ninguna licencia válida, se devuelve "NO"
    except Exception as e:
            pyautogui.alert(f'Ha ocurrido un error: {str(e)}')
