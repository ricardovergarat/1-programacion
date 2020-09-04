'''
Manuel Castro
Jose Martinez
Manuel Montecino
Robinson Donoso
'''


import requests
import json
import unicodedata
import networkx as nx
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt
import csv

import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

# se Importan las Librerias a Usar


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')

def descargarcsv(values,apiKey):
    response = requests.get('https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.json/?auth_key='+apiKey)
    if response.status_code==200:
        s=json.loads(response.text,encoding='utf8',strict=False)
        data=pd.DataFrame(s['data'],columns=s['headers'])
        lowercase = lambda x: str(x).lower().replace(' ', '_')
        data.rename(lowercase, axis="columns", inplace=True)
        data.rename(strip_accents, axis="columns", inplace=True)
        data.rename(columns={
            'latitud':'lat',
            'longitud':'lon',
            'gasolina_93_$/l':'gasolina_93',
            'gasolina_95_$/l':'gasolina_95',
            'gasolina_97_$/l':'gasolina_97',
            'petroleo_diesel_$/l':'petroleo_diesel'},inplace=True)
        data.set_index('id',inplace=True)
        data['ultima_actualizacion']=pd.to_datetime(data['ultima_actualizacion'],infer_datetime_format=True)
        for v in values:
            data[v] = pd.to_numeric(data[v], errors='coerce')
        data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
        data['lon'] = pd.to_numeric(data['lon'], errors='coerce')
        data['region'] = data['region'].astype('category')
        data['id_region'] = data['id_region'].astype('category')
        data.dropna(how="any",inplace=True)
        data.to_csv('precios_bencinas.csv')
    else:
        print("error")

#funcion que solo lee el archivo CSV donde estan los datos.
def LeerArchivo(a, l, e):
    with open(a, encoding=e) as File:
        reader = csv.DictReader(File)
        for row in reader:
            l.append(row)
            #largo = len(l)
            #print(largo)

#funcion obtiene los datos solo de la region establecida y los guarda en una lista
def ObtenerDatosRegion( a, l1,l2 ):
    for i in l1:
        if ( i['id_region'] == a):
            l2.append(i)
    #print('las bencineras de la region son: ', len(l2))


#funcion calcula las distancias entre 2 cordenadas.
def haversine (lat1, lon1,lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2* asin(sqrt(a))
    r = 6371.*1000
    return c *r

def dibujarGrafo(a): #funcion que dubuja un grafo, recive un grafo nx
    pos=nx.get_node_attributes(G,'pos')
    #nx.draw(a, nx.get_node_attributes(a, 'pos'), with_labels=True)
    nx.draw(a,pos,with_labels=True)
    plt.show()


def dibujarArboldeExpansion(a): # funcion dibuja el arbol de expansion del Grafo
    t = nx.Graph()
    t= nx.minimum_spanning_tree(a)
    pos= nx.get_node_attributes(t,'pos')
    name = nx.get_node_attributes(t,'name')
    #print(name)
    nx.draw(a,pos,with_labels=True)
    plt.show()

def escribirArchivos(data): # funcion que crea un archivo correspondiente a la region seleccionada.
    with open('region.csv', 'w') as csvfile:
        fieldValues=['id','ultima_actualizacion','razon_social','calle','numero','id_comuna','comuna','id_region','region','horario_de_atencion',
        'distribuidor','distribuidor_logo','distribuidor_logo_svg','distribuidor_logo_svg_horizontal','gasolina_93','gasolina_97','petroleo_diesel','gasolina_95',
        'glp_vehicular_$/m3','gnc_$/m3','lat','lon','tienda','farmacia','mantencion','autoservicio','pago_efectivo','cheque','tarjetas_bancarias','tarjeta_grandes_tiendas']
        writer = csv.DictWriter(csvfile, fieldnames=fieldValues)
        writer.writeheader()
        writer.writerows(data)

def obtenerArbolExpansionMinimo(a): # funcion recibe un grafo, devuelve un arbol de expansion minimo
    t = nx.Graph()
    t = nx.minimum_spanning_tree(a)
    return t

def ListaCordenadas(a): #funcion que crea una lista con las cordenadas del grafo
    l = []
    lpos = nx.get_node_attributes(a,'pos')
    for x in lpos:
        l.append(lpos[x])
    return l

def obtenerCordenadaNodo(c, i): # funcion que obtiene la cordenda de un nodo, necesita el drataframe, numero del nodo y devuelve un string
    a = "["+c.iat[i,0]+","+c.iat[i,1]+"]"
    return str(a)

def CrearListaInicioFin(a,b):
    l =[]
    l.append(a)
    l.append(b)
    return l

def posicionesGrafo(l):
    lista1=[]
    for x in range(0,len(l)):
        for y in range(0,len(l)):
            if x!=y:
                lista1.append([float(l[x][0]),float(l[x][1]),float(l[y][0]),float(l[y][1])])
    pandas=pd.DataFrame(lista1,columns=["lat1","lon1","lat2","lon2"])
    return pandas


if __name__ == "__main__":
    api_key='02f23d8e1dd050539725ce70b158e81bf6416cec'
    val=['gasolina_93','gasolina_97','gasolina_95','petroleo_diesel']
    descargarcsv(val,api_key)
    region = [] # se crea una lista con las bencineras correspondiente a la Region
    listaPrincipal =[]
    LeerArchivo('precios_bencinas.csv', listaPrincipal, "utf8")
    
    ObtenerDatosRegion('10',listaPrincipal, region)
    #print(len(region))
    #print(len(listaPrincipal))
    contador =0

    #creamos el Grafo a Usar
    G = nx.Graph()
    for x in range(0,len(region)):
        for y in range(0,len(region)):
            distancia = (haversine(float(region[x]['lat']),float(region[x]['lon']),float(region[y]['lat']),float(region[y]['lon'])))
            if distancia > 0:
                G.add_node(x, pos=(region[x]['lat'],region[x]['lon']),name = region[x]['distribuidor'],lat = region[x]['lat'], lon =region[x]['lon'] )
                G.add_node(y, pos=(region[y]['lat'],region[y]['lon']), name = region[y]['distribuidor'],lat = region[y]['lat'], lon =region[y]['lon'] )
                G.add_edge(x,y)
                G[x][y]['weight'] = distancia
                #print("peso arbol:", G[x][y]['weight'])

                #print('distancia entre: ', region[x]['razon_social'], 'y :', region[y]['razon_social'], 'es: ', distancia, '\n')
                #contador = contador+1
    #print (contador-93)

#dibujarGrafo(G)
#dibujarArboldeExpansion(G)
lista_X = []

t = obtenerArbolExpansionMinimo(G)

CordenadasGrafo = pd.DataFrame(data = ListaCordenadas(G), columns=["lat","lon"]) #DataFrame Cordenadas

CordenadasArbol = pd.DataFrame(data= ListaCordenadas(t), columns=["lat","lon"]) #DataFrame Cordenadas Arbol Expansion

recorridoArbol = pd.DataFrame(data= t.edges(), columns=["inicio","fin"])

caminos2 =[]
for z in range(0, len(recorridoArbol)):

    x2 = float(CordenadasGrafo.iat[recorridoArbol.iat[z,0],1])
    x3 = float(CordenadasGrafo.iat[recorridoArbol.iat[z,0],0])
    x5 = float (CordenadasGrafo.iat[recorridoArbol.iat[z,1],1])
    x6 = float (CordenadasGrafo.iat[recorridoArbol.iat[z,1],0])
    caminos2.append( [float(x2), float(x3) ,float (x5),float (x6) ])
    #caminos2.append( [ [float(CordenadasGrafo.iat[recorridoArbol.iat[z,0],1]), float(CordenadasGrafo.iat[recorridoArbol.iat[z,0],0])] ,[float (CordenadasGrafo.iat[recorridoArbol.iat[z,1],1]),float (CordenadasGrafo.iat[recorridoArbol.iat[z,1],0])] ] )

extremos =nx.get_node_attributes(G,'pos')
for XZ in extremos:
    lista_X.append(extremos[XZ])
grafo=posicionesGrafo(lista_X)


path = pd.DataFrame(data=caminos2, columns=['x1','y1' , 'x2','y2'])


escribirArchivos(region)

nodos = []
nodos = nx.get_node_attributes(G,'pos')

nn = pd.DataFrame(nodos, columns=['lat'])

dato = pd.read_csv('region.csv', encoding="latin1")
df = (dato)
df = df.fillna(0) # elimina los nan

st.title("Grafo y Arbol region 10")
st.markdown("Grafo")

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=-41.46852167033, longitude=-72.960548400879, zoom=8, pitch=40,
        ),
        layers=[ 

            pdk.Layer(
                "HexagonLayer",
                df,
                get_position="[lon, lat]",
                radius=300,
                elevation_scale=40,
                elevation_range=[200, 1000],
                pickable=True,
                extruded=True,
            ),
            
            
            pdk.Layer(
                "LineLayer",
                data=grafo,
                get_source_position=['lon1','lat1'],
                get_target_position=['lon2','lat2'],
                get_color=[132,56,71],
                get_width=1,
                highlight_color=[255, 255, 0],
                picking_radius=10,
                auto_highlight=True,
                pickable=True,
                )
            
        ],
        
    )
)

st.markdown("Arbol de Expansion Minimo")

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=-41.46852167033, longitude=-72.960548400879, zoom=8, pitch=40,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                df,
                get_position="[lon, lat]",
                radius=300,
                elevation_scale=40,
                elevation_range=[200, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
            "LineLayer",
            data=path,
            get_source_position=['x1','y1'],
            get_target_position=['x2','y2'],
            get_color=[132,56,71],
            get_width=10,
            highlight_color=[255, 255, 0],
            picking_radius=10,
            auto_highlight=True,
            pickable=True,
            ),   
        ],
    )
)