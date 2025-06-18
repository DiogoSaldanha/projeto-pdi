from PIL import Image

from utils.Filters.Grayscale import Grayscale
from utils.Filters.Brightness import Brightness
from utils.Filters.Threshold import Threshold
from utils.MathematicalMorphology.Dilatation import Dilatation
from utils.MathematicalMorphology.Erosion import Erosion


class Challenge:
    def __init__(self, image):
        # Garante que a imagem esteja em RGB
        self.image = image.convert("RGB")
        
        #Modificações automáticas na imagem
        #'''
        grayscale = Grayscale(self.image)
        self.image = grayscale.grayscale()
        
        contrast = Brightness(self.image)
        self.image = contrast.brightness(brightness=0, contrast=5)
        
        threshold = Threshold(self.image)
        self.image = threshold.threshold(100)
        #'''
        self.width = self.image.width
        self.height = self.image.height
        self.pixels = list(self.image.getdata())
        self.binary_matrix = self.build_binary_matrix()

    #Converte a imagem em uma matriz 0/1 baseada nos pixels brancos (comprimidos)
    def build_binary_matrix(self):
        matrix = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                r, g, b = self.pixels[y * self.width + x]
                value = 1 if (r + g + b) > 0 else 0  # branco = 1, preto = 0
                row.append(value)
            matrix.append(row)
        return matrix

    
    # A função abaixo percorre a matriz e executa rotulagem de componentes conectados.
    # Cada componente identificado representa um comprimido.
    # A forma é classificada com base no seu aspect ratio.
    def analyze(self):
        label = 2  # Começa com 2 para diferenciar de 0 e 1
        labeled_matrix = [[0] * self.width for _ in range(self.height)]
        components = {}

        for y in range(self.height):
            for x in range(self.width):
                if self.binary_matrix[y][x] == 1 and labeled_matrix[y][x] == 0:
                    # Novo objeto encontrado
                    pixels = []
                    self._dfs(x, y, label, labeled_matrix, pixels)

                    # Coleta bounding box e área
                    xs = [px for px, py in pixels]
                    ys = [py for px, py in pixels]
                    min_x, max_x = min(xs), max(xs)
                    min_y, max_y = min(ys), max(ys)
                    width = max_x - min_x + 1
                    height = max_y - min_y + 1
                    area = len(pixels)

                    aspect_ratio = width / height if height != 0 else 0

                    components[label] = {
                        "area": area,
                        "width": width,
                        "height": height,
                        "aspect_ratio": aspect_ratio
                    }

                    label += 1
                    for i, comp in enumerate(components.values(), 1):
                        print(f"[{i}] AR={comp['aspect_ratio']:.2f} | W={comp['width']} | H={comp['height']} | A={comp['area']}")
        
        # Classificação
        total = len(components)
        round_pills = 0
        capsules = 0
        broken_pills = 0
        
        for comp in components.values():
            ratio = comp["aspect_ratio"]
            area = comp["area"]
            
            if 0.9 <= ratio <= 1.1:
                round_pills += 1
            else:
                if area < 1000:
                    broken_pills += 1
                else:
                    capsules += 1

        return total, round_pills, capsules, broken_pills

    # Algoritmo de Busca Em Profundidade para rotular todos os pixels conectados (Depth-First Search)
    def _dfs(self, x, y, label, labeled_matrix, pixels):
        stack = [(x, y)]

        while stack:
            cx, cy = stack.pop()

            if (
                0 <= cx < self.width and
                0 <= cy < self.height and
                self.binary_matrix[cy][cx] == 1 and
                labeled_matrix[cy][cx] == 0
            ):
                labeled_matrix[cy][cx] = label
                pixels.append((cx, cy))

                # 8 conectividade
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx != 0 or dy != 0:
                            stack.append((cx + dx, cy + dy))
