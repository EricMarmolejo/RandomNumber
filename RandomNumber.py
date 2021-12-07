#README: In this Game the user has to guess the number between 1 to 10
import random
import msvcrt

print("======================================")
print("             ¡WELCOME!                ")
print("======================================")
print("Tu objetivo es adivinar el número generado \npor la computadora")


def adivina_el_numero (x):  
    num_aleatorio = random.randint(1,x) #Número aleatorio entre 1 y X

    prediccion = 0

    while prediccion != num_aleatorio:
        #El usuario ingresa un número
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) # f-string para poder reemplazar un valor en una variable

        if prediccion < num_aleatorio:
            print("Intenta de nuevo con un número Mayor ")

        elif prediccion > num_aleatorio:
            print("Intenta de nuevo con un número Menor ")

    print(f"Felicidades Adivinaste el número {num_aleatorio} correctamente.  ¡AWESOME!")
    print(""" 
                 .:::::::::::::.  
                .::'  '''''  '::. 
                :::           ::: 
                :::           ::: 
                :::           ::: 
                ::'           ':: 
                : : /~~~' '~~~\ : :
                :(:  <o> | <o>  :):
                '.:     / \     :.'
                 ':    (. .)    :' 
                  '.  .:::::.  .'
                   :  <----->  :   
                   '.  ~:::~  .'
                     '.  '  .'     
                      ''''' 	""")


adivina_el_numero(15)

msvcrt.getch()# Despues de importar la libreria 'svcrt' se coloca este alfinal para que el ejecutable no se cierre automaticamente

