import tkinter as tk
from ui.Menu import Menu

def main():
    #Root window do tkinter
    root = tk.Tk()
    
    #Instância de Menu
    app = Menu(root)
    
    #Começando o main loop do tkinter pra rodar o app
    root.mainloop()
    
if __name__ == "__main__":
    main()