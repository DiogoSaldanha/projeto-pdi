from utils.ImageProcessor import ImageProcessor

class Mirror:
    def __init__(self, image):
        #Inicializo o construtor com uma image
        self.image = image #Objeto Image do Pillow que retiro de ImageProcessor
        self.modifiedImage = ImageProcessor(image) #crio uma copia da imagem original para poder modificar
        
        
    def mirror(self):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        vertical = False #Mudar para testes
        
        modifiedPixels = []
        
        for i in range(height):            
            for j in range(width):
                #currentPixel = pixels[i * width + j]
                mirroredPixel = pixels[i * width + (width - j - 1)] # setando o pixel espelhado na coluna oposta à atual
                modifiedPixels.append(mirroredPixel)
                            
        #Ativa o espelhamento na vertical
        if vertical:
            modifiedPixels = modifiedPixels[::-1]
            
        
        self.modifiedImage.set_pixels(modifiedPixels)
        
        return self.modifiedImage.get_image()