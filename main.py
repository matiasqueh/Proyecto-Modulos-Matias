# Proyecto: [Nombre del Proyecto]
# Estudiante: [Nombre del Estudiante]
# Fecha de Inicio: [dd/mm/aaaa]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

def media(datos):
    media_aritmetica = sum(datos) / len(datos)
    return media_aritmetica

def mediana(datos):
    
    datos = sorted(datos)
    n = len(datos)
    mitad = n // 2
    if n % 2 == 0:
        mediana ((datos[mitad -1]+ datos[mitad])/2)
    else:
        mediana = datos[mitad]
    return mediana

if __name__== '__main__':
    notas = [100,50,100,78,100]
    print (mediana(notas))