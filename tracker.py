import csv  # archivos separados por comas
import os  # operaciones del sistema
from datetime import datetime  # fecha y hora

CSV_FILE = "journalTracker.csv"


def inicializar_archivo():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)  # definir la primera fila con los nombres exactos de las variables
            writer.writerow([
                "fecha", "num_dos", "gimnasio", "screen_time_h", "tipo_sueno",
                "paginas", "agua", "periodo", "skincare", "peso",
                "temperatura", "pasos", "luna", "dolor_cabeza", "energia"
            ])
        print("Archivo inicializado correctamente")
    else:
        print("El archivo ya existe")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def pedir_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número decimal válido.")

def pedir_binario(mensaje):
    while True:
        try:
            valor=int(input(mensaje))
            if valor in [0, 1]:
                return valor
            else:
                print("Solo se admite un 0 o 1.")
        except ValueError:
            print("Por favor, ingrese un número entero válido (0 o 1).")
def pedir_opcion(mensaje, opciones):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in opciones:
            return valor
        else:
            print(f"Por favor, ingrese una opción válida: {', '.join(opciones)}.")
def registro_dia():
    inicializar_archivo()
    hoy=datetime.now().strftime("%Y-%m-%d")
    veces_bano = pedir_entero("¿Cuantas veces has hecho caca hoy? ")
    veces_bano_intentadas = pedir_entero("¿Cuantas veces has intentado hacer caca hoy? ")
    paginas_leidas = pedir_entero("¿Cuantas páginas has leído hoy? ")
    vasos_agua = pedir_entero("¿Cuantos vasos de agua has tomado hoy? ")
    pasos = pedir_entero("¿Cuantos pasos has dado hoy? ")
    peso = pedir_decimal("¿Cual es tu peso hoy? ")
    screen_time = pedir_decimal("¿Cuantas horas has pasado frente a una pantalla hoy? ")
    temperatura = pedir_decimal("¿Cual es la temperatura de tu cuerpo hoy? ")
    gimnasio = pedir_binario("¿Has ido al gimnasio hoy? (0 = No, 1 = Sí) ")
    skincare_crema=pedir_binario("¿Te has aplicado crema de skincare hoy? (0 = No, 1 = Sí) ")
    dolor_cabeza=pedir_binario("¿Has tenido dolor de cabeza hoy? (0 = No, 1 = Sí) ")
    sueno=pedir_opcion("¿Como ha sido tu sueño hoy? (raro, calmado, triste, feliz, estresante, no recuerdo) ", (["raro", "calmado", "triste", "feliz", "estresante", "no recuerdo"]))
    energia=pedir_opcion("¿Como ha sido tu nivel de energía hoy? (bajo, medio, alto) ", ["bajo", "medio", "alto"])
    ciclo_lunar=pedir_opcion("¿En que fase del ciclo lunar te encuentras hoy? (luna nueva, cuarto creciente, luna llena, cuarto menguante) ", ["luna nueva", "cuarto creciente", "luna llena", "cuarto menguante"])
    periodo=pedir_binario("¿Estas en tu periodo hoy? (0 = No, 1 = Sí) ")
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            hoy, veces_bano, gimnasio, screen_time, sueno,
            paginas_leidas, vasos_agua, periodo, skincare_crema, peso,
            temperatura, pasos, ciclo_lunar, dolor_cabeza, energia
        ])
if __name__ == "__main__":
    registro_dia()