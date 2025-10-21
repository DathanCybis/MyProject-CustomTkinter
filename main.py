import customtkinter as ctk
from tkinter import ttk, messagebox
from banco import *

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

# -------------- Funções da interface --------------
def carregar_dados():
    ### Atualiza a tela com os dados do banco ###
    for item in tree.get_children():
        tree.delete(item)
    for pessoa in listar_alunos():
        tree.insert("", "end", values=pessoa)


def inserir_dados():
    nome = entry_nome_alunos.get().strip()
    datanasc = entry_datnasc_alunos.get().strip()
    turma = entry_turma_alunos.get().strip()

    if not nome or not turma or not datanasc.isdigit():
        messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
        return

    cadastrar_alunos(nome, datanasc, turma)
    carregar_dados()
    limpar_dados()
    messagebox.showinfo("Sucesso", f"{nome} foi cadastrado!")


def editar_dados():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma pessoa para editar.")
        return

    id_ = tree.item(selecionado[0], "values")[0]
    nome = entry_nome_alunos.get().strip()
    datanasc = entry_datnasc_alunos.get().strip()
    turma = entry_turma_alunos.get().strip()

    if not nome or not turma or not datanasc.isdigit():
        messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
        return

    atualizar_alunos(id_, nome, datanasc, turma)
    carregar_dados()
    limpar_dados()
    messagebox.showinfo("Sucesso", f"Dados de {nome} foram atualizados!")


def excluir_dados():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma pessoa para excluir.")
        return

    id_, nome = tree.item(selecionado[0], "values")[0:2]
    if messagebox.askyesno("Confirmação", f"Excluir {nome}?"):
        excluir_alunos(id_)
        carregar_dados()
        limpar_dados()
        messagebox.showinfo("Removido", f"{nome} foi excluído.")


def limpar_dados():
    entry_nome_alunos.delete(0, "end")
    entry_datnasc_alunos.delete(0, "end")
    entry_turma_alunos.delete(0, "end")
    tree.selection_remove(tree.selection())


def ao_selecionar(event):
    ### Preenche os campos ao clicar numa linha ###
    selecionado = tree.selection()
    if selecionado:
        valores = tree.item(selecionado[0], "values")
        entry_nome_alunos.delete(0, "end")
        entry_datnasc_alunos.delete(0, "end")
        entry_turma_alunos.delete(0, "end")
        entry_nome_alunos.insert(0, valores[1])
        entry_datnasc_alunos.insert(0, valores[2])
        entry_turma_alunos.insert(0, valores[3])


# -------------- Alunos --------------
tabview.add('Alunos')

entry_nome_alunos = ctk.CTkEntry(tabview.tab('Alunos'), placeholder_text='Nome...', width=250)
entry_nome_alunos.pack()

entry_datnasc_alunos = ctk.CTkEntry(tabview.tab('Alunos'), placeholder_text='Data de Nascimento (DD/MM/AAAA)...', width=250)
entry_datnasc_alunos.pack(pady=15)

entry_turma_alunos = ctk.CTkEntry(tabview.tab('Alunos'), placeholder_text='Turma...', width=250)
entry_turma_alunos.pack(pady=(0, 15))

ctk.CTkButton(tabview.tab('Alunos'), text='CADASTRAR ALUNO', fg_color='black', text_color='purple', width=250, 
              font=('arial bold', 14), hover_color='grey', command=inserir_dados).pack(pady=(0, 5))

ctk.CTkButton(tabview.tab('Alunos'), text='EDITAR ALUNO', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey', command=editar_dados).pack(pady=(0, 5))

ctk.CTkButton(tabview.tab('Alunos'), text='EXCLUIR ALUNO', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey', command=excluir_dados).pack(pady=(0, 5))

ctk.CTkButton(tabview.tab('Alunos'), text='LIMPAR DADOS', fg_color='black', text_color='purple', width=250,
                           font=('arial bold', 14), hover_color='grey', command=limpar_dados).pack()


# -------------- Treeview de alunos --------------
style = ttk.Style(tabview.tab('Alunos'))
style.theme_use("clam")
style.configure("Treeview",
                background="grey",
                foreground="white",
                fieldbackground="grey",
                rowheight=25,
                font=("Arial", 12))

frame_tree = ctk.CTkFrame(tabview.tab('Alunos'), corner_radius=10)
frame_tree.pack(side="bottom", expand=True, fill="both", padx=10, pady=10)

tree = ttk.Treeview(frame_tree, columns=("ID", "Nome", "Idade", "Turma"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Turma", text="Turma")
tree.column("ID", width=10, anchor="center")
tree.column("Nome", width=200)
tree.column("Idade", width=10 , anchor="center")
tree.column("Turma", anchor="center")
tree.pack(expand=True, fill="both", padx=10, pady=10)


# -------------- Barra de rolagem --------------
scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

tree.bind("<<TreeviewSelect>>", ao_selecionar)



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



conectar_banco()
carregar_dados()

janela.mainloop()
