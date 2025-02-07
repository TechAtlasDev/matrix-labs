from matplotlib import pyplot as plt
from dataclasses import dataclass

@dataclass
class Screen:
    """
    Clase para visualizar matrices usando matplotlib.
    """
    title: str

    def view(self, content, cmap="binary"):
        """
        Muestra una matriz 2D como una imagen.

        :param content: Una lista de listas (matriz 2D) con los valores a graficar.
        :param cmap: Mapa de colores para la visualización (por defecto: 'binary').
        """
        if not content or not isinstance(content, list) or not all(isinstance(row, list) for row in content):
            raise ValueError("El contenido debe ser una lista de listas (matriz 2D).")

        plt.title(self.title)
        plt.imshow(content, cmap=cmap, origin="lower")  # Usamos origin="lower" para que (0, 0) esté en la esquina inferior
        plt.colorbar()
        plt.show()

    def save(self, content, filename: str, cmap="binary"):
        """
        Guarda la matriz 2D como una imagen en un archivo.

        :param content: Una lista de listas (matriz 2D) con los valores a graficar.
        :param filename: Nombre del archivo donde se guardará la imagen (por ejemplo, 'output.png').
        :param cmap: Mapa de colores para la visualización (por defecto: 'binary').
        """
        if not content or not isinstance(content, list) or not all(isinstance(row, list) for row in content):
            raise ValueError("El contenido debe ser una lista de listas (matriz 2D).")

        plt.title(self.title)
        plt.imshow(content, cmap=cmap, origin="lower")
        plt.colorbar()
        plt.savefig(filename)
        plt.close()  # Cerrar la figura para liberar memoria