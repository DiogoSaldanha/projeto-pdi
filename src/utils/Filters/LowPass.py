from utils.ImageProcessor import ImageProcessor

class LowPass:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    def low_pass(self):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        modifiedPixels = []
        
        mask_size = 3
        mask = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        
        # O total de coeficientes na máscara (no caso de uma máscara 3x3, são 9)
        total_coefficients =  mask_size * mask_size
        
        # Deslocamento da máscara (metade do tamanho da máscara)
        offset = mask_size // 2
        
        for y in range(height):
            for x in range(width):
                #Acumuladores especificos para RGB para a soma ponderada dos pixels vizinhos
                sum_red = 0
                sum_green = 0
                sum_blue = 0
                
                #Contador de pixels válidos (dentro da imagem)
                counter = 0
                
                #Abaixo é um for para iterar pela janela de pixels ao redor do pixel atual (x,y)
                for py in range(-offset, offset + 1):
                    for px in range(-offset, offset + 1):
                        #Coordenados do pixel vizinho:
                        coord_x = x + px
                        coord_y = y + py
                        
                        #Verificação para se as coordenadas do vizinho estão dentro da imagem
                        if 0 <= coord_x < width and 0 <= coord_y < height:
                            #Índice do pixel naquela lista unidimensional:
                            index_pixel = coord_y * width + coord_x
                            
                            #Obtendo valor RGB do pixel
                            r, g, b = pixels[index_pixel]
                            
                            #Somando os valores ponderados em cada um dos canais
                            sum_red += r * mask[py + offset][px + offset]
                            sum_green += g * mask[py + offset][px + offset]
                            sum_blue += b * mask[py + offset][px + offset]
                            
                            counter += 1
                
                #Calcula média ponderada dos valores dos pixels vizinhos para cada canal
                r_average = sum_red // total_coefficients
                g_average = sum_green // total_coefficients
                b_average = sum_blue // total_coefficients
                
                
                #Adiciona valor do 'pixel médio'
                modifiedPixels.append((r_average, g_average, b_average))
        
        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()