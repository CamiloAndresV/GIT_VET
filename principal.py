import bsd # modulo que contiene las listas generales
#import pyfiglet 
import ClaseAdmin
import os


def menu():
    #nombre_veterinaria= pyfiglet.figlet_format(f"\tMASCOTA   FELIZ", font="Doom")
    perro1=(rf"""
            
         __ / \                                                           / \__
     ___/@      )                                                       (      @\___        
    0           \                                                      /            O        
    \_____)      \                                                    /       (____/        
            \  ____\                                                /_____  /
            
            """)
    
    
    
    print(perro1) # se imprime los eslogan de las mascotas
    #print(nombre_veterinaria)
    print("\nINGRESA UNA OPCION\n")
    import ClasesVeterinario
    while True:
        seleccion = input(f"\n\tINGRESAR COMO\n1. Administrador\n2. Veterinario\n3. Salir \nDIGITA AQUI: ")
        if seleccion != "1" and seleccion != "2":
            print("Error, ingresa una opcion correcta")
        else:
            break
    if seleccion =="1": # si selecciona administrador
        os.system('clear')
        print("""OPCIONES ADMINISTRADOR\n1. Registrar un veterinario\n2. Modificar información propietario\n3. Modificar información Veterinario\n4. Consultar mascotas de propietario\n5. Consultar mascotas veterinario\n6. Asignar Mascota a Veterinario\n7. buscar historia clinica de Mascota\n8. Volver Menu """)
        while True:
            opcion_admin= input("Ingresa la opcion: ")
            if opcion_admin not in ["1","2","3","4","5","6","7","8"]:
                print("Error opciones(1-8)")
            else:
                break
        if opcion_admin =="1": # modulo, clase y metodo que permite registrar un veterinario
            ClaseAdmin.admin.registrar_vet() # llamar el modulo ClaseAdmin que contiene la clase Admin y el metodo (registrar_vet) que  llama el modulo ClaseVeterinario que contiene la clase veterinario y se llama el metodo registrar_Veterinario
            print("Veterinario Registrado Exitosamente")  
            volver_menu()
        elif opcion_admin == "2": # modulo, clase y metodo que permite actualizar datos de propietario
            os.system('clear')
            ClaseAdmin.admin.modificar_propietario()
            volver_menu()
        elif opcion_admin == "3":# modulo, clase y metodo que permite actualizar datos de Veterinario
            ClaseAdmin.admin.modificar_veterinario()
            print("Modificacion exitosas")
            volver_menu()
        elif opcion_admin =="4":# modulo, clase y metodo que permite mostrar mascotas de propietario
            ClaseAdmin.admin.consultar_mascotas_propietario()
            volver_menu()
        elif opcion_admin == "5":
            
            ClaseAdmin.admin.mostrar_mascotas_veterinario()
            volver_menu()
        elif opcion_admin == "6":# modulo, clase y metodo que permite asignar mascotas
            ClaseAdmin.admin.asignar()
            volver_menu()
        elif opcion_admin =="7": # modulo ClassVeterinario, clase Veterinario y metodo buscar_historia_clinica
            ClasesVeterinario.Veterinario.Buscar_historia_clinica()
            volver_menu()
        elif opcion_admin == "8": # si selecciona 8 vuelve al menu
            menu()
            
    elif seleccion == "2": #Si selecciona el Veterinario
        print("\nOPCIONES DE VETERINARIO\n1. Registrar Nueva mascota\n2. Registrar Nuevo propietario\n3. Buscar una Mascota en especifico\n4. Buscar Mascotas\n5. Realizar Visita\n6. Buscar Historia Clinica Mascotas\n7. Volver Menu")
        while True:
            opcion_veterinario= input("Ingresa la opcion: ")
            if opcion_veterinario not in ["1", "2", "3","4","5","6","7"]: # 5 opciones que ejecutan lo que puede realizar el veterinario
                print("Error, opciones (1-7)")
            else:
                break
        # METODOS DE VETERINARIO
        if opcion_veterinario == "1": # si la opcion es 1, Registra la mascota
            print(f"\t\n REGISTRAR MASCOTA\n")
            ClasesVeterinario.Veterinario().registrar_mascota() # se llama el modulo ClasesVterinario, la clase Veterinario y () porque esa clase recibe atributos, y posteriormente se llama el metodo que permite registrar una mascota
            volver_menu()
        elif opcion_veterinario =="2": # si la opcion es 2, registra el veterinario
            print(f"\t\n REGISTRAR VETERINARIO\n")
            ClasesVeterinario.Veterinario().registrar_propietario() # Se llama el modulo CLasesVeterinario, la clase Veterinario con () ya que la clase contiene atributos, ademas se llama el metodo que permite registrar un propietario
            volver_menu()
        elif opcion_veterinario =="3": # si la opcion es 3, busca una mascota en especifico
            print("\nBUSCAR MASCOTA\n")
            ClasesVeterinario.Veterinario().buscar_mascota() # se llama el modulo ClasesVterinario, la clase Veterinario con () ya que esta clase recibe atributos, posteriormente el metodo que permite buscar una mascota en especifico
            volver_menu()
        elif opcion_veterinario == "4": # si la opcion es 4, busca todas las mascotas
            print("\nBUSCAR MASCOTAS\n")
            ClasesVeterinario.Veterinario().buscar_mascotas() # se llama el modulo ClasesVterinario, la clase Veterinario con () ya que esta clase recibe atributos, posteriormente el metodo que permite buscar todas las mascotas
            volver_menu()
            
        elif opcion_veterinario =="5": #REALIZAR VISITAS
            ClasesVeterinario.Veterinario().realizar_visitas() # se llama el modulo Clasesveterinario y su clase Veterinario, que contiene el metodo realizar_visitas que se encarga de realizar visitas a las mascotas del veterinario
            volver_menu()
        elif opcion_veterinario =="6": # se llama el modulo ClasesVeterinario y su clase veterinario y posteriormente el metodo buscar_historia_clinica
            ClasesVeterinario.Veterinario().Buscar_historia_clinica()
            volver_menu()
        elif opcion_veterinario =="7": # si selecciona opcion 7 vuelve al menu
            menu()
    elif seleccion =="3":
        print("Hasta pronto :)")
        exit()
            
            
            
        
    
        
            
            
            

def volver_menu(): # funcion que se encarga de posibilitar volver al menu
    while True:
        volver= input("Deseas volver al menu si/no: ").lower()
        if volver != "si" and volver != "no":
            print("Error, ingresa si/no")
        else:
            break
    if volver == "si":
        menu()
    else:
        print("Ok, hasta pronto")
        exit()
menu()
