# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA
import random
import numpy as np

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

if __name__ == '__main__':
    print("Ahora sí! buena suerte\n")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    print('#########################')
    print('BIENVENIDOS A BLACKJACK21')
    print('#########################\n')
    
    nombre = str(input('ingrese nombre del jugador: '))
    print()
    cartas = (random.randint(1,13))
    print('carta de', nombre, 'es: ', cartas)
    print()
    
    contador= cartas
        
    
    opcion = int(input('presione 1 para pedir otra carta o 2 para plantarte: '))
    
    while opcion != 1 and opcion != 2:
        print('la opcion es incorrecta, ingrese una opcion')
        opcion = int(input('presione 1 para pedir otra carta o 2 para plantarte: '))
    
    while opcion == 1:
        cartas = (random.randint(1,13))
        print('carta de', nombre, 'es: ', cartas)
        contador += cartas
        print('hasta ahora sumas', contador)
        print()
        
        if contador > 21:
            print('te pasaste, tus cartas suman', contador)
            break
        if contador == 21:
            print('ganaste, sumaste', contador)
            break
        else:
            opcion = int(input('presione 1 para pedir otra carta o 2 para plantarte: '))
                
            while opcion != 1 and opcion != 2:
                print('la opcion es incorrecta, ingrese una opcion')
                opcion = int(input('presione 1 para pedir otra carta o 2 para plantarte: '))
            
            
            
            
        
    

        
        
                 
    
    
    
    
    
    
    
        
    


    print("terminamos")