from .matrix import Matrix

class Drawer:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix

    def draw_line(self, start: list[int, int], end: list[int, int], value: int = 1):
        """
        Dibuja una línea desde `start` hasta `end` en la matriz dispersa.
        Usa el algoritmo de Bresenham para trazar la línea.
        """
        x1, y1 = start
        x2, y2 = end

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steep = dy > dx

        # Si la línea es más vertical que horizontal, intercambiamos x e y
        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Aseguramos que x1 < x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = x2 - x1
        dy = abs(y2 - y1)
        error = dx // 2
        y_step = 1 if y1 < y2 else -1
        y = y1

        # Iteramos sobre cada punto de la línea
        for x in range(x1, x2 + 1):
            if steep:
                self.matrix.set(y, x, value)  # Intercambiamos x e y si la línea es vertical
            else:
                self.matrix.set(x, y, value)  # Caso normal

            error -= dy
            if error < 0:
                y += y_step
                error += dx