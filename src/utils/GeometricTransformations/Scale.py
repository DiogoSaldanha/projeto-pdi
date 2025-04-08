from utils.ImageProcessor import ImageProcessor

#Classe usada para os menos de Zoom In e Zoom Out
class Scale:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    # Dependendo do parâmetro vai dar zoom in ou zoom out, negativo é zoom out, positivo é zoom in
    def zoom(self, in_or_out):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        
        modifiedPixels = []
        
        for y in range(height):
            for x in range(width):
                # Mapeando a nova posição do pixel na imagem redimensionada para a posição correspondente na imagem original
                src_x = int(x / in_or_out)
                src_y = int(y / in_or_out)
                
                # Garantir que os índices estão dentro dos limites da imagem original usando If/Else
                if src_x < 0:
                    src_x = 0
                elif src_x >= width:
                    src_x = width - 1
                
                if src_y < 0:
                    src_y = 0
                elif src_y >= height:
                    src_y = height - 1
                
                # Pega o pxel na posição mapeada
                index = src_y * width + src_x # Convertendo (src_x, src_y) para um índice 1D
                modifiedPixels.append(pixels[index])
                
        self.modifiedImage.set_pixels(modifiedPixels)
        
        return self.modifiedImage.get_image()
        