import winreg
def get_installed_programs():
    installed_programs = []
    
    # Rutas adicionales donde buscar programas instalados
    additional_paths = [
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall",
        r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
        r"Software\Microsoft\Windows\CurrentVersion\App Paths",
        r"Software\Classes\Installer\Products",
        r"Software\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products"
        # Agrega aquí más rutas según tus necesidades
    ]
    
    for path in additional_paths:
        try:
            uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            num_subkeys = winreg.QueryInfoKey(uninstall_key)[0]
            
            for i in range(num_subkeys):
                program_key = winreg.EnumKey(uninstall_key, i)
                program_subkey = winreg.OpenKey(uninstall_key, program_key)
                try:
                    display_name = winreg.QueryValueEx(program_subkey, "DisplayName")[0]
                    installed_programs.append(display_name)
                except OSError:
                    pass

        except FileNotFoundError:
            pass

    installed_programs = sorted(installed_programs)
    return '\n'.join(installed_programs)


