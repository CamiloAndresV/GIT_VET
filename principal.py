import bsd # modulo que contiene las listas generales
import pyfiglet 
import ClaseAdmin
import os

NEON_PINK = "\033[38;5;Magenta"
NEON_GREEN = "\033[38;5;82m"
NEON_YELLOW = "\033[38;5;11m"
NEON_ORANGE = "\033[38;5;202m"
NEON_BLUE = "\033[38;5;14m"
NEON_PURPLE = "\033[38;5;129m"
BROWN = "\033[38;5;94m"
RESET = "\033[0m"


def menu():
    import ClasesVeterinario
    nombre_veterinaria= pyfiglet.figlet_format(f"\tMASCOTA   FELIZ", font="Doom")
    perro1=(rf"""{NEON_BLUE}
            
     __ / \                                                           / \__
 ___/@      )                                                       (      @\___        
0           \                                                      /            O        
\_____)      \                                                    /       (____/        
        \  ____\                                                /_____  /
        {RESET}""")
    
    
    
    print(perro1) # se imprime los eslogan de las mascotas
    #print(nombre_veterinaria)
    print(f"{BROWN}{nombre_veterinaria}{RESET}")
    while True:
        seleccion = input(f"{NEON_ORANGE}\nINGRESAR COMO{RESET}\n1. Administrador\n2. Veterinario\n3. Salir \nDIGITA AQUI: ")
        if seleccion != "1" and seleccion != "2" and seleccion != "3":
            print("Error, ingresa una opcion correcta")
        else:
            break
    if seleccion =="1": # si selecciona administrador
        os.system('cls')
        
        print(f"""{NEON_ORANGE}OPCIONES ADMINISTRADOR{RESET}\n1. Registrar un veterinario\n2. Modificar información propietario\n3. Modificar información Veterinario\n4. Consultar mascotas de propietario\n5. Consultar mascotas veterinario\n6. Asignar Mascota a Veterinario\n7. buscar historia clinica de Mascota\n8. Volver Menu """)
        while True:
            opcion_admin= input(f"{BROWN}Ingresa la opcion: {RESET}")
            if opcion_admin not in ["1","2","3","4","5","6","7","8"]:
                print("Error opciones(1-8)")
            else:
                break
        if opcion_admin =="1": # modulo, clase y metodo que permite registrar un veterinario
            os.system('cls')
            ClaseAdmin.admin.registrar_vet() # llamar el modulo ClaseAdmin que contiene la clase Admin y el metodo (registrar_vet) que  llama el modulo ClaseVeterinario que contiene la clase veterinario y se llama el metodo registrar_Veterinario
            print(f"{NEON_YELLOW}Veterinario Registrado Exitosamente{RESET}")  
            volver_menu()
        elif opcion_admin == "2": # modulo, clase y metodo que permite actualizar datos de propietario
            os.system('cls')
            ClaseAdmin.admin.modificar_propietario()
            volver_menu()
            print(f"{NEON_YELLOW}Propieario modificado exitosamente{RESET}")  
        elif opcion_admin == "3":# modulo, clase y metodo que permite actualizar datos de Veterinario
            os.system('cls')
            ClaseAdmin.admin.modificar_veterinario()
            print(f"{NEON_YELLOW}Modificacion exitosas{RESET}")
            volver_menu()
        elif opcion_admin =="4":# modulo, clase y metodo que permite mostrar mascotas de propietario
            os.system('cls')
            ClaseAdmin.admin.consultar_mascotas_propietario()
            volver_menu()
        elif opcion_admin == "5": # modulo ClaseAdmin que contiene la clase admin y su metodo mostrar_mascotas_veterinarioo
            os.system('cls')
            ClaseAdmin.admin.mostrar_mascotas_veterinario()
            volver_menu()
        elif opcion_admin == "6":# modulo, clase y metodo que permite asignar mascotas
            os.system('cls')
            ClaseAdmin.admin.asignar()
            volver_menu()
        elif opcion_admin =="7": # modulo ClassVeterinario, clase Veterinario y metodo buscar_historia_clinica
            os.system('cls')
            ClasesVeterinario.Veterinario().Buscar_historia_clinica()
            volver_menu()
        elif opcion_admin == "8": # si selecciona 8 vuelve al menu
            os.system('cls')
            menu()
            
    elif seleccion == "2": #Si selecciona el Veterinario
        os.system('cls')
        print(f"\n{NEON_ORANGE}OPCIONES DE VETERINARIO{RESET}\n{NEON_BLUE}1.{RESET} Registrar Nueva mascota\n{NEON_BLUE}2.{RESET} Registrar Nuevo propietario\n{NEON_BLUE}3.{RESET} Buscar una Mascota en especifico\n{NEON_BLUE}4.{RESET} Buscar Mascotas\n{NEON_BLUE}5.{RESET} Realizar Visita\n{NEON_BLUE}6.{RESET} Buscar Historia Clinica Mascotas\n{NEON_BLUE}7.{RESET} Volver Menu")
        while True:
            opcion_veterinario= input(f"{BROWN}Ingresa la opcion:{RESET} ")
            if opcion_veterinario not in ["1", "2", "3","4","5","6","7"]: # 5 opciones que ejecutan lo que puede realizar el veterinario
                print("Error, opciones (1-7)")
            else:
                break
        # METODOS DE VETERINARIO
        if opcion_veterinario == "1": # si la opcion es 1, Registra la mascota
            os.system('cls')
            print(f"\t\n REGISTRAR MASCOTA\n")
            ClasesVeterinario.Veterinario().registrar_mascota() # se llama el modulo ClasesVterinario, la clase Veterinario y () porque esa clase recibe atributos, y posteriormente se llama el metodo que permite registrar una mascota
            volver_menu()
        elif opcion_veterinario =="2": # si la opcion es 2, registra el veterinario
            os.system('cls')
            print(f"\t\n REGISTRAR VETERINARIO\n")
            ClasesVeterinario.Veterinario().registrar_propietario() # Se llama el modulo CLasesVeterinario, la clase Veterinario con () ya que la clase contiene atributos, ademas se llama el metodo que permite registrar un propietario
            volver_menu()
        elif opcion_veterinario =="3": # si la opcion es 3, busca una mascota en especifico
            os.system('cls')
            print("\nBUSCAR MASCOTA\n")
            ClasesVeterinario.Veterinario().buscar_mascota() # se llama el modulo ClasesVterinario, la clase Veterinario con () ya que esta clase recibe atributos, posteriormente el metodo que permite buscar una mascota en especifico
            volver_menu()
        elif opcion_veterinario == "4": # si la opcion es 4, busca todas las mascotas
            os.system('cls')
            print("\nBUSCAR MASCOTAS\n")
            ClasesVeterinario.Veterinario().buscar_mascotas() # se llama el modulo ClasesVterinario, la clase Veterinario con () ya que esta clase recibe atributos, posteriormente el metodo que permite buscar todas las mascotas
            volver_menu()
            
        elif opcion_veterinario =="5": #REALIZAR VISITAS
            os.system('cls')
            ClasesVeterinario.Veterinario().realizar_visitas() # se llama el modulo Clasesveterinario y su clase Veterinario, que contiene el metodo realizar_visitas que se encarga de realizar visitas a las mascotas del veterinario
            volver_menu()
        elif opcion_veterinario =="6": # se llama el modulo ClasesVeterinario y su clase veterinario y posteriormente el metodo buscar_historia_clinica
            os.system('cls')
            ClasesVeterinario.Veterinario().Buscar_historia_clinica()
            volver_menu()
        elif opcion_veterinario =="7": # si selecciona opcion 7 vuelve al menu
            os.system('cls')
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
