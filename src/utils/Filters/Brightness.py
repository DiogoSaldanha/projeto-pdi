from utils.ImageProcessor import ImageProcessor

class Brightness:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    def brightness(self):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        modifiedPixels = []
        
        #Aplicando valores de contraste e brilho para testes
        contrast = 1 #Para diminuir o constraste, apenas valores entre 0 e 1. Aumentar maior que 1
        brightness = 0
        
        for y in range(height):
            for x in range(width):
                index = y * width + x
                
                r, g, b = pixels[index]
                
                if contrast != 1:
                    r = int(r * contrast)
                    g = int(g * contrast)
                    b = int(b * contrast)
                    
                if brightness != 0:
                    r = int(r + brightness)
                    g = int(g + brightness)
                    b = int(b + brightness)
                    
                #Tenho que ter certeza que os valores ficam entre 0 e 255, posso fazer isso assim:
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))
                
                modifiedPixels.append((r,g,b))
                        
        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
        
        