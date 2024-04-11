import re
import pyautogui
from functools import reduce
import bit_transformation as bt

class information:
    def __init__(self, info) -> None:
        self.info = info
   
    def getLine(self,word):
        try:
            for line in self.info: #Buscamos la palabra
                if word in line:
                    return self.info.index(line)
            return ""
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido un error: {str(e)}')
        
    def getLineAndWord(self,word):
        try:
            wordLine = self.getLine(word)
            if wordLine != "":
                word = self.info[wordLine].split(":")
                word = word[1]
                word = word.strip()
                return word
            else:
                return ""
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido mun error: {str(e)}')

    def getMAC(self,findWord):
        try:
            for linea in self.info: #Buscamos la palabra
                if findWord in linea:
                    ethLine = self.info.index(linea) #Tomamos la linea Eth 
                    ethInfo = self.info[ethLine:] #Buscamos desde ahi
                    for linea in ethInfo: #Buscamos la linea de la MAC
                        if 'Direcci' in linea:
                            macLine = ethInfo.index(linea) 
                            macLine = ethInfo[macLine].split(":")
                            mac = macLine[1]
                            mac = mac.replace(" ","")
                            mac = mac.strip()
                            return mac
            return ""
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido mun error: {str(e)}')
    
    def getSharedFolder(self):
        try:
            sh_folder_line = self.getLine("las nuevas conexiones")
            foder_info = self.info[sh_folder_line:]
            expresion_regular = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\[a-zA-Z]+'
            ips = re.findall(expresion_regular,' '.join(foder_info))
            if ips == []:
                return "No posee carpetas compartidas"
            else:
                ips = ', '.join(ips)
                return ips
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido mun error: {str(e)}')
    
    def get_RAM_memory(self):
        try:
            memory_line = self.getLine("Memoria RAM:") #Buscamos la linea donde esta la data
            ssd_line = self.getLine("Espacio en Disco Duro:") #Buscamos donde finaliza la data
            memory_data = self.info[memory_line:ssd_line] #Creamos un arreglo con esos limites
            regular_expresion = r"\d+" #Creamos la expresion regular que siempre busque nuemeros
            memorys = re.findall(regular_expresion,' '.join(memory_data)) #Buscamos segun la RE
            if memorys == []:
                return "No reconocio el espacio de la memoria RAM"
            else:
                #Transformamos a int, sumamos las memorias y lo pasamos de Bytes a GB
                memorys = [int(memory) for memory in memorys]
                total_memory = reduce(lambda x, y: x+y,memorys)
                total_memory = bt.space_transformation(total_memory)
                return total_memory 
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido mun error: {str(e)}')

    def get_disk_memory(self):
        try:
            memory_line = self.getLine("Espacio en Disco Duro:") #Buscamos la linea donde esta la data
            proc_line = self.getLine("Modelo del Procesador") #Buscamos donde finaliza la data
            memory_data = self.info[memory_line:proc_line] #Creamos un arreglo con esos limites
            regular_expresion = r"\d+" #Creamos la expresion regular que siempre busque nuemeros
            memorys = re.findall(regular_expresion,' '.join(memory_data)) #Buscamos segun la RE
            if memorys == []:
                return "No reconicio el espacio del disco"
            else:
                #Transformamos a int, sumamos las memorias y lo pasamos de Bytes a GB
                memorys = [int(memory) for memory in memorys]
                total_memory = reduce(lambda x, y: x+y,memorys)
                total_memory = bt.space_transformation(total_memory)
                return total_memory 
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido mun error: {str(e)}')
    
    def get_processor_info(self):
        try:
            processor_line = self.getLine("Modelo del Procesador") #Buscamos la linea donde esta la data
            processor_data = self.info[processor_line:] #Creamos un arreglo con esos limites
            return processor_data[3]
        except Exception as e:
            pyautogui.alert(f'Ha ocurrido mun error: {str(e)}')


                         
        


