import json
from random import randint
from io import open

temasU1=['union','interseccion','diferencia']
rangosU1=[(1,2),(2,4),(4,6),(6,8),(8,12)]
aciertos=0
nivel=1
ruta="plantillaU1.json"

#Crear JSON
def crear_datos(ruta):
    contenido= open(ruta,"w")
    dct=[{"A":1},{"P1":1},{"Respuestas":1}]
    json_str = contenido.write(json.dumps(dct, indent=True))

#Creador de conjuntos
def create(count):
    S=set()
    while len(S) < count:
        S.add(randint(0,20))
    return S

#Función para modificar datos del JSON
def modificar_datos(ruta,indice,ubicacion,cambio):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    plantilla[indice][ubicacion]=cambio
    contenido= open(ruta,"w")
    json.dump(plantilla,contenido,indent=True)

#Entradas de preguntas
def entradasU1():
    (low,high) = rangosU1[nivel]
    A=create(randint(low,high))
    B=create(randint(low,high)) 
    A=list(A)
    B=list(B)
    modificar_datos(ruta,0,"A",A)
    modificar_datos(ruta,0,"B",B)

#def resultado():
def respuestas():
    (low,high) = rangosU1[nivel]
    R1=create(randint(low,high))
    R2=create(randint(low,high))
    R3=create(randint(low,high))
    R4=create(randint(low,high))
    respuestas=[R1,R2,R3,R4]
    print(respuestas)



#Preguntas U1
def preguntasU1():
    P1="Cual es la"
    P2=temasU1
    P3="de"
    P4="y"
    P5="?"
    modificar_datos(ruta,1,"P1",P1)
    modificar_datos(ruta,1,"P2",P2)
    modificar_datos(ruta,1,"P3",P3)
    modificar_datos(ruta,1,"P4",P4)
    modificar_datos(ruta,1,"P5",P5)





crear_datos(ruta)
respuestas()

"""
#Código principal
for nivel in range(len(rangosU1)):
    (low,high) = rangosU1[nivel]
    ResultadoU=A|B
    ResultadoI=A&B
    ResultadoD=A-B
    if ResultadoI==set():
        ResultadoI="es nula"
    print("El nivel actual es: "+ str(nivel))
    print(A)
    print(B)
    print("Unión "+ str(ResultadoU))
    print("Intersección "+ str(ResultadoI))
    print("Diferencia "+ str(ResultadoD))
"""


