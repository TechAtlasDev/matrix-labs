from .matrix import Matrix
from ..utils.screen import Screen

class Processor:
    """
    Clase para procesar una matriz y realizar operaciones como graficarla.
    """
    def __init__(self, matrix: Matrix):
        """
        Inicializa el Processor con una matriz.

        :param matrix: Una instancia de la clase Matrix.
        """
        if not isinstance(matrix, Matrix):
            raise ValueError("Se esperaba una instancia de Matrix.")
        self.matrix = matrix

    def graficar(self):
        """
        Convierte la matriz dispersa en una matriz densa y la grafica usando Screen.
        """
        if not self.matrix:
            raise ValueError("La matriz no puede ser None.")

        # Convertir la matriz dispersa en una matriz densa usando comprensión de listas
        matrix_dense = [
            [self.matrix.query(x, y) for x in range(self.matrix.width)]
            for y in range(self.matrix.height)
        ]

        # Graficar la matriz densa
        screen = Screen("Matriz graficada")
        screen.view(matrix_dense)