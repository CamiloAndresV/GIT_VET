from itertools import chain # este modulo permite realizar la manipulacion de datos de manera rapida
import bsd
import os 
class admin:
    def registrar_vet(): # metodo de administrador que permite registrar veterinarios
        import ClasesVeterinario # importa el modulo ClasesVeterinario
        while True: 
            try:
                os.system('clear')
                print('\tINGRESA LOS DATOS DEL VETERINARIO\n')
                id = str(input("Ingresa el id del veterinario: ")) #se pide el id 
                if id in bsd.ides_veterinarios or len(id) != 10: #se hace control de excepciones
                    print("\n\tALERT: el id ingresado ya se encuentra registrado, o el id debe tener 10 digitos")
                #if len(id) != 10:
                    #print("ERROR: el id debe tener 10 digitos")
                else:
                    while True:
                        nombre = str(input("ingresa el nombre del veterinario: ")) #pedir datos
                        if nombre.isnumeric() == True: #excepcion
                            print("\n\tERROR: el nombre no debe contener numeros")
                        else:
                            break
                    while True:
                        apellido = str(input("ingresa el apellido del veterinario: ")) #pedir datos
                        if apellido.isnumeric() == True: #excepcion 
                            print("\n\tERROR: el apellido no debe contener numeros")
                        else:
                            break
                    direccion = input("ingresa la direccion del veterinario: ")
                    break #sale del ciclo for
            except ValueError:
                print("\n\tERROR: el dato que ingresaste no es correcto")
        while True: #se crea un bucle
            try: 
                telefono = str(input("ingresa el telefono del veterinario: "))
                if len(telefono) != 10: #excepcion de 10 numeros
                    print("\n\tERROR: el telefono debe contener 10 digitos")
                else:
                    break
            except ValueError:
                print("\n\tERROR: dato ingresado no valido")
        os.system('clear')
                
        tarjeta= ClasesVeterinario.Veterinario(id,nombre,apellido,direccion,telefono).tarjeta_profesional() # se llama el metodo tarjeta de la clase veterinario y el diccionario retornado se pasa como parametro en la clase Veterinario
        ClasesVeterinario.Veterinario(id,nombre,apellido,direccion,telefono,tarjeta).registrar_veterinario()
        
        
    def consultar_mascotas_propietario(): #FUNCION QUE CONSULTA LAS MASCOTAS DE UN PROPIETARIO
        if bsd.ides_propietarios==[]: # se verifica que si hallan datos
            print("No hay propietarios registrados")
        else:
            while True:
                solic_id = input("ingresa el id del propietario: ") # Solicitar id de propietario
                if solic_id.isnumeric()== False:
                    print("Ingresa numeros")
                elif len(solic_id) !=10:
                    print("Error, ingresa 10 digitos")
                elif solic_id not in bsd.ides_propietarios:
                    print("Error, ese id no ha sido registrado")
                else:
                    break
            for i in bsd.lista_propietario:# For iterable sobre la lista de los propietarios
                if (i["id"]) == solic_id: #verifica si el id si es corresponde al ingresado
                    print(f"Mascotas propietario: {i["Mascotas"]}") #mostrar las mascotas del propietario
                    while True:
                        mascota_selec=input("Ingresa el id de la mascota: ") # solicitar id de la mascota que desea ver
                        #Excepciones
                        if mascota_selec.isnumeric()==False:
                            print("Error, ingresa numeros")
                        elif len(mascota_selec) !=4:
                            print("Error, ingresa 4 digitos")
                        elif mascota_selec not in bsd.ides_mascotas:
                            print("Error, ese id no ha sido registrado")
                        else:
                            break
                    for m in bsd.lista_mascota: # for que iterara sobre la lista mascotas
                        if m["id"]== mascota_selec: # en caso de que encuentre una mascota con ese id, imprime la información de esa mascota
                            print(m) # imprimir

                

    def mostrar_mascotas_veterinario(): # metodo de administrador que permitira mostrar las mascotas de un veterinario
        if bsd.ides_veterinarios==[]: # si no se encuentran veterinarios registrados, le dice que no hay veterinarios registrados
            print("No se encuentran veterinarios registrados")
        else:
            while True: # control de excepciones
                id_veterinario= input("Ingresa el id del veterinario: ")
                if id_veterinario.isnumeric()== False:
                    print("Error, ingresa numeros")
                elif id_veterinario not in bsd.ides_veterinarios:
                    print("Ese id no se encuentra regitrado")
                elif len(id_veterinario) !=10:
                    print("Ingresa 10 digitos")
                else:
                    break
            for i in bsd.lista_veterinarios: # recorrer la lista de los veterinarios
                if i["Id"]== id_veterinario: # si el id de ese diccionario es igual al que esta siendo  digitado, imprimolas mascotas de este veterinario
                    print(f"Mascotas: {i["Mascotas"]}")

        
    def modificar_propietario(): # funcion que actualiza los datos del propietario
        if bsd.lista_propietario ==[]: # si la lista esta vacia, significa que no hay propietarios
            print("Error, el veterinario no ha agregado Propietarios")
        else:
            while True:
                propietario_modificar = input("Ingresa el ID del propietario: ") # solicitare el nombre del propietario
                if propietario_modificar not in bsd.ides_propietarios: # si el id ingresado no se encuentra en la listra        ides_propietarios, mostrar error
                    print("No existe propietario con ese numero de ID")
                else:
                    break
            for i in bsd.lista_propietario: # recorrer la lista que contiene todos los propietarios
                if i["Id"]== propietario_modificar: # se accede a cada propietario y se compara su ID
                    #Solicitar nuevos datos y control de excepciones
                    while True:
                        nueva_direccion = (input("Ingresa la direccion: "))
                        if nueva_direccion.isnumeric()==True:
                            print("Error, no ingreses numeros")
                        else:
                            break
                        
                    while True:
                        nuevo_telefono = input("Ingresa el numero de telefono: ")
                        if nuevo_telefono.isnumeric()== False:
                            print("No ingreses str")
                        else:
                            break
                    while True:
                        arroa="@gmail.com"
                        nuevo_correo=input("Ingresa el correo electronico del veterinario: ")
                        if arroa not in nuevo_correo:
                            print("Ingresa el @gmail.com")
                        else:
                            break
                    #Reemplazar los valores de las claves del diccionario 
                    i["Direccion"]=nueva_direccion
                    i["Telefono"]=nuevo_telefono
                    i["Correo"]= nuevo_correo
                    print("\nInformación de Propietario Actualizada\n")
                
    def modificar_veterinario():
        import ClasesVeterinario
        if bsd.ides_veterinarios==[]:
            print("Error, no se ha registrado un veterinario")
        else:
            while True:
                # solicitar id de veterinario a modificar
                veterinario_modificar = input("Ingresa ID del veterinario: ")
                if veterinario_modificar.isalpha() == True:
                    print("Ingresa solo caracteres numericos")
                elif len(veterinario_modificar) != 10:
                    print("Error, ingresa solo 10 digitos")
                elif veterinario_modificar not in bsd.ides_veterinarios:
                    print("Error, ese veterinario no existe")
                else:
                    break
            # se recorrera la lista de los veterinarios
            for i in bsd.lista_veterinarios:
                # se verificara si el id de este veterinario es igual al que se ingreso
                if i["Id"]==veterinario_modificar: 
                    # Datos a modificar
                    while True:
                        arroa="@gmail.com"
                        nuevo_correo=input("Ingresa el correo electronico del veterinario: ")
                        if arroa not in nuevo_correo:
                            print("Ingresa el @gmail.com")
                        else:
                            break
                        
                    while True:
                        nueva_direccion = input("Ingresa la direccion de veterinario: ")
                        if nueva_direccion.isnumeric()== True:
                            print("Error, no ingreses numeros")
                        else:
                            break
                    while True:
                        nuevo_telefono = input("Ingresa el numero telefonico: ")
                        if nuevo_telefono.isnumeric() == False:
                            print("Error, ingresa solo numeros")
                        elif len(nuevo_telefono)  != 10:
                            print("Error, ingresa un numero telefonico valido, (de 10 digitos)")
                        else:
                            break
                    while True:
                        mod_tarjeta_profesional= input("Desea agregar otra tarjeta profesional si/no: ").lower()
                        if mod_tarjeta_profesional != "si" and mod_tarjeta_profesional != "no":
                            print("Error, ingresa si/no")
                        else:
                            break
                    if mod_tarjeta_profesional =="si":  
                        print("\n   TARJETA PROFESIONAL \n")
                        nueva_tarjeta_profesional_veterinario = ClasesVeterinario.Veterinario().tarjeta_profesional() # se llama la funcion tarjeta del modulo  tarjeta_veterinario
                        i["Telefono"]=nuevo_telefono 
                        i["Direccion"]= nueva_direccion
                        i["Correo"]=nuevo_correo
                        i["tarjeta Profesional"].append(nueva_tarjeta_profesional_veterinario)
                    else:
                        i["Telefono"]=nuevo_telefono 
                        i["Direccion"]= nueva_direccion
                        i["Correo"]=nuevo_correo

                    print("Información actualizada")
                    print("")
                    print(i) # imprimira el diccionario de los datos del veterinario que se modifico

    def asignar(): # funcion que se encargara de asignar un veterinario a una mascota, y una mascota a un veterinario
        if bsd.ides_veterinarios==[]:
            print("No hay veterinarios registrados")
        else:
            while True:
                id_veterinario = input("Ingresa el id veterinario: ") # solicitar id del veterinario
                if len(id_veterinario) !=10: # excepcion
                    print("Error, ingresa 10 digitos")
                elif id_veterinario.isnumeric()== False: # Si el id_veterinario no es numerico
                    print("Error, ingresa numeros")
                elif id_veterinario not in bsd.ides_veterinarios: # si el id no se encuentra en la lista ides_veterinarios
                    print("Error, ese id no se encuentra registrado.")
                else: # finalizar bucle
                    break
            for i in bsd.lista_veterinarios: # recorrer lista que contiene los diccionarios de todos los veterinarios
                if i["Id"]== id_veterinario: # se compara si el id que se encuentra en este es igual al id que fue ingresado
                    print("\n INGRESA EL ID DE LA MASCOTA\n")
                    mascotas_asignadas=[] # lista donde se almacenaran las mascotas que se encuentran asignadas a un veterinario
                    for k in bsd.lista_veterinarios:
                        mascotas_asignadas.append(k["Mascotas"])
                    mascotas_asignadas_mod=list(chain.from_iterable(mascotas_asignadas)) # esto permite convertir varias listas en una sola

                    for j in bsd.lista_mascota: # un for que iterara sobre las mascotas y mostrara las que no tienen veterinario
                        mascotas_sin_veterinario=[] # id de mascotas que no tienen veterinario
                        if j["Veterinario"]=="": # si en el diccionario de las mascotas, en la clave Veterinario tenga un valor, en caso    de que no, se le asignara el id del veterinario a essta mascota
                            mascotas_sin_veterinario.append(j["Id"])
                            print(f"\n MASCOTAS SIN VETERINARIO {mascotas_sin_veterinario[0]}")
                            while True:
                                id_mascota= input("Ingresa el id de la mascota: ") # se solicita el numero de id de la mascota
                                if len(id_mascota) != 4:
                                    print("El id de la mascota es de 4 digitos")
                                elif id_mascota not in bsd.ides_mascotas: # si el numero de ficha no se encuentra en la listaides_mascotas
                                    print("Error, ese id no se encuentra")
                                elif id_mascota.isnumeric()==False:
                                    print("Error, ingresa numeros")
                                elif id_mascota in i["Mascotas"]: # si el id de la mascota ya esta asignada al veterinario
                                    print("Este veterinario ya tiene esa mascota")
                                elif id_mascota in mascotas_asignadas_mod:
                                    print("Esa mascota ya le pertenece a otro veterinario")
                                else:
                                    break
                            i["Mascotas"].append(id_mascota) # se agrega el id de la mascota a la informacion del veterinario
                            j["Veterinario"]=id_veterinario # se agrega el id del veterinario a la informacion de la mascota
                            print(f"\n  LISTA VETERINARIO\n{i}")
                            print(f"\n  LISTA MASCOTAS\n{j}")
                            while True:
                                agregar_mas= input("\nDesea agregar mascota a otro veterinario?\n ").lower().strip()
                                if agregar_mas != "si" and agregar_mas != "no":
                                    print("Error, ingresa si/no")
                                else:
                                    break
                            if agregar_mas =="si": # si dice que si 
                                if len(mascotas_sin_veterinario)==1: # En este caso si la lista solo tiene un elemento, significa que en realidad no se encuentran ninguna mascota sin veterinario
                                    print("No se encuentran mascotas sin veterinario")
                                else:  # de lo contrario se retorna de nuevo la funcion asignar
                                    return admin.asignar()
                            else:
                                break # y si dice que no, finaliza el bucle



                    #OPCION PARA CAMBIAR EL VETERINARIO DE UNA MASCOTA QUE YA TIENE VETERINARIO
                    print("""\n DESEA MODIFICAR UN VETERINARIO DE LA MASCOTA QUE YA TIENE UN VETERINARIO ASIGNADO\n
                        1. SI / 2. NO""")
                    while True:
                        seleccion = input("").lower() #solicitar si desea cambiar el veterinario de una mascota
                        if seleccion!= "si" and seleccion !="no":
                            print("error, ingresa si/no")
                        else:
                            break
                    if seleccion =="si":
                        while True:
                            id_mascota_mod = input("Ingresa el id de la mascota: ") # solicitar el id de la mascota a la que se le modificara el veterinario
                            if len(id_mascota_mod) != 4:
                                print("Error, ingresa 4 digitos")
                            elif id_mascota not in bsd.ides_mascotas:
                                print("Error, ese id de mascota no se encuentra registrado")
                            else:
                                break
                        for m in bsd.lista_mascota: # recorrer la lista de las mascotas para cambiar su veterinario
                            if m["Id"]== id_mascota_mod: # si el id es igual al que se encuentra en el diccionario
                                while True:
                                    id_veterinario=input("Ingresa el id del veterinario que asignaras: ")
                                    if id_veterinario not in bsd.ides_veterinarios:
                                        print("Error, ese id de veterinario no se encuentra registrado")
                                    elif len(id_veterinario) != 10:
                                        print("Error, el ingresa 10 digitos")
                                    else:
                                        break
                                # Asignar veterinario a mascota
                                m["Veterinario"]=id_veterinario
                        for v in bsd.lista_veterinarios: # Redcorrer la lista de los veterinarios para agregarle la mascota
                            if v["Id"] ==id_veterinario: # si el id del diccionario es igual al id_veterinario ingresado
                                v["Mascotas"].append(id_mascota) # Agregar mascota a la lista mascotas del veterinario

                        
                                    
                            