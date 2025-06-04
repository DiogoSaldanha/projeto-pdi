from utils.ImageProcessor import ImageProcessor
import math


#Aplicação do algoritmo de Sobel
class HighPass:
    def __init__(self, image):
        self.image = image.convert("RGB")  # Garante que a imagem esteja em RGB
        self.processor = ImageProcessor(self.image)
        self.width = self.image.width
        self.height = self.image.height

    def high_pass(self):
        original_pixels = self.processor.get_pixels()
        new_pixels = []

        # Máscaras de Sobel
        sobel_x = [
            [ 1,  0, -1],
            [ 2,  0, -2],
            [ 1,  0, -1]
        ]

        sobel_y = [
            [ 1,  2,  1],
            [ 0,  0,  0],
            [-1, -2, -1]
        ]

        offset = 1  # Para uma máscara 3x3

        for y in range(self.height):
            for x in range(self.width):
                gx_r = gx_g = gx_b = 0
                gy_r = gy_g = gy_b = 0

                for ky in range(-offset, offset + 1):
                    for kx in range(-offset, offset + 1):
                        nx = x + kx
                        ny = y + ky

                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            index = ny * self.width + nx
                            r, g, b = original_pixels[index]

                            kx_weight = sobel_x[ky + offset][kx + offset]
                            ky_weight = sobel_y[ky + offset][kx + offset]

                            gx_r += r * kx_weight
                            gx_g += g * kx_weight
                            gx_b += b * kx_weight

                            gy_r += r * ky_weight
                            gy_g += g * ky_weight
                            gy_b += b * ky_weight

                # Calcula a magnitude do gradiente para cada um dos canais
                mag_r = int(math.sqrt(gx_r ** 2 + gy_r ** 2))
                mag_g = int(math.sqrt(gx_g ** 2 + gy_g ** 2))
                mag_b = int(math.sqrt(gx_b ** 2 + gy_b ** 2))

                # Preciso garantir que os valores fiquem entre esses intervalos
                mag_r = max(0, min(255, mag_r))
                mag_g = max(0, min(255, mag_g))
                mag_b = max(0, min(255, mag_b))

                new_pixels.append((mag_r, mag_g, mag_b))

        self.processor.set_pixels(new_pixels)
        return self.processor.get_image()
