import customtkinter as ctk
from tkinter import ttk, messagebox
janela = ctk.CTk()

janela._set_appearance_mode("dark")
janela.title("Treino CTK")
janela.geometry('1100x800')


ctk.CTkLabel(janela, text='  Treino CTK  ', font=("arial bold", 20), fg_color='black', text_color='purple').pack(pady=20)

tabview = ctk.CTkTabview(janela, width=1000, height=700, corner_radius=20, segmented_button_selected_color='purple', 
                         segmented_button_selected_hover_color='black')
tabview.pack()
# -------------- Funções --------------

def limpar():
    entry_nome_alunos.delete(0, "end")
    entry_datnasc_alunos.delete(0, "end")
    entry_turma_alunos.delete(0, "end")


# -------------- Alunos --------------
tabview.add('Alunos')

entry_nome_alunos = ctk.CTkEntry(tabview.tab('Alunos'), placeholder_text='Nome...', width=250)
entry_nome_alunos.pack()

entry_datnasc_alunos = ctk.CTkEntry(tabview.tab('Alunos'), placeholder_text='Data de Nascimento (DD/MM/AAAA)...', width=250)
entry_datnasc_alunos.pack(pady=15)

entry_turma_alunos = ctk.CTkEntry(tabview.tab('Alunos'), placeholder_text='Turma...', width=250)
entry_turma_alunos.pack(pady=(0, 15))

btn_cadastrar_alunos = ctk.CTkButton(tabview.tab('Alunos'), text='CADASTRAR ALUNO', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey')
btn_cadastrar_alunos.pack(pady=(0, 5))

btn_editar_alunos = ctk.CTkButton(tabview.tab('Alunos'), text='EDITAR ALUNO', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey')
btn_editar_alunos.pack(pady=(0, 5))

btn_excluir_alunos = ctk.CTkButton(tabview.tab('Alunos'), text='EXCLUIR ALUNO', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey')
btn_excluir_alunos.pack(pady=(0, 5))

btn_limpar_alunos = ctk.CTkButton(tabview.tab('Alunos'), text='LIMPAR DADOS', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey', command=limpar)
btn_limpar_alunos.pack()

style = ttk.Style(tabview.tab('Alunos'))
style.theme_use("clam")
style.configure("Treeview",
                background="grey",
                foreground="white",
                fieldbackground="grey",
                rowheight=25,
                font=("Arial", 12))

frame_tree = ctk.CTkFrame(tabview.tab('Alunos'), corner_radius=10)
frame_tree.pack(side="right", expand=True, fill="both", padx=10, pady=10)

tree = ttk.Treeview(frame_tree, columns=("ID", "Nome", "Idade", "Turma"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Turma", text="Turma")
tree.column("ID", width=10, anchor="center")
tree.column("Nome", width=200)
tree.column("Idade", width=10 , anchor="center")
tree.column("Turma")
tree.pack(expand=True, fill="both", padx=10, pady=10)


# -------------- Professores --------------
tabview.add('Professores')
prof = ctk.CTkLabel(tabview.tab("Professores"), text=('professores teste'), font=("arial bold", 16))
prof.pack()


# -------------- Turmas --------------
tabview.add('Turmas')
tur = ctk.CTkLabel(tabview.tab('Turmas'), text=('turmas teste'), font=("arial bold", 16))
tur.pack()


# -------------- Aulas --------------
tabview.add('Aulas')
aul = ctk.CTkLabel(tabview.tab('Aulas'), text=('aulas teste'), font=("arial bold", 16))
aul.pack()






janela.mainloop()
