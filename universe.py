import numpy as np
import matplotlib.pyplot as plt
import random
import os

os.makedirs("Universo-Combinaciones", exist_ok=True)

def write_combinations_with_dynamic_blocks(n, file_path):
    with open(file_path, 'w') as file:
        file.write("{e ")  # Iniciar con el elemento vacío 'e'
        initial_block_size = 100  # Tamaño inicial del bloque
        for length in range(1, n + 1):
            # Ajustar dinámicamente el tamaño del bloque basado en la longitud de la combinación
            block_size = max(initial_block_size // (length), 1)  # Asegurar al menos 1 combinación por línea
            count = 0  # Contador para agregar saltos de línea cada 'block_size' combinaciones
            combination = ['a'] * length
            while True:
                file.write(''.join(combination) + " ")
                count += 1
                if count % block_size == 0:
                    file.write("\n")  # Agregar un salto de línea después de cada 'block_size' combinaciones
                for i in range(length - 1, -1, -1):
                    if combination[i] == 'a':
                        combination[i] = 'b'
                        break
                    combination[i] = 'a'
                else:
                    break
        file.write("}")  

def plot_counts_from_file(file_path, title, ylabel, log_scale=False):
    counts = []
    with open(file_path, 'r') as file:
        for line in file:
            items = line.strip(" {}\n").split()
            for item in items:
                if item != 'e':  # Ignorar el elemento 'e'
                    counts.append(item.count('b'))

    plt.figure(figsize=(10, 6))
    x = np.arange(len(counts))
    if log_scale:
        counts = np.log10(np.array(counts) + 1)  # Ajuste para logaritmo
        plt.plot(x, counts, label=f"Log10 del {ylabel}")
    else:
        plt.plot(x, counts, label=f"Número de {ylabel}")
    plt.title(title)
    plt.xlabel("Índice de la Combinación")
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.close()

def main():
    repeat = True
    while repeat:
        mode = input("Elige el modo (manual/auto): ").lower()
        if mode == "manual":
            n_input = input("Ingresa el valor de n: ")
            try:
                n = int(n_input)
                if n < 0:
                    raise ValueError("El número debe ser positivo.")
            except ValueError as e:
                print(f"Error: {e}. Ingresar un número entero positivo.")
                continue
        elif mode == "auto":
            n = random.randint(0, 1000)
            print(f"Modo automático seleccionado. Generando para n = {n}")
        else:
            print("Modo no reconocido. Elige 'manual' o 'auto'.")
            continue

        file_path = 'Universo-Combinaciones/combinations.txt'
        write_combinations_with_dynamic_blocks(n, file_path)
        print(f"Las combinaciones hasta longitud {n} han sido guardadas en {file_path}.")

        # Graficar el conteo de 'b's leyendo desde el archivo
        plot_counts_from_file(file_path, "Conteo de 'b's en las combinaciones", "Conteo de 'b's")

        # Graficar el logaritmo base 10 del conteo de 'b's, también leyendo desde el archivo
        plot_counts_from_file(file_path, "Logaritmo base 10 del conteo de 'b's en las combinaciones", "Conteo de 'b's", log_scale=True)

        repeat_prompt = input("¿Quieres realizar otra operación? (s/n): ").lower()
        repeat = repeat_prompt == 's'

if __name__ == "__main__":
    main()
