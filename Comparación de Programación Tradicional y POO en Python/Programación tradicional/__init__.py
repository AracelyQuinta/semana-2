# Programación Tradicional
# Ejemplo: Determinacion del promedio semanal del clima.

# Lista de días de la semana.
Dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Lista vacía para almacenar las temperaturas ingresadas por el usuario.
Dias_temperatura = []

# Variables para calcular la suma y el promedio de temperaturas.
suma = 0
promedio = 0

# Bucle que recorre cada día de la semana y solicita la temperatura.
for dia in Dias_semana:
    temperatura = float(input(f"Ingrese la temperatura del día: {dia}"))  # Solicita y convierte la entrada a tipo flotante.
    suma += temperatura  # Acumula la suma de todas las temperaturas ingresadas.
    Dias_temperatura.append(temperatura)  # Almacena la temperatura en la lista.

    # Imprime la temperatura ingresada del día correspondiente.
    print(f"{dia} su temperatura es de {temperatura} °C.")

# Calcula y muestra el promedio de temperaturas de la semana.
print("promedio", suma / len(Dias_semana))  # División entre el número de días para obtener el promedio.
