import time
questionNumber = 0
right = 0
wrong = 0
level = 0
name = str(input("Por favor ingrese su nombre:  "))
print()
def questions():
    def questionOne():
        global right, wrong, questionNumber , level
        print("¿Cual es el resultado de A∪B  si A={1,2,3} y B={2,4,5}?")
        print("A: A∪B={1,2,3,4,5} B: A∪B={2}  C: A∪B={1,2,2,3,4,5} D: A∪B={1,2,3,4,5}")   
        ans = str(input())
        if ans == "A" or ans == "a":
            print("Respuesta correcta!")
            right = right + 1
            level = level + 1
        else:
            print("Respuesta incorrecta...")
            wrong = wrong+1
            level = level-1
        questionNumber = questionNumber + 1
    def questionTwo():
        global right, wrong, questionNumber, level
        print("¿Cual es el resultado de A∪B∪C  si A={1,3,9} , B={2,9,5} y B={7,4,9,2,0}?")
        print("A: A∪B∪C={1,3,9,2,9,5,7,4,9,2,0} B: A∪B∪C={ 1,3,9,5,7} C: A∪B∪C={ 1,2,3,4,5,7,9,0} D: A∪B∪C={9}")
        ans = str(input())
        if ans == "C" or ans == "c":
            print("Respuesta correcta!")
            right = right + 1
            level = level + 1
        else:
            print("Respuesta incorrecta...")
            wrong = wrong+1
            level = level-1
        questionNumber = questionNumber + 1   
    def questionThree():
        global right, wrong, questionNumber, level
        print("¿Cual es la propiedad conmutativa?")
        print("A:A∪B=A∪A B:A∪B=B∪A C:A∪B=A∪B or D: Ninguna de la anteriores")
        ans = str(input())
        if ans == "B" or ans == "b":
            print("Respuesta correcta!")
            right = right + 1
            level = level + 1
        else:
            print("Respuesta incorrecta...")
            wrong = wrong+1
            level = level-1
        questionNumber = questionNumber + 1   
    def questionFour():
        global right, wrong, questionNumber, level
        print("¿Que es la propiedad de idempotencia")
        print("A:Es la reunión de cualquier conjunto con el conjunto vacío B:Un conjunto con el conjunto universal")
        print("C:Es la intersección de conjuntos o D:Cualquier conjunto unido consigo mismo es igual al mismo conjunto")
        ans = str(input())
        if ans == "D" or ans == "d":
            print("Respuesta correcta!")
            right = right + 1
            level = level + 1
        else:
            print("Respuesta incorrecta...")
            wrong = wrong+1
            level = level-1
        questionNumber = questionNumber + 1
    while level<4:
        time.sleep(1)
        if level==0 or level<0:
            questionOne()
            time.sleep(1)
            print()
            print("Hasta ahora",name,"tienes",right,"respuestas correctas,",wrong,"respuestas incorrectas y has completado",questionNumber,"preguntas")
            print(level)
        time.sleep(1)
        if level==1:
            questionTwo()
            time.sleep(1)
            print()
            print("Hasta ahora",name,"tienes",right,"respuestas correctas,",wrong,"respuestas incorrectas y has completado",questionNumber,"preguntas")
            print(level)
        time.sleep(1)
        if level==2:
            questionThree()
            time.sleep(1)
            print()
            print("Hasta ahora",name,"tienes",right,"respuestas correctas,",wrong,"respuestas incorrectas y has completado",questionNumber,"preguntas")
            print(level)
        time.sleep(1)
        if level==3:
            questionFour()
            time.sleep(1)
            print()
            print("Hasta ahora",name,"tienes",right,"respuestas correctas,",wrong,"respuestas incorrectas y has completado",questionNumber,"preguntas")
            print(level)
        time.sleep(1)
    print()
    print("Ya eres un master en este tema, ¡Felicidades!")
questions()
