from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Card YU-GI-OH")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.resizable(False, False)

        self.frames = {}
        for F in (TelaInicial, TelaJogo):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame

            # coloca todas as telas na mesma posição
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame("TelaInicial")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class TelaInicial(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # carregando e redimensionando a imagem de fundo
        largura = parent.winfo_screenwidth()
        altura = parent.winfo_screenheight()
        imagem = Image.open("img/yugioh_background.jpg")
        imagem = imagem.resize((largura, altura))
        self.background_image = ImageTk.PhotoImage(imagem)

        # criando label para imagem de fundo
        background_label = Label(self, image=self.background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # botão para mudar para a TelaJogo
        button = Button(self, text="Start Game", command=lambda: controller.show_frame("TelaJogo"))
        button.place(relx=0.5, rely=0.5, anchor=CENTER)

class TelaJogo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Exemplo de conteúdo da TelaJogo
        label = Label(self, text="Tela do Jogo", font=("Helvetica", 24))
        label.pack(pady=20)

        # botão para voltar para a TelaInicial
        button = Button(self, text="Back to Start", command=lambda: controller.show_frame("TelaInicial"))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
