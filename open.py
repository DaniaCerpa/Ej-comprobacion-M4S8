def guardar_informacion(archivo:str, formato:str):
    """Crea un nuevo archivo con el nombre y formato especificados, escribiendo líneas de información. 
        Si el archivo ya existe, se captura una excepción FileExistsError y se informa al usuario.
        
    Args:
        archivo: nombre del archivo a crear\n
        formato: formato del archivo a crear
    """
    try:
        ruta = "./archivos/"
        nom_archivo = f"{archivo}.{formato}"
        path = ruta + nom_archivo
        
        with open(path, "x") as nuevo_archivo:
        
            i=1
            while i<=5:
                nuevo_archivo.write(f"Datos de información en la línea {i}\n")
                i+=1
         
    except FileExistsError:
        print(f"No es posible crear el archivo {archivo}.{formato} porque ya existe uno previo con este nombre.\nPorfavor intenta con otro nombre")

    
    
def main():
    """Función principal del programa que entrega los parametros necesarios para la posterior ejecución de la función guadar_informacio().
    """
    nombre_archivo = "informacion"
    formato = "dat"    
    
    guardar_informacion(nombre_archivo, formato)

#Ejecución de la funcion para correr el programa
main()