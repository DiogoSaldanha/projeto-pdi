from utils.ImageProcessor import ImageProcessor
import math

# Rotação apresenta um pequeno erro ao mostrar a imagem na GUI, ajustar isso depois
class Rotation:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    def rotate(self):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        
        #Ãngulo desejado, começar com 45 graus e transformando em radianos pra poder trabalhar com cos() e sin()
        angle_of_rotation = 45
        angle_rad = math.radians(angle_of_rotation)
        
        #Centro da imagem
        center_x = width // 2
        center_y = height // 2
        
        modifiedPixels = []
        
        for y in range(height):            
            for x in range(width):
                #Movendo os pixels em relação ao centro da imagem para poder aplicar a rotação
                x_moved = x - center_x
                y_moved = y - center_y
                
                #Aplicando fórmula de rotação
                x_rotated = int(center_x + (x_moved * math.cos(angle_rad) - y_moved * math.sin(angle_rad)))
                y_rotated = int(center_y + (x_moved * math.sin(angle_rad) + y_moved * math.cos(angle_rad)))
                
                #Se a posição nova está dentro dos limites da imagem original, pega o valor do pixel
                if 0 <= x_rotated < width and 0 <= y_rotated < height:
                    index = y_rotated * width + x_rotated  # Eu tenho que converter (x_rotated, y_rotated) pra um indice de 1D por que pixels é uma lista e não tupla.
                    modifiedPixels.append(pixels[index])  # Pega o pixel naquele indice
                else:
                    # Se a posição tá fora do limite pinto o background de alguma cor
                    modifiedPixels.append((0,0,0))
                    
            
        self.modifiedImage.set_pixels(modifiedPixels)
        
        return self.modifiedImage.get_image()
        
        