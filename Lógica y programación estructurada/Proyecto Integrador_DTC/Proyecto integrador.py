# Daniel Trejo Camacho | Universidad del Valle de México | Ciencia de Datos
# Proyecto Integrador

# Se importan las librerías necesarias para crear un menú interactivo.
None

# Se define el catálogo de información
datos_de_estudiantes = {}

# Ejemplo del cómo deben lucir los datos
datos_de_estudiantes.update({271033: ["DANIEL", "TREJO", "CAMACHO", "CIENCIA DE DATOS", "DTREJO21@ALUMNOS.UAQ.MX", 4271820557]})
datos_de_estudiantes.update({271034: ["MARIANA", "TREJO", "CAMACHO", "BACHILLERATO", "MTREJO21@ALUMNOS.UAQ.MX", 4425592177]})

# Se consultan los datos del estudiante a través de la matricula.
print(datos_de_estudiantes[271033])




### Se definen las funciones que cumplen con la acción seleccionada

# ALTA DE ESTUDIANTE
def alta():
    # Esta función permite que los usarios den de alta su matricula en el sistema.
    matricula = int(input("Ingrese la matrícula del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    a_paterno = input("Ingrese el apellido paterno del estudiante: ")
    a_materno = input("Ingrese el apellido materno del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    correo = input("Ingrese el correo electrónico del estudiante: ")
    teléfono = input("Ingrese el teléfono del estudiante: ")
    # La siguiente parte del código permite actualizar el catálogo con los datos del usuario.
    datos_de_estudiantes.update({matricula: [nombre.upper(), a_paterno.upper(), a_materno.upper(), carrera.upper(), correo.upper(), teléfono]})

# MODIFICACIÓN DE DATOS DEL ESTUDIANTE
def modificación():
    # Esta función permite a los usuarios hacer una modificación de sus datos
    matricula = int(input("Ingrese su matrícula: "))
    número = int(input("Ingrese el campo a modificar (1. Nombre 2. Apellido paterno 3. Apellido materno 4. Carrera 5. Correo 6. Teléfono): "))
    if matricula in datos_de_estudiantes:
    # Los siguientes condicionales permiten que el campo seleccionado sea modificado con el valor correspondiente
        if número == 1:
            datos_de_estudiantes[matricula][0] = str(input("Ingrese el nombre correcto: ").upper())
        elif número == 2:
            datos_de_estudiantes[matricula][1] = str(input("Ingrese el apellido paterno correcto: ").upper())
        elif número == 3:
            datos_de_estudiantes[matricula][2] = str(input("Ingrese el apellido materno correcto: ").upper())
        elif número == 4:
            datos_de_estudiantes[matricula][3] = str(input("Ingrese la carrera correcta: ").upper())
        elif número == 5:
            datos_de_estudiantes[matricula][4] = str(input("Ingrese el correo electrónico correcto: ").upper())
        elif número == 6:
            datos_de_estudiantes[matricula][5] = str(input("Ingrese el número de teléfono correcto: "))
        else:
            print("La opción seleccionada no existe.")
    else:
        print("La matricula no se encuentra registrada.")

# BÚSQUEDA DE DATOS
def búsqueda():
    # Esta función permite al usuario consultar su información de estudiante con su matricula.
    matricula = int(input("Ingrese su matricula: "))
    # El condicional comprueba si la matricula ya ha sido dada de alta
    if matricula in datos_de_estudiantes:
        print(datos_de_estudiantes[matricula])
    else:
        print("La matricula no se encuentra registrada.")

# DARSE DE BAJA 
def baja():
    # Este código permite a los usuarios darse de baja.
    matricula = int(input("Ingrese su matricula: "))
    # El condicional comprueba si la matricula se encuentra en el diccionario
    if matricula in datos_de_estudiantes:
        datos_de_estudiantes.pop(matricula)
    else:
        print("La matricula no se encuentra registrada.")

# SALIR DEL MENÚ Y COMPROBAR QUE LOS CAMBIOS SE HAN VISTO REFLEJADOS
def mostrar_datos():
    # La finalidad de esta función es comprobar que los datos se vean reflejados y corresponde a la opción "salir" del menú.
    print("Datos de estudiantes:")
    print(datos_de_estudiantes)




### Se define el funcionamineto del menú
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('La opción seleccionada no existe.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menú(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


### Se define la interfaz del menú
def menú():
    opciones = {'1': ('Alta de estudiante', alta),
            '2': ('Modificación de datos', modificación),
            '3': ('Consulta de datos', búsqueda),
            '4': ('Baja de estudiante', baja),
            '5': ('Salir', mostrar_datos)}
    
    generar_menú(opciones, '5')

menú()