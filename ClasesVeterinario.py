import random
import ClasseMascota 
import ClassePropietario
import pandas as pd
from tabulate import tabulate
import os

""" NEON_PINK = (28, 160, 47)   # Neón Rosa
NEON_GREEN = (57, 255, 20)    # Neón Verde
NEON_YELLOW = (255, 255, 51)  # Neón Amarillo
NEON_ORANGE = (255, 95, 0)    # Neón Naranja
NEON_BLUE = (0, 255, 255)     # Neón Azul
NEON_PURPLE = (155, 89, 182) """

NEON_PINK = "\033[38;5;Magenta"
NEON_GREEN = "\033[38;5;82m"
NEON_YELLOW = "\033[38;5;11m"
NEON_ORANGE = "\033[38;5;202m"
NEON_BLUE = "\033[38;5;14m"
NEON_PURPLE = "\033[38;5;129m"
RESET = "\033[0m" 

import bsd
from datetime import datetime # importamos la libreria datetime para la hora
class Veterinario:#Clase Veterinario
    def __init__(self,id = "",nombres = "",apellidos ="",direccion ="",telefono ="",tarjeta=""):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.tarjeta = tarjeta
        
    def registrar_veterinario(self):
        diccionario_veterinario = {
            "Id":self.id,
            "Nombres":self.nombres,
            "Apellidos":self.apellidos,
            "Direccion":self.direccion,
            "Telefono":self.telefono,
            "Tarjeta profesional":[self.tarjeta],
            "Mascotas":[]
        }
        bsd.ides_veterinarios.append(self.id)#Se guardardo el id del veterinario a la lista respectiva
        bsd.lista_veterinarios.append(diccionario_veterinario) #Se subio a la lista de veterinarios
        
    def registrar_mascota(self):
        print("\nINGRESAR DATOS PROPIETARIO\n")
        while True:
            id = input("ingresa el id del propietario: ")
            if len(id) != 10: #se hace control de excepciones
                print("Error: el id debe contener 10 digitos")
            else:
                break
        while True:
            nombre=input("ingresa el nombre del propietario: ")
            if nombre.isnumeric() == True:
                print("Error: no puedes ingresar numeros")
            else:
                break
        while True:
            apellido = input("ingresa el apellido del propietario: ")
            if apellido.isnumeric() == True:
                print("Error: no puedes ingresar numeros")
            else:
                break
        direccion = input("ingresa la direccion del propietario: ")
        while True:
            telefono = input("ingresa el telefono del propietario: ")
            if len(telefono) != 10:
                print("Error: el telefono debe tener 10 numeros")
            else:
                break
        while True:
            u = "@."
            correo = input("ingresa el correo: ")
            if u not in correo:
                print("ERROR: ingresa un correo valido")
            else:
                break
        if id in bsd.ides_propietarios: # verificar si el propietario existe
            print("Se te agregara una mascota, ingresa los datos...\n ")
            for i in bsd.lista_propietario: # recorrer la lista de todos los propietarios
                if i["Id"]== id: # si el id del propietario coinciden 
                    # solicitar los datos de la nueva mascota
                    print("\nINGRESA LOS DATOS DE LA MASCOTA")
                    nombre=input("Nombre:").lower()
                    especie=input("Especie: ")
                    #No dejar pasar si estos dos datos ya existen
                    color=input("Color: ")
                    while True:
                        ingresar_raza=input("desea ingresae raza (si/no): ").lower()
                        if ingresar_raza != "si" and ingresar_raza !="no":
                            print("Ingresa si/no")
                        else:
                            break
                    if ingresar_raza == "si":
                        raza= input("Ingresa la Raza: ")
                    else:
                        pass
                    id_mascota=id_mascota_random() # generar id random para la mascota
                    i["Mascotas"].append(id_mascota) # Agregar el id de la nueva mascota al veterianario
                    mascota=ClasseMascota.Mascota(id_mascota,nombre,color,especie, raza)  # llamar el modulo, la clase, y pasar los atributos
                    mascota.registrar_mascota()# registrar mascota, llamando el metodo registrar_mascota
        else:
            #se registran como usuaios nuevo, con mascota nueva
            propietario = ClassePropietario.Propietario(id,nombre,apellido,direccion,telefono,correo)
            #Solicitar datos de la mascota 
            print("\nINGRESA LOS DATOS DE LA MASCOTA\n")
            nombre=input("Nombre:").lower()
            especie=input("Especie: ")
            #No dejar pasar si estos dos datos ya existen
            color=input("Color: ")
            while True:
                ingresar_raza=input("desea ingresae raza (si/no): ").lower()
                if ingresar_raza != "si" and ingresar_raza !="no":
                    print("Ingresa si/no")
                else:
                    break
            if ingresar_raza == "si":
                raza= input("Ingresa la Raza: ")
            else:
                pass
            id_mascota=id_mascota_random()
            mascota = ClasseMascota.Mascota(id_mascota,nombre,color,especie, raza)
            propietario.mascota=mascota.id
            #Guardar datos de la mascota y el propietario en la lista 
            propietario.registrar_propietario()
            mascota.registrar_mascota()

    def registrar_propietario(self): # metodo registrar propietario
        print("\nINGRESAR DATOS MASCOTA\n")
        while True:
                nombre=input("Nombre:").lower()
                if nombre.isalpha()==False:
                    print("Error: solo str")
                else:
                    break
                    
        while True:
            especie=input("Especie: ")
            if especie.isalpha()== False:
                print("Error: solo str")
            else:
                break
        color=input("Color: ")
        while True:
            ingresar_raza=input("desea ingresae raza (si/no): ").lower() # preguntar si quiere agregar la raza
            if ingresar_raza != "si" and ingresar_raza !="no":
                print("Ingresa si/no")
            else:
                break
        if ingresar_raza == "si": # si dice que si se solicita la raza
            raza= input("Ingresa la Raza: ")
        else: # en caso de que diga que no, no se hace nada
            pass
        id =id_mascota_random() # variable que almacena el id random que retorna la funcion id_mascota_random
        ClasseMascota.Mascota(id, nombre,color,especie, raza) # se llama el modulo ClasseMascota que contiene la clase Mascota, y se pasan como parametros los atributos que tiene la mascota
        #Solicitar datos propietario
        print("\nINGRESAR DATOS PROPIETARIO\n")
        Id= input("ID: "),
        nombre=input("NOMBRE: "),
        apellido = input("APELLIDOS: "),
        direccion = input("DIRECCION: "),
        telefono = input("TELEFONO: "),
        correo = input("CORREO: ")
        ClassePropietario.Propietario(Id,nombre,apellido,direccion,telefono,correo) # se llama el modulo ClassePropietario y su clase propietario, y se pasan como parametros los atributos que tiene el propietario
        
    def realizar_visitas(self): #Metodo de veterinario, que se encargara de realizar la visita
        if bsd.ides_veterinarios==[]: # si no exiten veterinarios
            print("No exiten veterinarios, agrega uno")
        else:
            while True:#Excepciones
                id_veterinario_visita= input("Ingresa el id del veterinario que visitara la mascota: ")
                if len(id_veterinario_visita) != 10:
                    print("Error, ingresa 10 digitos")
                elif id_veterinario_visita not in bsd.ides_veterinarios:
                    print("Error, ese id no se encuentra registrado")
                else:
                    break
            for i in bsd.lista_veterinarios: # recorrer la lista de los propietarios, para mostrar las mascotas
                if i["Id"] == id_veterinario_visita:
                    if i["Mascotas"]==[]: # si el veterinario no tiene asignado una mascota
                        print("Error, ese veterinario no tiene asignada ninguna mascota, (asignale una)")
                    else: # si por el contrario si tiene
                        print(f"Mascotas: {i["Mascotas"]}")# Mostrar mascotas que tiene asignadas la mascota
                        #Excepciones
                        while True:
                            id_mascota_visita = input("Ingresa el id de la mascota a la que se le realizara la visita: ")
                            if id_mascota_visita.isnumeric()== False: # si la entrada es distinta a  numeros
                                print("Error, ingresa numeros")
                            elif len(id_mascota_visita) !=4: # si ingresa mas de 4 digitos
                                print("Error, digita 4 digitos")
                            elif id_mascota_visita not in i["Mascotas"]: # si la mascota ingresada, no se encuentran en las mascotas asginadas al veterinario
                                print("Error, digita un id correcto")
                            else:
                                break
                            
                        #DATOS DE VISITA
                        print("\n\t REALIZAR VISITA\n")
                        id_visita= id_visita_random() # esta variable almacenara el id random que se generara
                        
                        #Temperatura
                        while True:
                            #excepciones
                            temperatura_mascota = input("Ingresa la temperatura: ") 
                            if temperatura_mascota.isnumeric()== False:
                                print("Ingresa datos numericos")
                            elif len(temperatura_mascota) !=2:
                                print("Ingresa correctamente la temperatura")
                            else:
                                break
                        #Peso mascota
                        while True:
                            peso_mascota= input("Ingresa el peso: ")
                            if peso_mascota.isnumeric()== False:
                                print("Error, ingresa datos numericos")
                            else:
                                break
                        #frecuencia Respiratoria
                        while True:
                            frecuencia_respiratoria = input("Ingresa la frecuencia respiratoria por  minuto: ")
                            if frecuencia_respiratoria.isnumeric()== False:
                                print("Error, ingresa numeros")
                            else:
                                break
                        #frecuencia cardiaca
                        while True:
                            frecuencia_cardiaca = input("Ingresa la frecuencia cardiaca por minuto: ")
                            if frecuencia_cardiaca.isnumeric()== False:
                                print("Error, ingresa numeros")
                            else:
                                break
                        #Estado de animo
                        while True:
                            estados_animos=[f"{NEON_BLUE}EXITADO{RESET}", f"{NEON_BLUE}FELIZ{RESET}", f"{NEON_BLUE}TRISTE{RESET}", f"{NEON_BLUE}ENOJADO{RESET}",f"{NEON_BLUE}CANSADO{RESET}"]
                            print(estados_animos)
                            estado_animo_mascota = input("Ingresa el estado de animo: ").upper()
                            if estado_animo_mascota not in estados_animos:
                                print("Error, ingresa un estado de animo correcto")
                            else:
                                break
                        #Fecha registro
                        fecha_sin_formato=datetime.now() # definir hora
                        fecha_con_formato=fecha_sin_formato.strftime("%d/%m/%Y %H:%M:%S")
                        #recomendaciones
                        recomendaciones = input("Recomendaciones: ")
                        #Almacenar todo en un diccionario
                        
                        visita={ # diccionario que almacena todos los datos de visita
                            "Id Visita": id_visita,
                            "Temperatura":temperatura_mascota,
                            "Peso":peso_mascota,
                            "Frecuencia Respiratoria": frecuencia_respiratoria,
                            "Frecuencia Cardiaca": frecuencia_cardiaca,
                            "Estado de Animo": estado_animo_mascota,
                            "ID veterinario": id_veterinario_visita, # id del veterinario que le realiza la visita
                            "Recomendaciones": recomendaciones,
                            "Fecha Visita": fecha_con_formato
                        }
                        for i in bsd.lista_mascota: # recorrer la lista con todas las mascotas
                            if i["Id"]==id_mascota_visita: #ingresar al diccionario y comparar si los id son iguales
                                i["Historia Clinica"].append(id_visita) # agregar a la historia clinica de la mascota el id de la visita
                                encabezado =[f"{NEON_BLUE}ID mascota{RESET}", f"{NEON_BLUE}Nombre{RESET}",f"{NEON_BLUE}Color{RESET}",f"{NEON_BLUE}Especie{RESET}",f"{NEON_BLUE}Raza{RESET}",f"{NEON_BLUE}IDveterinario{RESET}", f"{NEON_BLUE}Historial Clinico{RESET}"] # encabezado con estilos (colores)
                                datos=[i.values()]
                                print(tabulate(datos, headers=encabezado, tablefmt="grid"))
                                
                        bsd.lista_visitas.append(visita) # almacenar la visita en la lista visitas
                        bsd.ides_visitas.append(id_visita)# almacenar el id de la visita en la lista de todos los ides de las visitas
            
    def Buscar_historia_clinica(self): #Metodo que se encargara de buscar las historias clinicas
        
        if bsd.ides_mascotas==[]: # verifica que las lista de ides_mascotas no este vacia
            print("Error, no hay mascotas registradas")
        else:
            info_mascota=Veterinario().buscar_mascota() # llamar metodo de veterinario que lo que hace es buscar una mascota, y retorna el diccionario, el cual se almacena en la variable info_mascota
            print(f"{NEON_GREEN}Historias Clinicas  de la mascota{RESET} ({info_mascota["Nombre"]}) {info_mascota["Historia Clinica"]}")
            while True:
                #excepciones
                id_visitas_ingresada= input("Ingresa el id de visita: ")
                if id_visitas_ingresada.isnumeric()== False:
                    print("Error,digita valores numericos")
                elif len(id_visitas_ingresada)!=5:
                    print("Error, escribe 5 digitos")
                elif id_visitas_ingresada not in bsd.ides_visitas:
                    print("Error, ese id no es valido")
                else:
                    break
            datos=[] # datos que seran los valores del diccionario
            encabezado=[f"{NEON_BLUE}Id visita{RESET}",f"{NEON_BLUE}Temperatura{RESET}",f"{NEON_BLUE}Peso{RESET}",f"{NEON_BLUE}Frecuencias Respiratoria{RESET}",f"{NEON_BLUE}Frecuencia cardiaca{RESET}",f"{NEON_BLUE}Estado Animo{RESET}", f"{NEON_BLUE}Id Veterinario{RESET}",f"{NEON_BLUE}Recomendaciones{RESET}",f"{NEON_BLUE}Fecha Registro{RESET}"]
            
            for i in bsd.lista_visitas: # for que recorrera la lista que contiene las informaciones de todas las visitas
                if i["Id Visita"]== id_visitas_ingresada: # si el id de la visita que esta registrada es igual al que se ingreso, mostrar toda la info de la visita
                    datos.append(list(i.values()))
                    print("\nVISITA")
            print(tabulate(datos, headers=encabezado, tablefmt="grid"))
                    

    def buscar_mascota(self):#Metodo para buscar una mascota en especifico
        if bsd.lista_mascota==[]:
            print("No hay mascotas Registradas")
        else:
            mascota_buscar = input('Ingresa el nombre de la mascota que deseas buscar: ').lower() # se solicita el nombre de la mascota que se desea buscar
            for i in bsd.lista_mascota: 
                if i['Nombre'] == mascota_buscar: # se verifica que el nombre se encuentre
                    print(i) # se imprime todos los diccionarios de las mascotas que tengan ese nombre
                    while True:
                        mascota_buscar_id = input('Ingresa el ID de la mascota: ') # Se solicita el numero de ID de la mascota
                        #Excepciones
                        if mascota_buscar_id.isnumeric()==False:
                            print("Error, ingresa numeros")
                        elif len(mascota_buscar_id) != 4:
                            print("Error, ingresa 4 digitos")
                        elif mascota_buscar_id not in bsd.ides_mascotas:
                            print('El id ingresado no existe\n asegurare de haber escrito correctamente.')
                        else:
                            break
                    # se imprime el diccionario que corresponde al id ingresado
                    for m in bsd.lista_mascota:
                        if m['Id'] == mascota_buscar_id:
                            encabezado =[f"{NEON_BLUE}ID mascota{NEON_BLUE}", f"{NEON_BLUE}Nombre{RESET}",f"{NEON_BLUE}Color{RESET}",f"{NEON_BLUE}Especie{RESET}",f"{NEON_BLUE}Raza{RESET}",f"{NEON_BLUE}ID veterinario{RESET}", f"{NEON_BLUE}Historial Clinico{RESET}"]
                            print('LISTA MASCOTAS')
                            datos = [m.values()] # almacenar los datos del diccionario en esta lista
                            print(tabulate(datos,headers=encabezado, tablefmt="grid"))
                            return m # retornar el diccionario
                else:
                    print(f"Ese nombre no se encuentra")
                
    def buscar_mascotas(self): # metodo que muestra todas las mascotas
        if bsd.lista_mascota==[]: # verifica que si hallan mascotas
            print("No hay mascotas registradas")
        else:
            encabezado =[f"{NEON_BLUE}ID mascota{NEON_BLUE}", f"{NEON_BLUE}Nombre{RESET}",f"{NEON_BLUE}Color{RESET}",f"{NEON_BLUE}Especie{RESET}",f"{NEON_BLUE}Raza{RESET}",f"{NEON_BLUE}ID veterinario{RESET}", f"{NEON_BLUE}Historial Clinico{RESET}"]
            datos=[] # se almacenan en la lista datos los valores
            for i in bsd.lista_mascota:
                datos.append(i.values()) # almacenar cada una de los valores de una mascota a la lista de datos generales
            print(tabulate(datos, headers=encabezado, tablefmt="grid")) # se imprime con tabulate
                


    def tarjeta_profesional(self):#Metodo que solicita la tarjeta profesional de veterinario
        os.system('cls')
        print(f"\t\n TARJETA PROFESIONAL\n")
        diccionario_tarjeta={ # diccionario con toda la información de la tarjeta profesional
            "Nombre":f"{self.nombres} {self.apellidos}",
            "Nombre Titulo":"",
            "Nombre Especialidad":"",
            "Nombre instituto":"",
            "Año":""
        }
        while True: 
            especialidad=input("Ingresa la especialidad: ").strip()
            if especialidad.isalpha()==False:
                print("Error, ingresa solo str")
            else:
                break
            
        while True: 
            nombre_instituto=input("Ingresa el nombre del instituto: ").strip()
            if nombre_instituto.isnumeric()==True:
                print("Error, ingresa solo str")
            else:
                break
        while True: 
            Año=input("Ingresa el año de certificación: ").strip()
            if Año.isnumeric()==False:
                print("Error, ingresa solo numeros")
            else:
                break
        while True: 
            nombre_titulo=input("Ingresa el titulo: ").strip()
            if nombre_titulo.isalpha()==False:
                print("Error, ingresa solo str")
            else:
                break
        diccionario_tarjeta["Nombre Titulo"]=nombre_titulo
        diccionario_tarjeta["Nombre Especialidad"]=especialidad
        diccionario_tarjeta["Nombre instituto"]=nombre_instituto
        diccionario_tarjeta["Año"]= Año
        return diccionario_tarjeta
    os.system('cls')
    




def id_mascota_random():
    lista_id=[]
    lista_numeros =["1","2","3","4","5","6","7","8","9","0"]
    while len(lista_id) <=3:
        digito = random.choice(lista_numeros)
        lista_id.append(digito)
    return "".join(lista_id)
def id_visita_random():
    lista_id=[]
    lista_numeros =["1","2","3","4","5","6","7","8","9","0"]
    while len(lista_id) <=4:
        digito = random.choice(lista_numeros)
        lista_id.append(digito)
    
    return "".join(lista_id)
        
#Veterinario().buscar_mascotas()
#Veterinario().buscar_mascota()
