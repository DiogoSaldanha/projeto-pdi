from utils.ImageProcessor import ImageProcessor

#Classe usada para os menos de Zoom In e Zoom Out
class Scale:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    # Dependendo do parâmetro vai dar zoom in ou zoom out, valores entre 0 e 1 são zoom out, acima de 1 é zoom in
    def zoom(self, in_or_out):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height

        modifiedPixels = []

        # Dimensões da imagem pós escala
        scaled_width = int(width * in_or_out)
        scaled_height = int(height * in_or_out)

        # Offset pra centralizar a imagem no canvas
        x_offset = (width - scaled_width) // 2
        y_offset = (height - scaled_height) // 2

        for y in range(height):
            for x in range(width):
                # Verifica se o pixel está dentro da área da imagem
                if (x_offset <= x < x_offset + scaled_width) and (y_offset <= y < y_offset + scaled_height):
                    # Mapeando a nova posição do pixel na imagem redimensionada para a posição correspondente na imagem original
                    src_x = int((x - x_offset) / in_or_out)
                    src_y = int((y - y_offset) / in_or_out)

                    if 0 <= src_x < width and 0 <= src_y < height:
                        index = src_y * width + src_x
                        modifiedPixels.append(pixels[index])
                    else:
                        modifiedPixels.append((0, 0, 0))  # pixel é preto se fica fora dos limites
                else:
                    modifiedPixels.append((0, 0, 0))  # pixel preto fora da imagem quando escala

        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()


        