import json
from random import randint
from io import open

ruta="plantillaU1.json"
ruta2="usuarios.json"

#Crear JSON
def crear_datos(ruta):
    contenido= open(ruta,"w")
    dct=[{"O1":1},{"P1":1},{"A":1},{"Respuesta usuario":1},{"rangosU1":[(1,2),(2,4),(4,6),(6,8),(8,12)]}]
    json_str = contenido.write(json.dumps(dct, indent=True))

#Visualizar datos JSON para crear variables
def ver_datos(ruta,indice,ubicacion):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    return plantilla[indice][ubicacion]

#Función para modificar datos del JSON
def modificar_datos(ruta,indice,ubicacion,cambio):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    plantilla[indice][ubicacion]=cambio
    contenido= open(ruta,"w")
    json.dump(plantilla,contenido,indent=True)

#Crea usuarios y mantiene los ya existentes
def crear_usuario(ruta):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    size=len(plantilla)
    usuario=input('Cual es su nombre?\n')
    nuevo_usuario={'usuario'+str(size+1): [{'Nombre':usuario}]}
    plantilla.append(nuevo_usuario)
    usu_exis=0
    for i in range(size):
        if usu_exis==0:
            usuario_registrado=busc_us(ruta,i,'usuario'+str(i+1),0,'Nombre')
        if usuario_registrado==usuario:
            print('Bienvenido '+usuario)
            usu_exis=1
            usuario_actual='usuario'+str(i+1)
            indice=i
            break
    if usu_exis==0:
        usuario_actual='usuario'+str(size+1)
        indice=size
        contenido= open(ruta,"w")
        contenido.write(json.dumps(plantilla,indent=True))
        contenido.close()
        #Aquí se agregan los temas
        temas_U1("usuarios.json",size,'usuario'+str(size+1))     
        print("Registro exitoso!")
    return indice,usuario_actual

#Buscar usuario
def busc_us(ruta,indice,ubicacion,indice2,ubicacion2):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    return plantilla[indice][ubicacion][indice2][ubicacion2]

#Agregar temas de la U1
def temas_U1(ruta,indice,usuario):
    contenido= open(ruta,"r")
    plantilla= json.load(contenido)
    plantilla[indice][usuario][0]['U1']=[{'nombre':'union','aciertos':0,'nivel':1},
    {'nombre':'interseccion','aciertos':0,'nivel':1},
    {'nombre':'diferencia','aciertos':0,'nivel':1}]
    contenido= open(ruta,"w")
    json.dump(plantilla,contenido,indent=True)
    print('Se agrego la Unidad 1')
    
#buscar tema
def buscar_tema(ruta,indice_u,ubicacion_u,ubicacion_unidad,indice_t,ubicacion_t):
    contenido= open(ruta,"r")
    plantilla= json.load(contenido)
    return plantilla[indice_u][ubicacion_u][0][ubicacion_unidad][indice_t][ubicacion_t]

#buscar unidad
def buscar_unidad(ruta,indice_u,ubicacion_u,ubicacion_unidad):
    contenido= open(ruta,"r")
    plantilla= json.load(contenido)
    return plantilla[indice_u][ubicacion_u][0][ubicacion_unidad]

#Escoger tema
def esc_tema(ruta,indice,usuario):
    t=0
    print('Ingrese la unidad:')
    while(t==0):
        unidad=input('U1=Conjuntos U2=Cambio de base\n')
        if unidad=='U1' or unidad=='U2':
            while (t==0):
                #Visualizacion de temas en consola
                print('Ingrese el nombre del tema: ')
                for i in range(len(buscar_unidad(ruta,indice,usuario,unidad))):
                    print(buscar_tema(ruta2,indice_usuario,usuario_actual,unidad,i,'nombre')+' = '+'Tema'+str(i+1))
                #Guardar el tema actual en caso de que sea uno existente
                tema_actual=input()
                for i in range(len(buscar_unidad(ruta,indice,usuario,unidad))):
                    if tema_actual==buscar_tema(ruta2,indice_usuario,usuario_actual,unidad,i,'nombre'):
                        print('Bienvenido al tema: '+tema_actual)
                        t=1
                        indice_tema=i
                        break
        else:
            print('Ingrese una unidad disponible por favor: ')
    return indice_tema,unidad

#Creador de conjuntos
def create(count):
    S=set()
    while len(S) < count:
        S.add(randint(1,20))
    return S

#Preguntas U1
def preguntasU1(ru,indice_u,ubicacion_u,ubicacion_unidad,indice_t):
    P1="Cual es la "
    P2=buscar_tema(ru,indice_u,ubicacion_u,ubicacion_unidad,indice_t,'nombre')
    P3=" de "
    P4=" y "
    P5="?"
    modificar_datos(ruta,1,"P1",P1)
    modificar_datos(ruta,1,"P2",P2)
    modificar_datos(ruta,1,"P3",P3)
    modificar_datos(ruta,1,"P4",P4)
    modificar_datos(ruta,1,"P5",P5)

#Entradas de preguntas
def entradasU1(ru,indice_u,ubicacion_u,ubicacion_unidad,indice_t):
    (low,high) = ver_datos(ruta,4,'rangosU1')[buscar_tema(ru,indice_u,ubicacion_u,ubicacion_unidad,indice_t,'nivel')]
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
def respuestasU1(tema,nivel):
    (low,high) = ver_datos(ruta,4,'rangosU1')[nivel]
    R1=create(randint(low,high))
    R2=create(randint(low,high))
    R3=create(randint(low,high))
    R4=create(randint(low,high))
    respuestas=[R1,R2,R3,R4]
    O1=ver_datos(ruta,0,"O1")
    O2=ver_datos(ruta,0,"O2")
    O1=set(O1)
    O2=set(O2)
    respuesta_correcta=[(O1|O2),(O1&O2),(O1-O2)]
    rc=randint(0,3)
    respuestas[rc]=respuesta_correcta[tema]
    for i in range(4):
        if respuestas[i]==set():
            respuestas[i]="La interseccion es nula"
        else:
            respuestas[i]=list(respuestas[i])
    respuestas_JSON=["A","B","C","D"]
    for i in range(4):
        modificar_datos(ruta,2,respuestas_JSON[i],respuestas[i])
    return respuestas_JSON[rc]


#Mostrar respuestas
def mostrar_respuestas():
    respuestas_JSON=["A","B","C","D"]
    inic_respuestas=["A= ","B= ","C= ","D= "]
    for i in range(4):
        respuesta=ver_datos(ruta,2,respuestas_JSON[i])
        if type(respuesta)==list:
            respuesta=set(respuesta)
            print(inic_respuestas[i] + str(respuesta))
        else:
            print(inic_respuestas[i] + str(respuesta))

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

def aumentar_aciertos(ruta,indice_u,ubicacion_u,ubicacion_unidad,indice_t,ubicacion_t,cambio):
    contenido= open(ruta,"r")
    plantilla = json.load(contenido)
    plantilla[indice_u][ubicacion_u][0][ubicacion_unidad][indice_t][ubicacion_t]=cambio
    contenido= open(ruta,"w")
    json.dump(plantilla,contenido,indent=True)

#Sistema de preguntas infinitas
def preguntas_usuario(indice_usuario,usuario_actual,unidad,indice_tema):
    nivel=buscar_tema(ruta2,indice_usuario,usuario_actual,unidad,indice_tema,'nivel')
    print('Empezemos con el nivel '+str(nivel))
    while (buscar_tema(ruta2,indice_usuario,usuario_actual,unidad,indice_tema,'aciertos')<5):
        entradasU1(ruta2,indice_usuario,usuario_actual,unidad,indice_tema)
        respuestasU1(indice_tema,nivel)
        respuesta_correcta=respuestasU1(indice_tema,nivel)
        preguntasU1(ruta2,indice_usuario,usuario_actual,unidad,indice_tema)
        mostrar_preguntasU1()
        mostrar_respuestas()
        print("Ingrese su respuesta: ")
        respuesta_usuario=input()
        subir_resp(respuesta_usuario)
        comp_resp(respuesta_correcta)
        if comp_resp(respuesta_correcta)==1:
            aciertos=buscar_tema(ruta2,indice_usuario,usuario_actual,unidad,indice_tema,'aciertos')
            aciertos+=1
            aumentar_aciertos(ruta2,indice_usuario,usuario_actual,unidad,indice_tema,'aciertos',aciertos)
            print("Correcto! \n")
        else:
            print("Incorrecto! \n")
    print("Terminaste!")

#Código principal

#inicializar JSON U1
#crear_datos(ruta)

#Crear usuario y empezar curso
(indice_usuario,usuario_actual)=(crear_usuario(ruta2))
(indice_tema,unidad)=esc_tema(ruta2,indice_usuario,usuario_actual)
preguntas_usuario(indice_usuario,usuario_actual,unidad,indice_tema)
