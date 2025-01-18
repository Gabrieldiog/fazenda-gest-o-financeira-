import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
from gestao import Gestao  # Importação direta porque não há ciclo aqui


class escolha(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tela_principal()
        self.gestao_financeira()
        self.cadastro_de_coisas()
        self.voltar_login()

    def tela_principal(self):
        self.geometry("540x390")
        self.title("Escolha o seu destino!")
        self.resizable(False, False)

    def gestao_financeira(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="  Ir para gestão  ",
            font=("Century Gothic", 16, "bold")  # Configurando a fonte para Century Gothic
        )
        self.title_label.grid(row=1, column=1, pady=10)
        self.title_label.place(x=85, y=50)

        self.frame_gestao = ctk.CTkFrame(self, width=150, height=150)
        self.frame_gestao.place(x=65, y=95)

        img_original = Image.open("img/gestao.png")
        img_redimensionada = img_original.resize((150, 150))  # Define largura e altura da imagem
        self.img_gestao = ImageTk.PhotoImage(img_redimensionada)

        # Exibindo a imagem
        self.lb_img = ctk.CTkLabel(self.frame_gestao, text=None, image=self.img_gestao)
        self.lb_img.grid(row=1, column=0, padx=0, pady=0)

        self.btn_gestao = ctk.CTkButton(
            self.frame_gestao,
            width=150,
            text="Gestão",
            fg_color="green",
            hover_color="#5a5a5a",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15,
            command=self.APP_gestao
        )
        self.btn_gestao.grid(row=2, column=0, pady=10, padx=10)

    def cadastro_de_coisas(self):
        self.title_label_cadastro = ctk.CTkLabel(
            self,
            text="  Cadastrar",
            font=("Century Gothic", 16, "bold")  # Configurando a fonte para Century Gothic
        )
        self.title_label_cadastro.grid(row=1, column=1, pady=10)
        self.title_label_cadastro.place(x=370, y=50)

        self.frame_cadastro = ctk.CTkFrame(self, width=150, height=150)
        self.frame_cadastro.place(x=330, y=95)

        img_original = Image.open("img/cadastro.png")
        img_redimensionada = img_original.resize((150, 150))  # Define largura e altura da imagem
        self.img_cadastro = ImageTk.PhotoImage(img_redimensionada)

        # Exibindo a imagem
        self.lb_img_cadastro = ctk.CTkLabel(self.frame_cadastro, text=None, image=self.img_cadastro)
        self.lb_img_cadastro.grid(row=1, column=0, padx=0, pady=0)

        self.btn_cadastrar = ctk.CTkButton(
            self.frame_cadastro,
            width=150,
            text="Cadastrar",
            fg_color="green",
            hover_color="#5a5a5a",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.btn_cadastrar.grid(row=2, column=0, pady=10, padx=10)

    def voltar_login(self):
        self.frame_voltar = ctk.CTkFrame(self, width=150, height=150)
        self.frame_voltar.place(x=200, y=310)

        self.btn_voltar = ctk.CTkButton(
            self.frame_voltar,
            width=150,
            text="Voltar",
            fg_color="red",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15,
            command=self.ir_para_login
        )
        self.btn_voltar.grid(row=1, column=0, pady=10, padx=10)

    def ir_para_login(self):
        from login import App  # Importação atrasada para evitar ciclo
        self.destroy()  # Fecha a janela atual
        app_login = App()  # Cria uma nova instância da classe de login
        app_login.mainloop()  # Mostra a tela de login

    def APP_gestao(self):
        self.lb_img.grid_forget()
        self.title_label.grid_forget()
        self.frame_gestao.place_forget()
        self.frame_cadastro.place_forget()
        self.destroy()
        self.gestao = Gestao()  # Cria a janela de gestão
        self.gestao.mainloop()  # Abre a tela de gestão