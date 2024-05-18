import matplotlib.pyplot as plt
import pickle

def cargar_resultados(nombre_archivo='resultados.pkl'):
    try:
        with open(nombre_archivo, 'rb') as f:
            resultados = pickle.load(f)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
        print(f"Error al cargar el archivo: {e}. Se creará un nuevo registro de resultados.")
        resultados = {"total_juegos": 0, "juegos_ganados": []}
    return resultados

def guardar_resultados(resultados, nombre_archivo='resultados.pkl'):
    with open(nombre_archivo, 'wb') as f:
        pickle.dump(resultados, f)

def actualizar_resultados(ganador, nombre_archivo='resultados.pkl'):
    resultados = cargar_resultados(nombre_archivo)
    resultados["total_juegos"] += 1
    if ganador == "IA":
        juegos_ganados = len(resultados["juegos_ganados"])
        juegos_ganados += 1
        resultados["juegos_ganados"].append(juegos_ganados)
    guardar_resultados(resultados, nombre_archivo)


def graficar_resultados(nombre_archivo='resultados.pkl'):
    resultados = cargar_resultados(nombre_archivo)
    juegos_ganados = resultados["juegos_ganados"]

    # Imprimir puntos de datos específicos
    puntos_interes = [0, len(juegos_ganados) // 4, len(juegos_ganados) // 2, 3 * len(juegos_ganados) // 4, len(juegos_ganados) - 1]
    for punto in puntos_interes:
        if punto < len(juegos_ganados):
            print(f"Punto {punto}: Juego {punto + 1}, Juegos Ganados = {juegos_ganados[punto]}")

    plt.figure(figsize=(10, 5))
    plt.plot(juegos_ganados)
    plt.title("Cantidad de Juegos Ganados por la IA")
    plt.xlabel("Número de Juegos")
    plt.ylabel("Juegos Ganados")
    plt.show()

    if juegos_ganados:
        porcentaje_ganados = juegos_ganados[-1] / resultados["total_juegos"] * 100
        print(f"Porcentaje de juegos ganados por la IA: {porcentaje_ganados:.2f}%")

def mostrar_porcentaje(nombre_archivo='resultados.pkl'):
    resultados = cargar_resultados(nombre_archivo)
    if resultados["total_juegos"] > 0:
        porcentaje_ganados = len(resultados["juegos_ganados"]) / resultados["total_juegos"] * 100
        print(f"Porcentaje de juegos ganados por la IA hasta ahora: {porcentaje_ganados:.2f}%")
