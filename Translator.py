from googletrans import Translator

def traductor():
    print("Bienvenido al traductor")

    #Pedimos al usuario la palabra o frase para traducir
    texto_a_traducir = input("Ingrese la palabra o frase a traducir:")

    #Pedimos al usuario el idioma de origen
    idioma_origen = input("Ingrese el idioma de origen:")

    #Pedimos al usuario el idioma de destino
    idioma_destino = input("Ingrese el idioma de destino:")

    #Creamos una instancia del traductor
    traductor = Translator()

    #Traducir el texto
    texto_traducido = traductor.translate(texto_a_traducir, src = idioma_origen, dest = idioma_destino)

    #Mostrar restultados por consola
    print(f"Texto Original ({idioma_origen}): {texto_a_traducir}")
    print(f"texto_a_traducido ({idioma_destino}): {texto_traducido.text}")

traductor()

