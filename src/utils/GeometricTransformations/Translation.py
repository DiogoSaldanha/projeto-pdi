from utils.ImageProcessor import ImageProcessor

# Rotação apresenta um pequeno erro ao mostrar a imagem na GUI, ajustar isso depois
class Translation:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    #Recebe como parametro a quantidade de pixels que quer mexer na imagem, em abos os eixos    
    def translate(self, x_translation, y_translation):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        modifiedPixels = []
        
        for y in range(height):
            for x in range(width):
                #calcula nova posição após translação
                x_modified = x + x_translation
                y_modified = y + y_translation
                
                #checa se a nova posição está nos limites da imagem
                if 0 <= x_modified < width and 0 <= y_modified < height:
                    #se sim, pega o pixel naquela posição e append na lista
                    index = y_modified * width + x_modified
                    modifiedPixels.append(pixels[index])
                else:
                    modifiedPixels.append((0,0,0))
        
        
        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
        
        