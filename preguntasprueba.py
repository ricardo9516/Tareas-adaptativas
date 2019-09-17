import json
from random import randint
from io import open

temasU1=["union","interseccion","diferencia"]
tema_actual=0
rangosU1=[(1,2),(2,4),(4,6),(6,8),(8,12)]
aciertos=0
nivel=0
ruta="plantillaU1.json"

#Crear JSON
def crear_datos(ruta):
    contenido= open(ruta,"w")
    dct=[{"O1":1},{"P1":1},{"A":1},{"Usuario":1}]
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
    P1="Cual es la "
    P2=temasU1[tema]
    P3=" de "
    P4=" y "
    P5="?"
    modificar_datos(ruta,1,"P1",P1)
    modificar_datos(ruta,1,"P2",P2)
    modificar_datos(ruta,1,"P3",P3)
    modificar_datos(ruta,1,"P4",P4)
    modificar_datos(ruta,1,"P5",P5)


#Entradas de preguntas
def entradasU1():
    (low,high) = rangosU1[nivel]
    A=create(randint(low,high))
    B=create(randint(low,high)) 
    A=list(A)
    B=list(B)
    modificar_datos(ruta,0,"O1",A)
    modificar_datos(ruta,0,"O2",B)

#Visualizar entradas conjuntos
def mostrar_entradas_con(entrada):
    operador=ver_datos(ruta,0,entrada)
    operador=set(operador)
    return operador

#Visualizar las preguntas
def mostrar_preguntasU1():
    preguntas=["P1","P2","P3","P4","P5"]
    pregunta_final=[]
    for i in range(5):
        pregunta_final.append(ver_datos(ruta,1,preguntas[i]))
    print(pregunta_final[0]+pregunta_final[1]+pregunta_final[2]+str(mostrar_entradas_con("O1"))+pregunta_final[3]+str(mostrar_entradas_con("O2"))+pregunta_final[4])

#def resultado():
def respuestasU1(tema):
    (low,high) = rangosU1[nivel]
    R1=create(randint(low,high))
    R2=create(randint(low,high))
    R3=create(randint(low,high))
    R4=create(randint(low,high))
    respuestas=[R1,R2,R3,R4]
    O1=ver_datos(ruta,0,"O1")
    O2=ver_datos(ruta,0,"O2")
    O1=set(O1)
    O2=set(O2)
    respuesta_corrrecta=[(O1|O2),(O1&O2),(O1-O2)]
    rc=randint(0,3)
    respuestas[rc]=respuesta_corrrecta[tema]
    for i in range(4):
        if respuestas[i]==set():
            respuestas[i]="La interseccion es nula"
            print("Respuesta= "+ respuestas[i])
        else:
            respuestas[i]=list(respuestas[i])
    respuestas_JSON=["A","B","C","D"]
    for i in range(4):
        modificar_datos(ruta,2,respuestas_JSON[i],respuestas[i])
    return respuestas_JSON[rc]
    """#Visualizar en la consola
    print(respuestas)
    print("A= "+ str(O1))
    print("B= "+ str(O2))
    print("Respuesta= "+str(respuestas[rc]))"""

#Mostrar respuestas
def mostrar_respuestas():
    respuestas_JSON=["A","B","C","D"]
    inic_respuestas=["A= ","B= ","C= ","D= "]
    for i in range(4):
        respuesta=ver_datos(ruta,2,respuestas_JSON[i])
        respuesta=set(respuesta)
        print(inic_respuestas[i] + str(respuesta))

#Crear un nuevo usuario
def usuario():
    print("Ingrese su nombre: ")
    nombre=input()
    modificar_datos(ruta,3,"Usuario",nombre)

#Subir respuestas del usuario al JSON
def subir_resp(resp_usuario):
    if resp_usuario=="A" or resp_usuario=="B" or resp_usuario=="C" or resp_usuario=="D":
        resp_usuario=ver_datos(ruta,2,resp_usuario)
        modificar_datos(ruta,3,"Respuesta usuario",resp_usuario)

#Comparar respuesta del usuario con la respuesta correcta
def comp_resp(rc):
    acierto=0
    if ver_datos(ruta,3,"Respuesta usuario")==ver_datos(ruta,2,rc):
        acierto=1
    return acierto

#inicializar JSON
#crear_datos(ruta)



#Código principal

#usuario()
while (aciertos<3):
    entradasU1()
    respuestasU1(tema_actual)
    respuesta_correcta=respuestasU1(tema_actual)
    preguntasU1(tema_actual)
    mostrar_preguntasU1()
    mostrar_respuestas()
    print("Ingrese su respuesta: ")
    respuesta_usuario=input()
    subir_resp(respuesta_usuario)
    comp_resp(respuesta_correcta)
    if comp_resp(respuesta_correcta)==1:
        aciertos+=1
        modificar_datos(ruta,3,"Aciertos",aciertos)
        print("Correcto! \n")
    else:
        print("Incorrecto! \n")
print("Terminaste!")
