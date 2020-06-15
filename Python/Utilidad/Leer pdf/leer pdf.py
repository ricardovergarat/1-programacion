
from PyPDF2 import PdfFileReader # leer archivos pdf

def obtener_datos_pdf(nombre):
    with open(nombre,'rb') as archivo:
        contenido = PdfFileReader(archivo)
        n_paginas = contenido.getNumPages()
        x = 0
        datos = []
        while x != n_paginas:
            print("Pagina: ",x)
            pagina = contenido.getPage(x)
            texto = pagina.extractText()
            print(texto)
            datos.append(texto)
            x = x + 1
        return datos

if __name__ == '__main__':
    #path = '1_19925526-1.pdf'
    #text_extractor(path)
    estrucutura_pdf = obtener_datos_pdf("1_19925526-1.pdf")
    print(estrucutura_pdf)