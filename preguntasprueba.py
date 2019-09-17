import json
from random import randint
from io import open

temasU1=["union","interseccion","diferencia"]
rangosU1=[(1,2),(2,4),(4,6),(6,8),(8,12)]
aciertos=0
nivel=0
ruta="plantillaU1.json"

#Crear JSON
def crear_datos(ruta):
    contenido= open(ruta,"w")
    dct=[{"A":1},{"P1":1},{"R1":1},{"Usuario":1}]
    json_str = contenido.write(json.dumps(dct, indent=True))

#Visualizar datos JSON para crear variables
def ver_datos(ruta,indice,ubicacion):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    return plantilla[indice][ubicacion]

#Creador de conjuntos
def create(count):
    S=set()
    while len(S) < count:
        S.add(randint(1,20))
    return S

#Función para modificar datos del JSON
def modificar_datos(ruta,indice,ubicacion,cambio):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    plantilla[indice][ubicacion]=cambio
    contenido= open(ruta,"w")
    json.dump(plantilla,contenido,indent=True)

#Preguntas U1
def preguntasU1(tema):
    P1="Cual es la"
    P2=temasU1[tema]
    P3="de"
    P4="y"
    P5="?"
    modificar_datos(ruta,1,"P1",P1)
    modificar_datos(ruta,1,"P2",P2)
    modificar_datos(ruta,1,"P3",P3)
    modificar_datos(ruta,1,"P4",P4)
    modificar_datos(ruta,1,"P5",P5)

#def mostrar_preguntasU1():

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
def respuestasU1(tema):
    (low,high) = rangosU1[nivel]
    R1=create(randint(low,high))
    R2=create(randint(low,high))
    R3=create(randint(low,high))
    R4=create(randint(low,high))
    respuestas=[R1,R2,R3,R4]
    A=ver_datos(ruta,0,"A")
    B=ver_datos(ruta,0,"B")
    A=set(A)
    B=set(B)
    respuesta_corrrecta=[(A|B),(A&B),(A-B)]
    rc=randint(0,3)
    respuestas[rc]=respuesta_corrrecta[tema]
    for i in range(4):
        if respuestas[i]==set():
            respuestas[i]="La interseccion es nula"
            print("Respuesta= "+ respuestas[i])
        else:
            respuestas[i]=list(respuestas[i])
    respuestas_JSON=["R1","R2","R3","R4"]
    for i in range(4):
        modificar_datos(ruta,2,respuestas_JSON[i],respuestas[i])
    """#Visualizar en la consola
    print(respuestas)
    print("A= "+ str(A))
    print("B= "+ str(B))
    print("Respuesta= "+str(respuestas[rc]))"""

#Mostrar respuestas
def mostrar_respuestas():
    respuestas_JSON=["R1","R2","R3","R4"]
    inic_respuestas=["A= ","B= ","C= ","D= "]
    for i in range(4):
        respuesta=ver_datos(ruta,2,respuestas_JSON[i])
        respuesta=set(respuesta)
        print(inic_respuestas[i] + str(respuesta))


def usuario():
    print("Ingrese su nombre: ")
    nombre=input()
    print("nombre")
    modificar_datos(ruta,3,"Usuario",nombre)


#inicializar JSON
#crear_datos(ruta)



#Código principal

#usuario()
entradasU1()
respuestasU1(0)
preguntasU1(0)
mostrar_respuestas()
