from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from tkinter.ttk import Progressbar

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tkcalendar import Calendar, DateEntry
from datetime import date

#importanto funcoes da view
from banco_view import bar_valores, grafico_pizza,porcentagem_valor,inserir_categoria, inserir_gastos, inserir_receitas,ver_categoria,tabela, deletar_gastos,deletar_receitas


class Gestao(Tk):
    def __init__(self):
        super().__init__()

        
        self.co0 = "#2e2d2b"  # Preta
        self.co1 = "#feffff"  # Branca
        self.co2 = "#4fa882"  # Verde
        self.co3 = "#38576b"  # Valor
        self.co4 = "#403d3d"  # Letra
        self.co5 = "#e06636"  # - Profit
        self.co6 = "#038cfc"  # Azul
        self.co7 = "#3fbfb9"  # Verde
        self.co8 = "#263238"  # + Verde
        self.co9 = "#e9edf5"  # Fundo

        self.colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

        self.geometry("900x650")
        self.configure(background=self.co9)
        self.resizable(False, False)



        #criando frames
        self.frame_cima = Frame(self, width=1043, height=50, bg=self.co1, relief="flat")
        self.frame_cima.grid(row=0, column=0)

        self.frame_meio = Frame(self, width=1043, height=361, bg=self.co1, pady=20, relief="raised")
        self.frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.frame_baixo = Frame(self, width=1043, height=300, bg=self.co1, relief="raised")
        self.frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

        self.frame_grafico = Frame(self.frame_meio, width=580, height=250, bg=self.co2)
        self.frame_grafico.place(x=415, y=5)

        self.frame_renda = Frame(self.frame_baixo, width=300, height=250, bg=self.co1, relief="flat")
        self.frame_renda.grid(row=0, column=0)

        self.frame_operacoes = Frame(self.frame_baixo, width=220, height=250, bg=self.co1, relief="flat")
        self.frame_operacoes.grid(row=0, column=1, padx=5)

        self.frame_configuracao = Frame(self.frame_baixo, width=300, height=250, bg=self.co1, relief="flat")
        self.frame_configuracao.grid(row=0, column=2, padx=5)


    #frame cima, trabalhando nele
        self.app_img = Image.open("img/logo_gestao.png")
        self.app_img = self.app_img.resize((45,45))
        self.app_img = ImageTk.PhotoImage(self.app_img)

        self.app_logo = Label(self.frame_cima, image=self.app_img, text=" Orçamento da Fazenda      ", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=("Verdana 20 bold"), bg=self.co1, fg=self.co4)
        self.app_logo.place(x=0, y=0)

        global tree

        self.app_tabela = Label(self.frame_meio, text="Tabela De Receitas e Despesas",  anchor=NW, font=("Verdana 12"), bg=self.co1, fg=self.co4)
        self.app_tabela.place(x=5, y=309)
        
        #frama operacoes
        self.l_descricao = Label(self.frame_operacoes, text="Inserir Novas Despesas", height=1, anchor=NW, font=("Verdana 10 bold"), bg=self.co1, fg=self.co4)
        self.l_descricao.place(x=10,y=10)
        # categoria
        self.l_categoria = Label(self.frame_operacoes, text="Categoria", height=1, anchor=NW, font=("Ivy 10 "), bg=self.co1, fg=self.co4)
        self.l_categoria.place(x=10,y=40)

        #pegando categorias
        self.categoria_funcao = ver_categoria()
        self.categoria = []
        for i in self.categoria_funcao:
            self.categoria.append(i[1])
        
        self.combo_categoria_despesas = ttk.Combobox(self.frame_operacoes, width=10, font=("Ivy 10"))
        self.combo_categoria_despesas["values"] = (self.categoria)
        self.combo_categoria_despesas.place(x=100, y=41)

        #calendario
        self.l_cal_despesas = Label(self.frame_operacoes, text="Data", height=1, anchor=NW, font=("Ivy 10 "), bg=self.co1, fg=self.co4)
        self.l_cal_despesas.place(x=10,y=70)
        self.e_cal_despesas = DateEntry(
        self.frame_operacoes, 
        width=8, 
        background="darkblue", 
        foreground="white", 
        borderwidth=2, 
        year=2025, 
        date_pattern="dd/MM/yyyy"
    )
        self.e_cal_despesas.place(x=100, y=71)

        #valor quantidade
        self.l_valor_despesas = Label(self.frame_operacoes, text="Quantia Total", height=1, anchor=NW, font=("Ivy 10 "), bg=self.co1, fg=self.co4)
        self.l_valor_despesas.place(x=10,y=105)
        self.e_valor_despesas = Entry(self.frame_operacoes, width=9, justify="left", relief="solid")
        self.e_valor_despesas.place(x=100, y=100)

        #botap inserir
        self.img_add_despessas = Image.open("img/add.png")
        self.img_add_despessas = self.img_add_despessas.resize((17,17))
        self.img_add_despessas = ImageTk.PhotoImage(self.img_add_despessas)
        self.bota_inserir_despesas = Button(self.frame_operacoes, command=self.inserir_despesas,image=self.img_add_despessas, text=" Adicionar".upper(), width=83, compound=LEFT, anchor=NW,relief=RAISED ,font=("Ivy 7 bold"), overrelief=RIDGE)
        self.bota_inserir_despesas.place(x=100, y=135)

        #botao deletar
        self.l_deletar = Label(self.frame_operacoes, text="Excluir Ação", height=1, anchor=NW, font=("Ivy 10 bold"), bg=self.co1, fg=self.co4)
        self.l_deletar.place(x=10,y=190)
        self.img_deletar = Image.open("img/deletar.png")
        self.img_deletar = self.img_deletar.resize((17,17))
        self.img_deletar = ImageTk.PhotoImage(self.img_deletar)
        self.bota_deletar = Button(self.frame_operacoes, command=self.deletar_dados,image=self.img_deletar, text=" Deletar".upper(), width=83, compound=LEFT, anchor=NW,relief=RAISED ,font=("Ivy 7 bold"), overrelief=RIDGE)
        self.bota_deletar.place(x=100, y=190)

        #confirurando receitas********************************
        self.l_receitas = Label(self.frame_configuracao, text="Inserir Novas Receitas", height=1, anchor=NW, font=("Verdana 10 bold"), bg=self.co1, fg=self.co4)
        self.l_receitas.place(x=10,y=10)

        #calendario receitas______________-----------
        self.l_cal_receitas = Label(self.frame_configuracao, text="Data", height=1, anchor=NW, font=("Ivy 10 "), bg=self.co1, fg=self.co4)
        self.l_cal_receitas.place(x=10,y=40)

        self.e_cal_receitas = DateEntry(
        self.frame_configuracao, 
        width=8, 
        background="darkblue", 
        foreground="white", 
        borderwidth=2, 
        year=2025, 
        date_pattern="dd/MM/yyyy"
    )
        self.e_cal_receitas.place(x=100, y=41)

        #valor receitas
        self.l_valor_receitas = Label(self.frame_configuracao, text="Quantia Total", height=1, anchor=NW, font=("Ivy 10 "), bg=self.co1, fg=self.co4)
        self.l_valor_receitas.place(x=10,y=70)
        self.e_valor_receitas = Entry(self.frame_configuracao, width=9, justify="left", relief="solid")
        self.e_valor_receitas.place(x=100, y=71)

        #botao adicionar
        self.img_add_receitas = Image.open("img/add.png")
        self.img_add_receitas = self.img_add_receitas.resize((17,17))
        self.img_add_receitas = ImageTk.PhotoImage(self.img_add_receitas)
        self.bota_inserir_receitas = Button(self.frame_configuracao, command=self.inserir_receitas,image=self.img_add_receitas, text=" Adicionar".upper(), width=83, compound=LEFT, anchor=NW,relief=RAISED ,font=("Ivy 7 bold"), overrelief=RIDGE)
        self.bota_inserir_receitas.place(x=100, y=111)

        
        #configuracao nova categoria_------------------
        self.l_add_categoria = Label(self.frame_configuracao, text="Categoria", height=1, anchor=NW, font=("Ivy 10 "), bg=self.co1, fg=self.co4)
        self.l_add_categoria.place(x=10,y=160)
        self.e_add_categoria = Entry(self.frame_configuracao, width=9, justify="left", relief="solid")
        self.e_add_categoria.place(x=100, y=160)

        self.img_add_categoria = Image.open("img/add.png")
        self.img_add_categoria = self.img_add_categoria.resize((17,17))
        self.img_add_categoria = ImageTk.PhotoImage(self.img_add_categoria)
        self.bota_inserir_categoria = Button(self.frame_configuracao, image=self.img_add_categoria, text=" Adicionar".upper(), width=83, compound=LEFT, anchor=NW,relief=RAISED ,font=("Ivy 7 bold"), overrelief=RIDGE, command=self.inserir_categoria_b)
        self.bota_inserir_categoria.place(x=100, y=190)


        self.porcentagem()
        self.grafico()
        self.resumo()
        self.grafico_pizza()
        self.mostrar_renda()
        
        
#porcentagem
    def porcentagem(self):
        self.l_nome = Label(self.frame_meio, text="Porcentagem da Receita Restante", height=1, anchor=NW, font=("Verdana 12"), bg=self.co1, fg=self.co4)
        self.l_nome.place(x=7, y=5)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("green.Horizontal.TProgressbar", background="green", troughcolor=self.co1, thickness=20)
        self.bar = Progressbar(self.frame_meio, length=180, style="green.Horizontal.TProgressbar", mode="determinate")

        self.bar.place(x=10, y=35)
        self.bar["value"] = porcentagem_valor()[0]

        valor = porcentagem_valor()[0]

        self.l_percentagem = Label(self.frame_meio, text="{:,.2f}%".format(valor), anchor=NW, font=("Verdana 12"), bg=self.co1, fg=self.co4)
        self.l_percentagem.place(x=200, y=35)
    
    def grafico(self):

        lista_categorias = ["Renda", "Despesas", "Saldo"]
        lista_valores = bar_valores()

        figura = plt.Figure(figsize=(4, 3.45), dpi=60)
        ax = figura.add_subplot(111)
        #ax.autoscale(enable=True, axis='both', tight=None)

        ax.bar(lista_categorias, lista_valores, color=self.colors, width=0.9)

        # Criando uma lista para coletar os dados de plt.patches
        c = 0
        # Configurando os rótulos individuais das barras
        for i in ax.patches:
            # get_x ajusta à esquerda ou direita; get_height ajusta para cima ou baixo
            ax.text(i.get_x() - .001, i.get_height() + .5,
                    str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',
                    verticalalignment='bottom', color='dimgrey')
            c += 1

        ax.set_xticklabels(lista_categorias, fontsize=16)

        ax.patch.set_facecolor('#ffffff')
        ax.spines['bottom'].set_color('#CCCCCC')
        ax.spines['bottom'].set_linewidth(1)
        ax.spines['right'].set_linewidth(0)
        ax.spines['top'].set_linewidth(0)
        ax.spines['left'].set_color('#CCCCCC')
        ax.spines['left'].set_linewidth(1)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(False, color='#EEEEEE')
        ax.xaxis.grid(False)

        canva = FigureCanvasTkAgg(figura, self.frame_meio)
        canva.get_tk_widget().place(x=10, y=70)     


    #função de resumo
    def resumo(self):
        valor = bar_valores()

        #primeiro valor
        l_linha = Label(self.frame_meio, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg="#545454")
        l_linha.place(x=309, y=52)
        l_sumario = Label(self.frame_meio, text="total Renda Mensal                      ".upper(), anchor=NW, font=("Verdana 12 "), bg=self.co1, fg="#83a9e6")
        l_sumario.place(x=309, y=35)
        l_sumario = Label(self.frame_meio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=("Arial 17"), bg=self.co1, fg="#545454")
        l_sumario.place(x=309, y=70)
        #segundo valor
        l_linha = Label(self.frame_meio, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg="#545454")
        l_linha.place(x=309, y=132)
        l_sumario = Label(self.frame_meio, text="total despesas mensais                   ".upper(), anchor=NW, font=("Verdana 12 "), bg=self.co1, fg="#83a9e6")
        l_sumario.place(x=309, y=115)
        l_sumario = Label(self.frame_meio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=("Arial 17"), bg=self.co1, fg="#545454")
        l_sumario.place(x=309, y=150)
        #terceiro valor
        l_linha = Label(self.frame_meio, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg="#545454")
        l_linha.place(x=309, y=207)
        l_sumario = Label(self.frame_meio, text="total saldo da caixa                      ".upper(), anchor=NW, font=("Verdana 12 "), bg=self.co1, fg="#83a9e6")
        l_sumario.place(x=309, y=190)
        l_sumario = Label(self.frame_meio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=("Arial 17"), bg=self.co1, fg="#545454")
        l_sumario.place(x=309, y=220)


    #grafico de pizza
    def grafico_pizza(self):
        #faça figura e atribua objetos de eixo
        figura = plt.Figure(figsize=(5, 3), dpi=90)
        ax = figura.add_subplot(111)

        lista_valores =  grafico_pizza()[1]
        lista_categorias = grafico_pizza()[0]

        #only "explode" the 2nd slice (i.e. 'Hogs')

        explode = []
        for i in lista_categorias:
            explode.append(0.05)

        ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=self.colors,shadow=True, startangle=90)
        ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

        canva_categoria = FigureCanvasTkAgg(figura, self.frame_grafico)
        canva_categoria.get_tk_widget().grid(row=0, column=0)

    
    #renda mensal(tabela)
    def mostrar_renda(self):


        #creating a treeview with dual scrollbars
        tabela_head = ['#Id','Categoria','Data','Quantia']

        lista_itens = tabela()
        
    
        global tree

        tree = ttk.Treeview(self.frame_renda, selectmode="extended",columns=tabela_head, show="headings")
        #vertical scrollbar
        vsb = ttk.Scrollbar(self.frame_renda, orient="vertical", command=tree.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(self.frame_renda, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        hd=["center","center","center", "center"]
        h=[30,100,100,100]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            #adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
        
            n+=1

        for item in lista_itens:
            tree.insert('', 'end', values=item)
    

    def inserir_categoria_b(self):
        nome = self.e_add_categoria.get()

        lista_inserir =[nome]
        for i in lista_inserir:
            if i == '':
                messagebox.showerror(title="Sistema de Gestão", message="Erro, preencha todos os campos")
                return
        #passando a lista para funcao inserir gastos presente na view
        inserir_categoria(lista_inserir)

        messagebox.showinfo(title="Sistema de Gestão", message="Os dados foram inserridos com sucesso!")

        self.e_add_categoria.delete(0, 'end')

        # Pegando valores da categoria
        categorias_funcao = ver_categoria()
        categoria = []

        for i in categorias_funcao:
            categoria.append(i[1])

        #atualizando a lista de categorias 
        self.combo_categoria_despesas["values"] = (categoria)
    
    def inserir_receitas(self):
        nome = 'Receita'
        data = self.e_cal_receitas.get()
        quantia = self.e_valor_receitas.get()

        lista_inserir = [nome, data, quantia]

        
        for i in lista_inserir:
            if i == '':
                messagebox.showerror(title="Sistema de Gestão", message="Erro, preencha todos os campos")
                return
            
        inserir_receitas(lista_inserir)

        messagebox.showinfo(title="Sistema de Gestão", message="Os dados foram inserridos com sucesso!")

        
        self.e_cal_receitas.delete(0, 'end')
        self.e_valor_receitas.delete(0, 'end')

        # Atualizando dados
        self.mostrar_renda()
        self.porcentagem()
        self.grafico_pizza()
        self.resumo()
        self.grafico()

    def inserir_despesas(self):
        nome = self.combo_categoria_despesas.get()
        data = self.e_cal_despesas.get()

        try:
            valor = float(self.e_valor_despesas.get())  # Converte para float
        except ValueError:
            messagebox.showerror(title="Sistema de Gestão", message="Erro, o valor deve ser numérico!")
            return

        lista_inserir = [nome, data, valor]

        for i in lista_inserir:
            if i == '':
                messagebox.showerror(title="Sistema de Gestão", message="Erro, preencha todos os campos")
                return

        inserir_gastos(lista_inserir)

        messagebox.showinfo(title="Sistema de Gestão", message="Os dados foram inseridos com sucesso!")

    # Limpeza dos campos
        self.combo_categoria_despesas.set('')
        self.e_cal_despesas.delete(0, 'end')
        self.e_valor_despesas.delete(0, 'end')

    # Atualização dos dados
        self.mostrar_renda()
        self.porcentagem()
        self.grafico_pizza()
        self.resumo()
        self.grafico()

    def deletar_dados(self):
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            valor = treev_lista[0]
            nome = treev_lista[1]

            if nome == 'Receita':
                deletar_receitas(valor)
                messagebox.showinfo(title="Sistema de Gestão", message="Os dados foram deletados com sucesso!")
                self.mostrar_renda()
                self.porcentagem()
                self.grafico_pizza()
                self.resumo()
                self.grafico()
            else:
                deletar_gastos(valor)
                messagebox.showinfo(title="Sistema de Gestão", message="Os dados foram deletados com sucesso!")

                self.mostrar_renda()
                self.porcentagem()
                self.grafico_pizza()
                self.resumo()
                self.grafico()
        except IndexError:
            messagebox.showerror(title="sistema de gestão", message="Erro, selecione um dos dados da tabela")

