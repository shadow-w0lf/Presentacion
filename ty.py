from threading import *
import time

def manejarCliente1():
    for i in range(12):
        print("Esperando al cliente 1...")

def manejarCliente2():
    for i in range(12):
        print("Esperando al cliente 2...")
        time.sleep(1) # Espera 3 segundos

# Creacion de los hilos
t = Timer(5.0, manejarCliente1)
t2 = Timer(3.0, manejarCliente2)

# Ejecutar los hilos
t.start()
t2.start()