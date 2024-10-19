# modulo que contiene las listas generales
#listas que almacenaran los ides de la mascota, propietario, veterinario

ides_veterinarios=["1212121212"]
ides_propietarios=["1313131313"]
ides_mascotas=["1212", "1313"]
ides_visitas=["13133"]
#listas generales que almacenaran las informaciones de los actores

visita={ # diccionario que almacena todos los datos de visita
                    "Id Visita": "13133",
                    "Temperatura":"13",
                    "Peso":"3",
                    "Frecuencia Respiratoria": "32",
                    "Frecuencia Cardiaca": "13",
                    "Estado de Animo": "bien",
                    "ID veterinario": "13131313", # id del veterinario que le realiza la visita
                    "Recomendaciones": "biem",
                    "Fecha Visita": "1313/13"
                }
diccionario_mascota={
    "Id":"1212",
    "Nombre": "pepe",
    "Color": "2e",
    "Especie":"gato",
    "Raza":"angora",
    "Veterinario":"32323",
    "Historia Clinica":["13133"]
}
diccionario_mascota1={
    "Id":"1313",
    "Nombre": "pepe",
    "Color": "negro",
    "Especie":"gato",
    "Raza":"angora",
    "Veterinario":"32323",
    "Historia Clinica":["43333","313"]
}
diccionario={
            "Id":"1212121212",
            "Nombres":"junior",
            "Apellidos":"Herrera",
            "Direccion":"Salgar",
            "Telefono":"1231131313",
            "Tarjeta profesional":"121212scxs",
            "Mascotas":["1212"]
        }


diccionario_propietario={
    "Id":"1313131313",
    "Nombre":"peddro",
    "Apellidos":"herrera",
    "Direccion":"algae",
    "Telefono":"1313131",
    "Correo":"qedas",
    "Mascotas":["12123"]
}
lista_veterinarios =[diccionario]
lista_mascota=[diccionario_mascota,diccionario_mascota1]
lista_propietario =[diccionario_propietario]
lista_visitas=[visita]