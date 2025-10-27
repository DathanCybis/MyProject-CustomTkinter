import customtkinter as ctk
from tkinter import ttk, messagebox
from banco import *
from funcao import *
from telas import turmas, alunos
janela = ctk.CTk()

janela._set_appearance_mode("dark")
janela.title("Treino CTK")
janela.geometry('1100x800')

# -------------- Texto de cima --------------
ctk.CTkLabel(janela, text='  Treino CTK  ', font=("arial bold", 20), fg_color='black', text_color='purple').pack(pady=20)

# -------------- Tabela de seleção --------------
tabview = ctk.CTkTabview(janela, width=1000, height=700, corner_radius=20, segmented_button_selected_color='purple', 
                         segmented_button_selected_hover_color='black')
tabview.pack()

# -------------- Alunos --------------
tabview.add('Alunos')
alunos.criar_tela_alunos(tabview.tab('Alunos'))

# -------------- Professores --------------
tabview.add('Professores')
prof = ctk.CTkLabel(tabview.tab("Professores"), text=('professores teste'), font=("arial bold", 16))
prof.pack()


# -------------- Turmas -------------- ******************************************************************===============================
tabview.add('Turmas')
turmas.criar_tela_turmas(tabview.tab('Turmas'))

# -------------- Aulas --------------
tabview.add('Aulas')
aul = ctk.CTkLabel(tabview.tab('Aulas'), text=('aulas teste'), font=("arial bold", 16))
aul.pack()

#limpa_banco()

conectar_banco_alunos()
conectar_banco_turmas()


janela.mainloop()
