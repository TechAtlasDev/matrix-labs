from .core.matrix import Matrix
from .core.processor import Processor
from .core.drawer import Drawer
from .core.generator import Generator
import time

def main():
    w_matrix = 250
    h_matrix = 250
    cantidad_lineas = 1000

    start_time = time.time()

    # Creando la matriz
    matriz = Matrix(
        width=w_matrix,
        height=h_matrix,
    )

    dibujador = Drawer(matrix=matriz)

    for line in Generator().generate_lines(w_matrix, h_matrix, cantidad_lineas):
        dibujador.draw_line(
            start=line[0],
            end=line[1]
        )

    elapsed_time = time.time() - start_time
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")

    # Graficando la matriz
    Processor(matriz).graficar()

if __name__ == "__main__":
    main()