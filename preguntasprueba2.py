import json
from random import randint

tema=['union','interseccion','diferencia']
rangos=[(1,2),(2,4),(4,6),(6,8),(8,10)]
rc=0
ri=0
nivel=1

for nivel in range(len(rangos)):
    (low,high) =rangos[nivel]


def create(count):
    S=set()
    while len(S) < count:
        S.add(randint(0,9))
    return S

#Falta función para respuestas
def respi():
    A=create(rangos(nivel))
    B=create(rangos(nivel))
    C=create(rangos(nivel))
    D=create(rangos(nivel))


#Json para la Unidad 1
U1={}
U1=[{#Temas de la unidad
    'Tema1': 'Union',
    'Tema2': 'Interseccion',
    'Tema3': 'Diferencia'
},
{#Operadores de las preguntas
    'Operador1': '1',
    'Operador2': '1'
},
{#Respuestas
    'A': '1',
    'B': '1',
    'C': '1',
    'D': '1'
},
{#Aciertos y errores
    'Aciertos': rc,
    'Errores': ri       
},
{#Rangos para dificultad
    'Rango1': rangos[1],
    'Rango2': rangos[2],
    'Rango3': rangos[3],
    'Rango4': rangos[4],
    'Rango5': rangos[5]
}]
with open('U1.txt', 'w') as outfile:
    json.dump(U1, outfile)
    
with open('U1.txt','r') as json_file:
    unidad1 = json.load(json_file)
