#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

# Función para que la computadora elija una opción aleatoria
def eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    eleccion = random.choice(opciones)
    return eleccion

# Función para determinar el ganador de una ronda
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    if (jugador == "piedra" and computadora == "tijera") or \
       (jugador == "papel" and computadora == "piedra") or \
       (jugador == "tijera" and computadora == "papel"):
        return "Jugador"
    return "Computadora"

# Función principal del juego
def jugar_piedra_papel_tijera():
    victorias_jugador = 0
    victorias_computadora = 0

    while True:
        print("Elige tu jugada: piedra, papel, tijera, o 'salir' para terminar el juego.")
        jugada_jugador = input().lower()

        if jugada_jugador == "salir":
            break

        if jugada_jugador not in ["piedra", "papel", "tijera"]:
            print("Jugada no válida. Intenta de nuevo.")
            continue

        jugada_computadora = eleccion_computadora()
        resultado = determinar_ganador(jugada_jugador, jugada_computadora)

        print(f"Tú eliges {jugada_jugador}")
        print(f"La computadora elige {jugada_computadora}")
        print(f"Resultado: {resultado}\n")

        if resultado == "Jugador":
            victorias_jugador += 1
        elif resultado == "Computadora":
            victorias_computadora += 1

    print(f"Total de victorias - Jugador: {victorias_jugador}, Computadora: {victorias_computadora}")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()