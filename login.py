import customtkinter as ctk
from tkinter import END, PhotoImage
from PIL import Image, ImageTk# Para redimensionar a imagem
from escolha import escolha# Importando a tela de gestão
import sqlite3
from tkinter import messagebox

class Bdd():
    def conect_db(self):
        self.con = sqlite3.connect("Cadastros.db")#conecatar ao banco
        self.cursor = self.con.cursor()
        print("Banco de dados conectao")

    def desconectar_db(self):
        self.con.close()
        print("banco off")
    
    def criar_tabela_user(self):
        self.conect_db()

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Usuarios(
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Username TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Senha TEXT NOT NULL,
                    Confirmar_senha TEXT NOT NULL
            );
        """)
        self.con.commit()
        print("Tabela criada")
        self.desconectar_db()

    def cadastrar_user(self):
        self.user_cadastro = self.cadastro_usuario.get()
        self.email_cadastro = self.cadastro_usuario_email.get()
        self.senha_cadastro = self.cadastro_senha.get()
        self.confirma_senha_cadastro = self.cadastro_confirma_senha.get()

        self.conect_db()

        self.cursor.execute(""" 
            INSERT INTO Usuarios (Username, Email, Senha, Confirmar_senha)
            VALUES (?, ?, ?, ?)""", (self.user_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))
        
        try:
            if(self.user_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
                messagebox.showerror(title="Sistema de Login", message="Por favor, preencha todos os campos.")
            elif len(self.user_cadastro) < 4:
                messagebox.showwarning("Sistema de Login", message="Usuário tem que ter pelo menos 4 caracteres.")
            elif(self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title="Sistema de Login", message="As senhas não são iguais.")
            elif len(self.senha_cadastro) < 4:
                messagebox.showwarning(title="Sistema de Login", message="A senha deve ter no minimo 4 caracteres.")
            else:
                self.con.commit()
                messagebox.showinfo(title="Sistema de Login", message=F"Bem-Vindo {self.user_cadastro}.")
                self.desconectar_db()
                self.limpa_cadastro()
        except:
            messagebox.showerror(title="Sistema de Login", message="Erro no seu Cadastro, por favor tente novamente.")
            self.desconectar_db()

    def verifica_login(self):
        self.ususario_login = self.usuario_login.get()
        self.senha_login = self.senha_login.get()
        
        self.limpa_login()

        self.cursor.execute(""" SELECT * FROM Usuarios WHERE(Username = ? AND Senha = ? )""", (self.ususario_login, self.senha_login))

        self.verifica_dados = self.cursor.fetchone()
        
        try:
            if(self.ususario_login == "" or self.senha_login == ""):
                messagebox.showerror(title="Sistema de Login", message="os campos estão vazios")
            if(self.ususario_login in self.verifica_dados and self.senha_login in self.verifica_dados):
                messagebox.showinfo(title="Sistema de Login", message=f"Bem vindo {self.ususario_login}.")
                self.desconectar_db()
        except:
            messagebox.showerror(title="Sistema de Login", message="Dados não encontrados, verifique se fez o cadastro ou se os dados estão corretor")
            self.desconectar_db()


# Classe principal
class App(ctk.CTk, Bdd):
    def __init__(self):
        super().__init__()
        self.conf_janela_principal()
        self.tela_login()
        self.criar_tabela_user()

    # Configurando janela principal
    def conf_janela_principal(self):
        self.geometry("1000x770")
        self.title("LOGIN")
        self.resizable(False, False)
        
    def tela_login(self):
        # Carregando e redimensionando a imagem
        img_original = Image.open("img/Img_login.png")
        img_redimensionada = img_original.resize((500, 500))  # Define largura e altura da imagem
        self.img = ImageTk.PhotoImage(img_redimensionada)

        # Exibindo a imagem
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=0, pady=20)  # Adicionado `pady` para afastar a imagem do topo

        # Exibindo o título
        self.title_label = ctk.CTkLabel(
            self,
            text="Faça login ou cadastre-se",
            font=("Century Gothic", 16, "bold")  # Configurando a fonte para Century Gothic
        )
        self.title_label.grid(row=0, column=0, pady=10)

        # Formulário
        self.frame_login = ctk.CTkFrame(self, width=1000, height=750)
        self.frame_login.place(x=490, y=150)

        # Colocando coisas no formulário 
        self.title_label = ctk.CTkLabel(
            self.frame_login,
            text="Faça seu login",
            font=("Century Gothic", 22, "bold")  # Configurando a fonte para Century Gothic
        )
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.usuario_login = ctk.CTkEntry(self.frame_login, width=455, placeholder_text="Seu Usuário..", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="green")
        self.usuario_login.grid(row=1, column=0, pady=10, padx=10)

        self.senha_login = ctk.CTkEntry(self.frame_login, width=455, show="*", placeholder_text="Sua Senha..", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="green")
        self.senha_login.grid(row=2, column=0, pady=10, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic", 14, "bold"), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=455, text="LOGIN", fg_color="green", hover_color="#5a5a5a", font=("Century Gothic", 16, "bold"), corner_radius=15, command=self.abrir_gestao)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)

        self.span = ctk.CTkLabel(self.frame_login, text="Se não tem cadastro, cadastre-se abaixo", font=("Century Gothic", 16, "bold"))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=455, fg_color="green", hover_color="#5a5a5a", text="FAZER CADASTRO", font=("Century Gothic", 16, "bold"), corner_radius=15, command=self.tela_cadastro)
        self.btn_cadastro.grid(row=6, column=0, pady=10, padx=10)

    def tela_cadastro(self):
        # Remover tela login
        self.frame_login.place_forget()

        self.frame_cadastro = ctk.CTkFrame(self, width=1000, height=750)
        self.frame_cadastro.place(x=490, y=150)

        # Criando coisas na tela
        self.title_label = ctk.CTkLabel(
            self.frame_cadastro,
            text="Faça seu cadastro",
            font=("Century Gothic", 22, "bold")  # Configurando a fonte para Century Gothic
        )
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.cadastro_usuario = ctk.CTkEntry(self.frame_cadastro, width=455, placeholder_text="Seu nome de usuário", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="green")
        self.cadastro_usuario.grid(row=1, column=0, pady=5, padx=10)

        self.cadastro_usuario_email = ctk.CTkEntry(self.frame_cadastro, width=455, placeholder_text="E-mail de usuário", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="green")
        self.cadastro_usuario_email.grid(row=2, column=0, pady=5, padx=10)

        self.cadastro_senha = ctk.CTkEntry(self.frame_cadastro, width=455, show="*", placeholder_text="Senha de usuário", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="green")
        self.cadastro_senha.grid(row=3, column=0, pady=5, padx=10)

        self.cadastro_confirma_senha = ctk.CTkEntry(self.frame_cadastro, width=455, show="*", placeholder_text="Confirme sua senha", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="green")
        self.cadastro_confirma_senha.grid(row=4, column=0, pady=5, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic", 14, "bold"), corner_radius=20)
        self.ver_senha.grid(row=5, column=0, pady=5, padx=10)

        self.btn_cadastrar_usu = ctk.CTkButton(self.frame_cadastro, width=455, fg_color="green", hover_color="#5a5a5a", text="CADASTRAR", font=("Century Gothic", 16, "bold"), corner_radius=15, command=self.cadastrar_user)
        self.btn_cadastrar_usu.grid(row=6, column=0, pady=5, padx=10)

        self.btn_voltar = ctk.CTkButton(self.frame_cadastro, width=455, text="VOLTAR", fg_color="red", font=("Century Gothic", 16, "bold"), corner_radius=15, command=self.tela_login)
        self.btn_voltar.grid(row=7, column=0, pady=5, padx=10)

    def limpa_cadastro(self):
        self.cadastro_usuario.delete(0, END)
        self.cadastro_usuario_email.delete(0, END)
        self.cadastro_senha.delete(0, END)
        self.cadastro_confirma_senha.delete(0, END)
    
    def limpa_login(self):
        self.usuario_login.delete(0, END)
        self.senha_login.delete(0, END)

    def abrir_gestao(self):
        # Remover a tela de login completamente, incluindo imagem e título
        self.lb_img.grid_forget()  # Escondendo a imagem
        self.title_label.grid_forget()  # Escondendo o título
        self.frame_login.place_forget()  # Removendo o frame de login
        # Fechar a janela de login (a janela principal)
        self.destroy()  # Fechando a janela principal de login
        # Criar a tela de gestão
        self.gestao = escolha()  # Cria a janela de gestão
        self.gestao.mainloop()  # Abre a tela de gestão

if __name__ == "__main__":
    app = App()
    app.mainloop()