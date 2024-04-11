from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import sys
import pyautogui


def set_googleSheets(info):
    
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # Obtiene la ruta del archivo .exe
    ruta_exe = os.path.abspath(sys.argv[0])

    # Obtiene el directorio donde se encuentra el archivo .exe
    directorio_actual = os.path.dirname(ruta_exe)

    # Construye la ruta completa del archivo key.json
    ruta_key = os.path.join(directorio_actual, 'key.json')
    KEY = ruta_key
    SPREADSHEET_ID = '117nGNJUADJKlB8sr3tCAkCvSjvN3kGHB0uhzyAxH0yw'

    try:
        creds = None
        creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

        
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        # Debe ser una matriz por eso el doble [[]]
        values = [info]
        # Llamamos a la API
        result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                        range='A1:W1',
                                        valueInputOption='USER_ENTERED',
                                        body={'values': values}).execute()

        if 'updates' in result and 'updatedCells' in result['updates']:
            updated_cells = result['updates']['updatedCells']
            return pyautogui.alert(f"Datos enviados de forma exitosa", "Información")
            
        else:
            raise Exception("No se pudo obtener información sobre las celdas actualizadas")

    except FileNotFoundError as e:
        print("Error al leer el archivo de clave:", str(e))
        pyautogui.alert(f'Error al leer el archivo de clave:{str(e)}',"Error")

    except Exception as e:
        pyautogui.alert(f'Ocurrió un error al insertar los datos en Google Sheets:{str(e)}',"Error")
        