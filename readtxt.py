import pyautogui

def readtxt(txt):
    try:
        with open(txt, "r") as document:
            datas = document.readlines()

        return datas
    except Exception as e:
            pyautogui.alert(f'Ha ocurrido un error: {str(e)}')


                


