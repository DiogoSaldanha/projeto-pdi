from utils.ImageProcessor import ImageProcessor

class HighPass:
    def __init__(self, image):
        self.image = image
        self.modifiedImage = ImageProcessor(image)
        
    def high_pass(self):
        pixels = self.modifiedImage.get_pixels()
        width = self.image.width
        height = self.image.height
        modifiedPixels = []
        
        mask_size = 3
        offset = mask_size // 2
        total_coefficients = mask_size * mask_size
        
        for y in range(height):
            for x in range(width):
                sum_red = 0
                sum_green = 0
                sum_blue = 0
                counter = 0
                
                for py in range(-offset, offset + 1):
                    for px in range(-offset, offset + 1):
                        coord_x = x + px
                        coord_y = y + py
                        
                        if 0 <= coord_x < width and 0 <= coord_y < height:
                            index_pixel = coord_y * width + coord_x
                            r, g, b = pixels[index_pixel]
                            
                            sum_red += r
                            sum_green += g
                            sum_blue += b
                            counter += 1
                
                # Aqui calcula a média dos vizinhos
                r_avg = sum_red // total_coefficients
                g_avg = sum_green // total_coefficients
                b_avg = sum_blue // total_coefficients
                
                # Valor original do pixel central
                original_index = y * width + x
                r_orig, g_orig, b_orig = pixels[original_index]
                
                # Passa Alta é o realce = valor atual - média local
                new_r = max(0, min(255, r_orig - r_avg + 128))  # +128 para centralizar o contraste
                new_g = max(0, min(255, g_orig - g_avg + 128))
                new_b = max(0, min(255, b_orig - b_avg + 128))
                
                modifiedPixels.append((new_r, new_g, new_b))
        
        self.modifiedImage.set_pixels(modifiedPixels)
        return self.modifiedImage.get_image()
