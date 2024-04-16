@echo off
chcp 65001
setlocal enabledelayedexpansion

REM Eliminar archivo existente
if exist respuestas.txt (
    del respuestas.txt
)


echo Recopilando información del sistema operativo...

wmic path softwarelicensingservice get OA3xOriginalProductKey > licencia.txt
systeminfo | findstr /i "Nombre del sistema operativo" >> respuestas.txt

REM Pregunta A
set /p nombres_apellidos="Ingrese sus nombres y apellidos: "
echo Nombre y Apellido:%nombres_apellidos% >> respuestas.txt

REM Pregunta B
set /p dni="Ingrese su DNI: "
echo DNI:%dni% >> respuestas.txt

REM Pregunta C
set /p telefono="Ingrese su telefono: "
echo Telefono:%telefono% >> respuestas.txt

REM Pregunta D: Tipo de funciones
:pregunta_d
echo D. Que tipo de funciones realiza: (Ingrese el numero de la opcion):
echo 1. Operaciones
echo 2. Administrativo
set /p funciones="Respuesta: "
if "%funciones%"=="1" (
    set funciones_text="Operaciones"
    echo Funciones:Operaciones >> respuestas.txt
) else if "%funciones%"=="2" (
    set funciones_text="Administrativo"
    echo Funciones:Administrativo >> respuestas.txt
) else (
    echo Opcion invalida. Por favor, ingrese un numero valido de opcion.
    goto pregunta_d
)

REM Pregunta E: Equipo utilizado
:pregunta_e
echo E. Para sus labores utiliza: (Ingrese el numero de la opcion):
echo 1. Laptop
echo 2. PC de escritorio
set /p equipo="Respuesta: "
if "%equipo%"=="1" (
    set equipo_text="Laptop"
    echo Equipo:Laptop >> respuestas.txt
) else if "%equipo%"=="2" (
    set equipo_text="PC de escritorio"
    echo Equipo:PC de escritorio >> respuestas.txt
) else (
    echo Opcion invalida. Por favor, ingrese un numero valido de opcion.
    goto pregunta_e
)

REM Pregunta F: Propiedad del equipo
:pregunta_f
echo F. El equipo con el que trabaja es propiedad de Hildmarc o personal: (Ingrese el numero de la opcion):
echo 1. Hildmarc
echo 2. Personal
set /p propiedad="Respuesta: "
if "%propiedad%"=="1" (
    set propiedad_text="Hildmarc"
    echo Propiedad:Hildmarc >> respuestas.txt
    goto pregunta_g
) else if "%propiedad%"=="2" (
    set propiedad_text="Personal"
    echo Propiedad:Personal >> respuestas.txt
    goto pregunta_i
) else (
    echo Opcion invalida. Por favor, ingrese un numero valido de opcion.
    goto pregunta_f
)

REM Pregunta G: Proveedor
:pregunta_g
echo H. Indique el Proveedor (Ingrese el número de la opción):
echo 1. HTG
echo 2. FALCON
echo 3. ITELCORE
echo 4. FT VENDOR
echo 5. KOBSA (Sin Stiker)
set /p proveedor="Respuesta: "
if "%proveedor%"=="1" (
    set ubicacion_text="HTG"
    echo Proveedor:HTG >> respuestas.txt
) else if "%proveedor%"=="2" (
    set ubicacion_text="FALCON"
    echo Proveedor:FALCON >> respuestas.txt
) else if "%proveedor%"=="3" (
    set ubicacion_text="ITELCORE"
    echo Proveedor:ITELCORE >> respuestas.txt
) else if "%proveedor%"=="4" (
    set ubicacion_text="FT VENDOR"
    echo Proveedor:FT VENDOR >> respuestas.txt
) else if "%proveedor%"=="5" (
    set ubicacion_text="KOBSA (Sin Stiker)"
    echo Proveedor:KOBSA >> respuestas.txt
) else (
    echo Opción inválida. Por favor, ingrese un número válido de opción.
    goto pregunta_g
)


REM Pregunta H
:pregunta_h
set /p etiqueta_proveedor="Ingrese el código de la etiqueta del proveedor: "
echo etiqueta_proveedor:%etiqueta_proveedor% >> respuestas.txt

REM Pregunta I: Ubicacion
:pregunta_i
echo H. Escoja la sede/ubicacion donde realiza sus actividades (Ingrese el numero de la opcion):
echo 1. Independencia
echo 2. San Isidro
echo 3. Provincia
echo 4. Remoto
set /p ubicacion="Respuesta: "
if "%ubicacion%"=="1" (
    set ubicacion_text="Independencia"
    echo Sede:Independencia >> respuestas.txt
    goto pregunta_independencia
) else if "%ubicacion%"=="2" (
    set ubicacion_text="San Isidro"
    echo Sede:San Isidro >> respuestas.txt
    goto pregunta_isidro
) else if "%ubicacion%"=="3" (
    set ubicacion_text="Provincia"
    echo Sede:Provincia >> respuestas.txt
    goto pregunta_provincia
) else if "%ubicacion%"=="4" (
    set ubicacion_text="Remoto"
    echo Sede:Remoto >> respuestas.txt
    goto pregunta_cartera
) else (
    echo Opcion invalida. Por favor, ingrese un numero valido de opcion.
    goto pregunta_i
)

REM Pregunta del Independencia - Comun para opciones 1 y 2
:pregunta_independencia
set /p piso="Ingrese el piso en el que labora: "
echo Piso:%piso% >> respuestas.txt
set /p cartera="Ingrese la cartera en la que labora: "
echo Cartera:%cartera% >> respuestas.txt
set /p jefe="Ingrese el nombre de su jefe inmediato: "
echo Jefe:%jefe% >> respuestas.txt
goto fin

REM Pregunta de Isidro
:pregunta_isidro
set /p piso="Ingrese el piso en el que labora: "
echo Piso:%piso% >> respuestas.txt
goto fin

REM Preguntas adicionales para opcion 3 (Provincia)
:pregunta_provincia
set /p cartera="Ingrese la cartera en la que labora: "
echo Cartera:%cartera% >> respuestas.txt
set /p jefe="Ingrese el nombre de su jefe inmediato: "
echo Jefe:%jefe% >> respuestas.txt
set /p departamento="Ingrese el departamento donde labora: "
echo Departamento:%departamento% >> respuestas.txt
set /p ciudad="Ingrese la ciudad donde labora: "
echo Ciudad:%ciudad% >> respuestas.txt
goto fin

REM Preguntas adicionales para opcion 4 (Remoto)
:pregunta_cartera
set /p cartera="Ingrese la cartera en la que labora: "
echo Cartera:%cartera% >> respuestas.txt
set /p jefe="Ingrese el nombre de su jefe inmediato: "
echo Jefe:%jefe% >> respuestas.txt
set /p departamento="Ingrese el departamento donde labora: "
echo Departamento:%departamento% >> respuestas.txt
set /p ciudad="Ingrese la ciudad donde labora: "
echo Ciudad:%ciudad% >> respuestas.txt
goto fin




:fin

echo Info de Red: >> respuestas.txt
ipconfig /all >> respuestas.txt
net use >> respuestas.txt
for /f "delims=" %%i in ('"C:\Program Files (x86)\AnyDesk\AnyDesk.exe" --get-id') do set ID=%%i
echo La ID de AnyDesk es:%ID% >> respuestas.txt
echo Memoria RAM: >> respuestas.txt
wmic memorychip get capacity /format:list >> respuestas.txt
echo Espacio en Disco Duro: >> respuestas.txt
wmic logicaldisk where "DeviceID='C:'" get Size >> respuestas.txt
echo Modelo del Procesador >> respuestas.txt
wmic cpu get name >> respuestas.txt



set "powershell_script="
set "path=%~dp0nadmin.ps1"

set "powershell_script=$powershell_script ^
$path"

powershell.exe -ExecutionPolicy Bypass -Command "%powershell_script%"

exit