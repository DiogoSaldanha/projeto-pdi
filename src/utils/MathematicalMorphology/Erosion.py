from utils.ImageProcessor import ImageProcessor

# remove ruído, afina objetos na imagem
class Erosion:
    def __init__(self, image):
        self.image = image  
        self.modifiedImage = ImageProcessor(self.image)
        self.width = self.image.width
        self.height = self.image.height

    def erode(self):
        pixels = self.modifiedImage.get_pixels()
        modifiedPixels = []

        struct_size = 3
        offset = struct_size // 2

        for y in range(self.height):
            for x in range(self.width):
                min_value = 255  # Para erosão, temos que achar o valor mais escuro

                for dy in range(-offset, offset + 1):
                    for dx in range(-offset, offset + 1):
                        ny = y + dy
                        nx = x + dx

                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            value = pixels[ny * self.width + nx]
                            if isinstance(value, tuple):
                                value = sum(value) // 3  # RGB → cinza
                            min_value = min(min_value, value)

                modifiedPixels.append((min_value, min_value, min_value))

        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
