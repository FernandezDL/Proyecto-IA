import matplotlib.pyplot as plt

#112
resultados = [
    "IA", "IA", "IA", "IA", "IA", "IA", "USER", "IA", "IA", "USER", "USER", "USER", "USER",
    "IA", "IA", "IA", "IA", "IA", "USER", "USER", "IA", "IA", "IA", "USER", "USER", "IA",
    "USER", "USER", "IA", "IA", "IA", "USER", "USER", "USER", "IA", "USER", "IA", "IA",
    "IA", "IA", "USER", "USER", "IA", "IA", "IA", "USER", "USER", "USER", "USER", "IA",
    "USER", "USER", "USER", "USER", "USER", "USER", "IA", "USER", "USER", "USER", "IA",
    "IA", "IA", "USER", "USER", "IA", "USER", "IA", "USER", "USER", "IA", "IA", "USER",
    "IA", "USER", "USER", "IA", "IA", "USER", "USER", "IA", "IA", "IA", "IA", "IA", "IA",
    "USER", "IA", "IA", "USER", "USER", "USER", "USER", "IA", "IA", "IA", "IA", "IA", "USER",
    "USER", "USER", "IA", "IA", "USER", "IA", "USER", "IA", "IA", "USER", "USER"
]

#IA - 60
#USER - 52

#Juegos Ganados por la IA: 58
#Porcentaje de Juegos Ganados por la IA: 52.73%


def calcular_metricas(resultados):
    total_juegos = len(resultados)
    juegos_ganados_ia = resultados.count("IA")
    porcentaje_ganados_ia = (juegos_ganados_ia / total_juegos) * 100
    return juegos_ganados_ia, porcentaje_ganados_ia

juegos_ganados_ia, porcentaje_ganados_ia = calcular_metricas(resultados)
print(f"Juegos Ganados por la IA: {juegos_ganados_ia}")
print(f"Porcentaje de Juegos Ganados por la IA: {porcentaje_ganados_ia:.2f}%")

def graficar_aprendizaje(resultados):
    juegos_acumulados = [1 if resultado == "IA" else 0 for resultado in resultados]
    juegos_acumulados = [sum(juegos_acumulados[:i+1]) for i in range(len(juegos_acumulados))]
    plt.figure(figsize=(10, 5))
    plt.plot(juegos_acumulados, label='Juegos Ganados por IA')
    plt.xlabel('Número de Juegos')
    plt.ylabel('Juegos Ganados Acumulados')
    plt.title('Curva de Aprendizaje de la IA')
    plt.legend()
    plt.show()

graficar_aprendizaje(resultados)



