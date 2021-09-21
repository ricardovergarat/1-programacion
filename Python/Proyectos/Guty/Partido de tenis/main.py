import random
import os

def preparar_juego(puntos_deseados_jugador_1,puntos_deseados_jugador_2):
    registro_jugador_1 = []
    registro_jugador_2 = []
    puntos_jugador_1 = obtener_cantidad_puntos(registro_jugador_1)
    puntos_jugador_2 = obtener_cantidad_puntos(registro_jugador_2)
    turno = 1
    #print("queremos el marcador: ",puntos_deseados_jugador_1," - ",puntos_deseados_jugador_2)
    while True:
        if ( (puntos_jugador_1 == puntos_deseados_jugador_1) and (puntos_jugador_2 == puntos_deseados_jugador_2) ):
            return registro_jugador_1,registro_jugador_2
        else:
            if (puntos_jugador_1 == puntos_deseados_jugador_1) or (puntos_jugador_2 == puntos_deseados_jugador_2):
                if puntos_jugador_1 == puntos_deseados_jugador_1:
                    #print("debe ganar el jugador 2")
                    registro_jugador_1.append("P")
                    registro_jugador_2.append("G")
                else:
                    # implica que fue el jugador dos el que obtuvo los puntos deseados
                    #print("debe ganar el jugador 2")
                    registro_jugador_1.append("G")
                    registro_jugador_2.append("P")
            else:
                gandor_del_punto = obtener_punto()
                if gandor_del_punto == 1:
                    registro_jugador_1.append("G")
                    registro_jugador_2.append("P")
                else:
                    registro_jugador_1.append("P")
                    registro_jugador_2.append("G")
            puntos_jugador_1 = obtener_cantidad_puntos(registro_jugador_1)
            puntos_jugador_2 = obtener_cantidad_puntos(registro_jugador_2)
            #print("turno: ", turno, " marcador --> ", puntos_jugador_1, " - ", puntos_jugador_2)
            turno = turno + 1

def obtener_cantidad_puntos(registro_jugador):
    puntaje = 0
    for i in range(len(registro_jugador)):
        if registro_jugador[i] == "G":
            puntaje = puntaje + 1
    return puntaje

def obtener_punto():
    ganador_del_punto = random.randint(1,2)
    return ganador_del_punto

def que_gane_el_mejor(registro_jugador_1,registro_jugador_2,punto_para_ganar):
    puntos_jugador_1 = obtener_cantidad_puntos(registro_jugador_1)
    puntos_jugador_2 = obtener_cantidad_puntos(registro_jugador_2)
    while (puntos_jugador_1 != punto_para_ganar) and (puntos_jugador_2 != punto_para_ganar):
        punto_jugador = obtener_punto()
        if punto_jugador == 1:
            registro_jugador_1.append("G")
            registro_jugador_2.append("P")
        else:
            registro_jugador_1.append("P")
            registro_jugador_2.append("G")
        #print(registro_jugador_1)
        #print(registro_jugador_2)
        puntos_jugador_1 = obtener_cantidad_puntos(registro_jugador_1)
        puntos_jugador_2 = obtener_cantidad_puntos(registro_jugador_2)
    #print(registro_jugador_1)
    #print(registro_jugador_2)
    return registro_jugador_1,registro_jugador_2

if __name__ == '__main__':
    os.system("cls")
    uno,dos = preparar_juego(8,7)
    print("juego preparado")
    print(uno," puntos: ",obtener_cantidad_puntos(uno))
    print(dos," puntos: ",obtener_cantidad_puntos(dos))
    uno,dos = que_gane_el_mejor(uno,dos,10)
    print(uno, " puntos: ", obtener_cantidad_puntos(uno))
    print(dos, " puntos: ", obtener_cantidad_puntos(dos))




