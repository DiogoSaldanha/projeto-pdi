from utils.ImageProcessor import ImageProcessor

class Threshold:
    def __init__(self, image):
        self.image = image  # NÃO converte aqui — deixa isso a cargo do chamador
        self.modifiedImage = ImageProcessor(self.image)
        self.width = self.image.width
        self.height = self.image.height

    def threshold(self, value=128):
        pixels = self.modifiedImage.get_pixels()
        modifiedPixels = []

        for pixel in pixels:
            # Se pixel for tupla RGB, usa média; se já for int, usa direto
            if isinstance(pixel, tuple):
                gray = sum(pixel) // 3
            else:
                gray = pixel

            # Aplicação do limiar
            if gray >= value:
                modifiedPixels.append((255, 255, 255))  # Branco
            else:
                modifiedPixels.append((0, 0, 0))        # Preto

        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
