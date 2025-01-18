from tkinter import *
from tkcalendar import DateEntry

# Cria a janela principal
root = Tk()
root.geometry("300x200")
root.title("Teste DateEntry")

# Frame para organizar o widget
frame_operacoes = Frame(root, width=300, height=200, bg="white", relief="flat")
frame_operacoes.pack(fill="both", expand=True)

# Widget DateEntry configurado para teste
e_cal_despesas = DateEntry(
    frame_operacoes, 
    width=12, 
    background="darkblue", 
    foreground="white", 
    borderwidth=2, 
    year=2025, 
    date_pattern="dd/MM/yyyy"
)
e_cal_despesas.place(x=50, y=50)

# Loop da interface gráfica
root.mainloop()