from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # importando Pillow

# criando a tela principal
root = Tk()

# coletando o tamanho da tela
largura = root.winfo_screenwidth()
altura = root.winfo_screenheight()

class app():
    def __init__(self):
        self.root = root
        self.configTela()
        root.mainloop()

    def configTela(self):
        self.root.title("GameCard YU-GI-OH")
        self.root.geometry(f"{largura}x{altura}")
        self.root.resizable(False, False)

        # carregando e redimensionando a imagem de fundo
        imagem = Image.open("img/yugioh_background.jpg")
        imagem = imagem.resize((largura, altura))# deixando a imagem do tamnho da tela
        self.imagem = ImageTk.PhotoImage(imagem)

        LabelImage = Label(self.root, image=self.imagem)
        LabelImage.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)

if __name__ == "__main__":
    app()
