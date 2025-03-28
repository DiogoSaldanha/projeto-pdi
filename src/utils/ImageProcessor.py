from PIL import Image

class ImageProcessor:
    def __init__(self, image):
        #Inicializo o construtor com uma image
        self.image = image #Objeto Image do Pillow
        self.pixels = list(self.image.getdata()) #Isso é uma lista dos dados de Pixels (em formato de tupla)
        
    #Retorna todos os pixels da imagem
    def get_pixels(self):
        return self.pixels
    
    def set_pixels(self, pixels):
        #Atualiza os pixels da imagem baseado numa lista de novos pixels
        self.pixels = pixels
        self.image.putdata(self.pixels)
        
    def get_image(self):
        #retorna o objeto de imagem atual
        return self.image