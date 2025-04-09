from utils.ImageProcessor import ImageProcessor

#Técnica mais simples implementada, como mostrada no vídeo.
class Grayscale:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    def grayscale(self):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        modifiedPixels = []
        
        for y in range(height):
            for x in range(width):
                index = y * width + x
                
                #Cor do pixel em (x,y)
                r, g, b = pixels[index]

                #Algoritmo
                gray_value = (r + g + b) // 3
                
                modifiedPixels.append((gray_value, gray_value, gray_value))
                        
        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
        
        