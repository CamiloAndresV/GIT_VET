import random
import ClasseMascota 
import ClassePropietario
import ClaseAdmin
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
            "Mascotas":[] #se crea la lista que pertenece a las mascotas del propietario
        }
        bsd.ides_veterinarios.append(self.id)#Se guardardo el id del veterinario a la lista respectiva
        bsd.lista_veterinarios.append(diccionario_veterinario) #Se subio a la lista de veterinarios
        
    def registrar_mascota(self):
        #Solicitar datos propietario
        print("\nINGRESAR DATOS PROPIETARIO\n")
        while True:
            try:
                id = input("ID: "),
                if id in len(id) != 10: #se hace control de excepciones
                    print("Error: el id debe contener 10 digitos")
                else:
                    while True:
                        nombre=input("NOMBRE: ")
                        if nombre.isnumeric() == True:
                            print("Error: no puedes ingresar numeros")
                        else:
                            break
                    while True:
                        apellido = input("APELLIDOS: ")
                        if apellido.isnumeric() == True:
                            print("Error: no puedes ingresar numeros")
                        else:
                            break
                    direccion = input("DIRECCION: ")
                    while True:
                        telefono = input("TELEFONO: ")
                        if telefono in len(telefono) != 10:
                            print("Error: el telefono debe tener 10 numeros")
                        else:
                            break
                    while True:
                        u = "@."
                        correo = input("CORREO: ")
                        if u not in correo:
                            print("ERROR: ingresa un correo valido")
                        else:
                            break
                    break
            except ValueError:
                print("ERROR: dato ingresado no valido")
                    

        propietario = ClassePropietario.Propietario(id,nombre,apellido,direccion,telefono,correo)
        #Solicitar datos de la mascota 
        print("\nINGRESA LOS DATOS DE LA MASCOTA\n")
        nombre=input("Nombre:").lower()
        especie=input("Especie: ")
        mascota_existe = verificar_mascota_existente(nombre,especie)
        print(mascota_existe)
        #No dejar pasar si estos dos datos ya existen
        while mascota_existe == True:
            print("La mascota ya existe")
            nombre=input("Nombre:")
            especie=input("Especie: ")
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
        id=id_mascota_random()
        mascota = ClasseMascota.Mascota(id,nombre,color,especie, raza="No definido")
        propietario.mascota=mascota.id
        #Guardar datos de la mascota y el propietario en la lista 
        propietario.registrar_propietario()
        mascota.registrar_mascota()
        
    def registrar_propietario(self):
        print("\nINGRESAR DATOS MASCOTA\n")
        while True:
            try:
                nombre=input("Nombre:").lower()
                if nombre.isdigit():
                    print("Error: solo str")
                else:
                    while True:
                        especie=input("Especie: ")
                        if especie.isnumeric():
                            print("Error: solo str")
                        else:
                            break
                    break
            except ValueError:
                print("ERROR: dato ingresado no valido")
        mascota_existe = verificar_mascota_existente(nombre,especie)
        print(mascota_existe)
        #No dejar pasar si estos dos datos ya existen
        while mascota_existe == True:
            print("La mascota ya existe")
            nombre=input("Nombre:")
            especie=input("Especie: ")
        mascota = ClasseMascota.Mascota("131313",nombre = nombre,color=input("Color: "),especie=especie, raza=input("Raza: "))
        #Solicitar datos propietario
        print("\nINGRESAR DATOS PROPIETARIO\n")
        Id= input("ID: "),
        nombre=input("NOMBRE: "),
        apellido = input("APELLIDOS: "),
        direccion = input("DIRECCION: "),
        telefono = input("TELEFONO: "),
        correo = input("CORREO: ")
        ClassePropietario.Propietario(Id,nombre,apellido,direccion,telefono,correo)
        
    def realizar_visitas(self): #Metodo de veterinario, que se encargara de realizar la visita
        if bsd.ides_veterinarios==[]: # si no exiten veterinarios
            print("No exiten veterinarios, agrega uno")
        else:
            while True:
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
                            id_mascota_visita = input("Ingresa el id de la mascota a la que se le   realizara la visita: ")
                            if id_mascota_visita.isnumeric()== False: # si la entrada es distinta a  numeros
                                print("Error, ingresa numeros")
                            elif len(id_mascota_visita) !=4: # si ingresa mas de 4 digitos
                                print("Error, digita 4 digitos")
                            elif id_mascota_visita not in i["Mascotas"]:
                                print("Error, digita un id correcto")
                            else:
                                break
                            
                        #DATOS DE VISITA
                        print("\n\t REALIZAR VISITA\n")
                        #Temperatura
                        while True:
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
                            estados_animos=["EXITADO", "FELIZ", "TRISTE", "ENOJADO","CANSADO"]
                            print(estados_animos)
                            estado_animo_mascota = input("Ingresa el estado de animo: ").upper()
                            if estado_animo_mascota not in estados_animos:
                                print("Error, ingresa un estado de animo correcto")
                            else:
                                break
                        #Fecha registro
                        fecha_sin_formato=datetime.now() # definir hora
                        fecha_con_formato=fecha_sin_formato.strftime("%A, %d de %B de %Y, %H:%M:%S")
                        print(fecha_con_formato)

                        
                    
                        
                    
                    

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
            for i in bsd.lista_mascota:
                if i['Id'] == mascota_buscar_id:
                    print(i)
                
                
    def buscar_mascotas(self): # metodo que muestra todas las mascotas
        if bsd.lista_mascota==[]:
            print("No hay mascotas registradas")
        else:
            
            print('LISTA MASCOTAS')
            for i in bsd.lista_mascota:
                print(f"{i.values()}\n")



    def tarjeta_profesional(self):#Metodo que solicita la tarjeta profesional de veterinario
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
    
#mi_objeto = Veterinario()
### Llamar al método
#mi_objeto.registrar_propietario()



def verificar_mascota_existente(nombre,especie):#Verifica si una mascota existe o no
    #Recorrer la lista de mascotas para verificar comparar si la mascota existe o no 
    for i in bsd.lista_mascota:
        if i["Nombre"]==nombre: 
            return True
        elif i["Especie"]== especie:
            return True
        else: 
            return False
def id_mascota_random():
    lista_id=[]
    lista_numeros =["1","2","3","4","5","6","7","8","9","0"]
    while len(lista_id) <=3:
        digito = random.choice(lista_numeros)
        lista_id.append(digito)
    return "".join(lista_id)
        
#Veterinario().buscar_mascotas()
#Veterinario().buscar_mascota()
