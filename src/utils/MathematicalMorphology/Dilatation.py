from utils.ImageProcessor import ImageProcessor

# expande as regiões brancas da imagem
class Dilatation:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(self.image)
        self.width = self.image.width
        self.height = self.image.height

    def dilate(self):
        pixels = self.modifiedImage.get_pixels()
        modifiedPixels = []

        # Elemento de estruturação 3x3
        struct_size = 3
        offset = struct_size // 2

        for y in range(self.height):
            for x in range(self.width):
                max_value = 0  # Para dilatação, usamos o maior valor vizinho

                for dy in range(-offset, offset + 1):
                    for dx in range(-offset, offset + 1):
                        ny = y + dy
                        nx = x + dx

                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            value = pixels[ny * self.width + nx]
                            if isinstance(value, tuple):
                                value = sum(value) // 3  # RGB → cinza
                            max_value = max(max_value, value)

                modifiedPixels.append((max_value, max_value, max_value))  # Resultado é branco se qualquer vizinho era branco

        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
