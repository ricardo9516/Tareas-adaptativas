import json
import random

def A1(start1, end1, num1): 
    res = [] 
    for j in range(num1): 
        res.append(random.randint(start1, end1)) 
    return res
num1 = 2
start1 = 0
end1 = 9

def B1(start2, end2, num2): 
    res = [] 
    for j in range(num2): 
        res.append(random.randint(start2, end2)) 
    return res
num2 = 3
start2 = 0
end2 = 9

def R1(start3, end3, num3): 
    res = [] 
    for j in range(num3): 
        res.append(random.randint(start3, end3)) 
    return res
num3 = random.randint(1,5)
start3 = 0
end3 = 9

def R2(start4, end4, num4): 
    res = [] 
    for j in range(num4): 
        res.append(random.randint(start4, end4)) 
    return res
num4 = random.randint(1,5)
start4 = 0
end4 = 9

def R3(start5, end5, num5): 
    res = [] 
    for j in range(num5): 
        res.append(random.randint(start5, end5)) 
    return res
num5 = random.randint(1,5)
start5 = 0
end5 = 9

def R4(start6, end6, num6): 
    res = [] 
    for j in range(num6): 
        res.append(random.randint(start6, end6)) 
    return res
num6 = random.randint(1,5)
start6 = 0
end6 = 9

score=0
A=A1(start1, end1, num1)
B=B1(start2, end2, num2)
Resp1=R1(start3, end3, num3)
Resp2=R2(start4, end4, num4)
Resp3=R3(start5, end5, num5)
Resp4=R4(start6, end6, num6)
Posresp=random.randint(1,4)
R= list(set(A)|set(B))
if Posresp==1:
    Resp1=R
elif Posresp==2:
    Resp2=R
elif Posresp==3:
    Resp3=R
else:
    Resp4=R

unidad1 = {}
unidad1['uniones'] = []
unidad1['uniones'].append({
    'Operador1': A,
    'Operador2': B,
})
unidad1['uniones'].append({
    'A': Resp1,
    'B': Resp2,
    'C': Resp3,
    'D': Resp4
})

with open('unidad1.txt', 'w') as outfile:
    json.dump(unidad1, outfile)
    
with open('unidad1.txt','r') as json_file:
    unidad1 = json.load(json_file)
    
    
    print("¿Cual es el resultado de la union de " + str(unidad1['uniones'][0]['Operador1'])+ " y " + str(unidad1['uniones'][0]['Operador2'])+ "?")
    print("A)"+str(unidad1['uniones'][1]['A'])+ "  B)"+str(unidad1['uniones'][1]['B'])+ "  C)"+str(unidad1['uniones'][1]['C'])+"  D)"+str(unidad1['uniones'][1]['D']))
    Resultado = str(input())
    if unidad1['uniones'][1][Resultado] == R:
        print("¡Correcto!")
    else:
        print("Incorrecto...")
