import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from utils.ImageProcessor import ImageProcessor

class Menu:
    def __init__(self, root):
        #Inicializando root windows e variáveis de instância
        self.root = root
        self.root.title("Processamento Digital de Imagens - Diogo Schaan Saldanha")
        self.root.geometry("800x700")
        self.img = None
        
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
        
        #Setando o menu bar pra root window
        self.root.config(menu=self.menu_bar)
        
        #Área pra mostrar a imagem, estudar melhor label pra centralizar dps etc
        self.label_img = tk.Label(self.root)
        self.label_img.pack(pady=200, anchor="center") #Não sei se o pady pode atrapalhar o display da imagem pós algoritmos
        
        
    def open_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        
        if filepath:
            self.img = Image.open(filepath)
            self.img.thumbnail((400,400))
            self.display_image()
            
        #teste abaixo de imageprocessor para verificar se esta pegando pixels da imagem
        if self.img:
            img_processor = ImageProcessor(self.img)
            print("uma imagem foi aberta")
            print("\n\nPixels da imagem: \n")
            print(img_processor.get_pixels()[:5])
            
    def save_image(self):
        if self.img:
            filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if filepath:
                self.img.save(filepath)
                
    def show_about(self):
        messagebox.showinfo("Sobre", "Projeto de Processamento Digital de Imagens feito na Universidade Feevale. O projeto foi feito utilizando a linguagem Python com Tkinter e Pillow.")
    
    #Para mostrar a imagem na Window do Tkinter
    def display_image(self):
        img_tk = ImageTk.PhotoImage(self.img)
        self.label_img.config(image=img_tk)
        self.label_img.image = img_tk
    
    def quit_app(self):
        self.root.quit()
        
    def translate(self):
        print("Translação...")

    def rotate(self):
        print("Rotação...")

    def mirror(self):
        print("Espelhamento...")

    def zoom_in(self):
        print("Aumentando...")

    def zoom_out(self):
        print("Diminuindo...")
        
    def grayscale(self):
        print("Grayscale...")
        
    def low_pass(self):
        print("Passa baixa...")
        
    def high_pass(self):
        print("Passa alta...")
        
    def threshold(self):
        print("Threshold...")
        
    def dilatation(self):
        print("Dilatação...")
    
    def erosion(self):
        print("Erosão...")
        
    def opening(self):
        print("Abertura...")
        
    def closing(self):
        print("Fechamento...")
        
    def challenge(self):
        print("Desafio...")