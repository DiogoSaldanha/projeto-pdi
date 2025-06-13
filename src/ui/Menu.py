import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from utils.ImageProcessor import ImageProcessor
from utils.GeometricTransformations.Mirror import Mirror
from utils.GeometricTransformations.Rotation import Rotation
from utils.GeometricTransformations.Translation import Translation
from utils.GeometricTransformations.Scale import Scale
from utils.Filters.Grayscale import Grayscale
from utils.Filters.Brightness import Brightness
from utils.Filters.LowPass import LowPass
from utils.Filters.HighPass import HighPass
from utils.Filters.Threshold import Threshold
from utils.MathematicalMorphology.Dilatation import Dilatation
from utils.MathematicalMorphology.Erosion import Erosion

class Menu:
    def __init__(self, root):
        #Inicializando root windows e variáveis de instância
        self.root = root
        self.root.title("Processamento Digital de Imagens - Diogo Schaan Saldanha")
        self.root.geometry("800x700")
        self.original_img = None
        self.modified_img = None
        
        #cria menu bar
        self.menu_bar = tk.Menu(self.root)
        
        # Menu de Arquivo
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir Imagem", command=self.open_image)
        file_menu.add_command(label="Salvar Imagem", command=self.save_image)
        file_menu.add_command(label="Sobre", command=self.show_about)
        file_menu.add_command(label="Sair", command=self.quit_app)
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)
        
        
        # Menu de Transofrmações Geométricas
        geom_menu = tk.Menu(self.menu_bar, tearoff=0)
        geom_menu.add_command(label="Transladar", command=self.translate)
        geom_menu.add_command(label="Rotacionar", command=self.rotate)
        geom_menu.add_command(label="Espelhar", command=self.mirror)
        geom_menu.add_command(label="Aumentar", command=self.zoom_in)
        geom_menu.add_command(label="Diminuir", command=self.zoom_out)
        self.menu_bar.add_cascade(label="Transformações Geométricas", menu=geom_menu)
        
        #Menu de Filtros
        filter_menu = tk.Menu(self.menu_bar, tearoff=0)
        filter_menu.add_command(label="Grayscale", command=self.grayscale)
        filter_menu.add_command(label="Brilho", command=self.brightness)
        filter_menu.add_command(label="Passa Baixa", command=self.low_pass)
        filter_menu.add_command(label="Passa Alta", command=self.high_pass)
        filter_menu.add_command(label="Threshold", command=self.threshold)
        self.menu_bar.add_cascade(label="Filtros", menu=filter_menu)
        
        
        #Menu de Morfologia Matemática
        morph_menu = tk.Menu(self.menu_bar, tearoff=0)
        morph_menu.add_command(label="Dilatação", command=self.dilatation)
        morph_menu.add_command(label="Erosão", command=self.erosion)
        morph_menu.add_command(label="Abertura", command=self.opening)
        morph_menu.add_command(label="Fechamento", command=self.closing)
        self.menu_bar.add_cascade(label="Morfologia Matemática", menu=morph_menu)
        
        
        #Menu de Extração de Características
        extraction_menu = tk.Menu(self.menu_bar, tearoff=0)
        extraction_menu.add_command(label="DESAFIO", command=self.challenge)
        self.menu_bar.add_cascade(label="Extração de Características", menu=extraction_menu)
        
        #Opção voltar imagem original
        original_image_menu = tk.Menu(self.menu_bar,tearoff=0)
        original_image_menu.add_command(label="Voltar à Imagem Original", command=self.showOriginalImage)
        self.menu_bar.add_cascade(label="Voltar à Imagem Original", menu=original_image_menu)
        
        #Setando o menu bar pra root window
        self.root.config(menu=self.menu_bar)
        
        #Área pra mostrar a imagem, estudar melhor label pra centralizar dps etc
        self.original_img_label = tk.Label(self.root)
        self.original_img_label.pack(side=tk.LEFT, padx=20) #Não sei se o pady pode atrapalhar o display da imagem pós algoritmos
        
        self.modified_img_label = tk.Label(self.root)
        self.modified_img_label.pack(side=tk.RIGHT, padx=20)
        
    def open_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]) #Para uso no Windows
        #filepath = filedialog.askopenfilename() #Para uso no Linux
        
        if filepath:
            self.original_img = Image.open(filepath)
            self.original_img.thumbnail((400,400))
            self.modified_img = self.original_img.copy()
            self.display_image()
            
        #teste abaixo de imageprocessor para verificar se esta pegando pixels da imagem
        # if self.img:
        #     img_processor = ImageProcessor(self.img)
        #     img_mirror = Mirror(self.img)
        #     print("uma imagem foi aberta")
        #     print("\n\nPixels da imagem através da classe Mirror: \n")
        #     print(img_mirror.mirror())
            
        # if self.img:
        #     img_processor = ImageProcessor(self.img)
        #     print("uma imagem foi aberta")
        #     print("\n\nPixels da imagem através da classe ImageProccesor: \n")
        #     print(img_processor.get_pixels()[:5])
            
            
    def save_image(self):
        if self.modified_img:
            filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if filepath:
                self.modified_img.save(filepath)
                
    def show_about(self):
        messagebox.showinfo("Sobre", "Projeto de Processamento Digital de Imagens feito na Universidade Feevale. O projeto foi feito utilizando a linguagem Python com Tkinter e Pillow.")
    
    #Para mostrar a imagem na Window do Tkinter
    def display_image(self):
        if self.original_img:
            original_tk = ImageTk.PhotoImage(self.original_img)
            self.original_img_label.config(image=original_tk)
            self.original_img_label.image = original_tk
            
        if self.modified_img:
            modified_tk = ImageTk.PhotoImage(self.modified_img)
            self.modified_img_label.config(image=modified_tk)
            self.modified_img_label.image = modified_tk
    
    def quit_app(self):
        self.root.quit()
        
    def translate(self):
        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return

        x_translation = simpledialog.askinteger("Translação", "Digite o deslocamento em X:", minvalue=-self.modified_img.width, maxvalue=self.modified_img.width)
        y_translation = simpledialog.askinteger("Translação", "Digite o deslocamento em Y:", minvalue=-self.modified_img.height, maxvalue=self.modified_img.height)

        if x_translation is not None and y_translation is not None:
            print(f"Translação em X: {x_translation}, Y: {y_translation}")
            translation = Translation(self.modified_img)
            self.modified_img = translation.translate(x_translation, y_translation)
            self.display_image()
            print("Concluído translação")
        

    def rotate(self):
        print("Rotação...")
        
        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        
        angle = simpledialog.askinteger("Rotacionar Imagem", "Digite o ângulo de rotação em graus: ", minvalue=0, maxvalue=360)
        
        if angle is not None:
            print(f"Rotacionando em {angle} graus...")
            rotation = Rotation(self.modified_img)
            self.modified_img = rotation.rotate(angle)
            self.display_image()
            print("Concluído rotação")

    def mirror(self):
        print("Espelhamento...")
        
        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        
        # Pergunta ao usuário se deseja espelhamento vertical
        answer = messagebox.askyesno("Tipo de Espelhamento", "Você deseja aplicar espelhamento vertical? \n('Sim' para Espelhamento Vertical, 'Não' para Espelhamento Horizontal)")
        
        mirror = Mirror(self.modified_img)
        self.modified_img = mirror.mirror(answer)
        self.display_image()
        
        print("Concluído espelhamento")

    def zoom_in(self):
        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return

        scaling_factor = simpledialog.askfloat("Zoom In", "Digite o fator de aumento (ex: 1.2, 1.5, 2.0):", minvalue=1.01, maxvalue=5.0)

        if scaling_factor:
            print(f"Aumentando com fator {scaling_factor}...")
            scale = Scale(self.modified_img)
            self.modified_img = scale.zoom(scaling_factor)
            self.display_image()
            print("Concluído aumentar")

    def zoom_out(self):
        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return

        factor = simpledialog.askfloat("Zoom Out", "Digite o fator de redução (ex: 0.5, 0.8):", minvalue=0.1, maxvalue=0.99)

        if factor:
            print(f"Diminuindo com fator {factor}...")
            scale = Scale(self.modified_img)
            self.modified_img = scale.zoom(factor)
            self.display_image()
            print("Concluído diminuir")
        
    def grayscale(self):
        print("Grayscale...")
        
        grayscale = Grayscale(self.modified_img)
        self.modified_img = grayscale.grayscale()
        self.display_image()
        
        print("Concluído grayscale")
        
    def brightness(self):
        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return

        brightness_value = simpledialog.askinteger("Brilho", "Digite o valor de brilho (-255 a 255):", minvalue=-255, maxvalue=255)
        contrast_value = simpledialog.askfloat("Contraste", "Digite o valor de contraste (Para diminuir, valores entre 0 e 1. Para aumentar, entre 1 e 5. Ex: 1.0 = normal):", minvalue=0.0, maxvalue=5.0)

        if brightness_value is not None and contrast_value is not None:
            print(f"Aplicando brilho {brightness_value} e contraste {contrast_value}")
            brightness = Brightness(self.modified_img)
            self.modified_img = brightness.brightness(brightness=brightness_value, contrast=contrast_value)
            self.display_image()
            print("Concluído brilho e contraste")
        
    def low_pass(self):
        print("Passa baixa...")
        
        lowPass = LowPass(self.modified_img)
        self.modified_img = lowPass.low_pass()
        self.display_image()
        
        print("Concluído Passa Baixa")
        
    def high_pass(self):
        print("Passa alta...")
        
        highPass = HighPass(self.modified_img)
        self.modified_img = highPass.high_pass()
        self.display_image()
        
        print("Concluído Passa Alta (Sobel)")
        
    def threshold(self):
        if self.modified_img:
            value = simpledialog.askinteger("Threshold", "Digite o valor do threshold (0 a 255):", minvalue=0, maxvalue=255)
            if value is not None:
                print(f"Aplicando Threshold com valor {value}...")
                threshold_filter = Threshold(self.modified_img)
                self.modified_img = threshold_filter.threshold(value)
                self.display_image()
                print("Concluído Threshold")
        
    def dilatation(self):
        print("Dilatação...")

        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        
        # Aplica grayscale automaticamente antes da dilatação
        #grayscale = Grayscale(self.modified_img)
        #self.modified_img = grayscale.grayscale()

        dilation = Dilatation(self.modified_img)
        self.modified_img = dilation.dilate()
        self.display_image()

        print("Concluído dilatação")
    
    def erosion(self):
        print("Erosão...")

        if not self.modified_img:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return

        # Aplica grayscale automaticamente antes da dilatação
        #grayscale = Grayscale(self.modified_img)
        #self.modified_img = grayscale.grayscale()

        erosion = Erosion(self.modified_img)
        self.modified_img = erosion.erode()
        self.display_image()

        print("Concluído erosão")
        
    def opening(self):
        print("Abertura...")
        
    def closing(self):
        print("Fechamento...")
        
    def challenge(self):
        print("Desafio...")
        
    def showOriginalImage(self):
        if self.original_img:
            self.modified_img = self.original_img.copy()
            self.display_image()
            print("Imagem original setada com sucesso")
        else:
            messagebox.showwarning("Aviso!!!", "Nenhuma imagem foi carregada.")