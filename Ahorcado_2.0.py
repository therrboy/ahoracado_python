import random
import modulo_ahoracado_1

from Hangman_words_module import word_list #desde el modulo importa directamente la lista sin hacer una variable extra
palabra_elegida = random.choice(word_list)

total_caracteres = []
for i in range(len(palabra_elegida)):
    total_caracteres.append("_")

var1 = modulo_ahoracado_1.ahorcado_1
var2 = modulo_ahoracado_1.ahorcado_2
var3 = modulo_ahoracado_1.ahorcado_3
var4 = modulo_ahoracado_1.ahorcado_4
var5 = modulo_ahoracado_1.ahorcado_5

print(f"La Palabra a adivinar es: {total_caracteres}\n")

final_del_juego = False
letra_usada = []
vidas = 5

while not final_del_juego:
    letra_input = str(input("ingrese una letra: ").lower())
    letra_usada += letra_input
    if letra_input in total_caracteres:
        print(f"ya utilizo la letra -{letra_input}-, elija otra")
        print(f"Letras usadas {letra_usada}\n")
    for posicion in range(len(palabra_elegida)):
        letra_var = palabra_elegida[posicion]
        if letra_var == letra_input:
            total_caracteres[posicion] = letra_var
            print(f"Esta letra esta en la palabra {total_caracteres}")
            print(f"Letras usadas {letra_usada}\n")

    if letra_input not in palabra_elegida:
        vidas -= 1
        print("Esta letra no esta en la palabra")
        print(f"Te quedan {vidas} vidas")
        print(f"Letras usadas {letra_usada}\n")
        if vidas == 4:
            print(var1)
        elif vidas == 3:
            print(var2)
        elif vidas == 2:
            print(var3)
        elif vidas == 1:
            print(var4)
        if vidas == 0:
            final_del_juego = True
            print(var5)
            print("Perdiste")
    if "_" not in total_caracteres:
        final_del_juego = True
        print("Gano")
        total_caracteres = "".join(total_caracteres)
        print(f"La palabra es {total_caracteres}")
