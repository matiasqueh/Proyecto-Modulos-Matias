# estadisticas.py
def media(datos):
    media_aritmetica = sum(datos) / len(datos)
    return media_aritmetica


if __name__ == '__main__':
    notas = [100,50,100,70,100]
    print(media(notas))
    