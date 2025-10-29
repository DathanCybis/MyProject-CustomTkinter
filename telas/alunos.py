import customtkinter as ctk
from tkinter import ttk, messagebox
from banco import *
from funcao import calcular_idade, verificar_idade

# -------------- Alunos --------------
def criar_tela_alunos(frame):
    # -------------- Funções internas --------------
    def carregar_dados_alunos():
        ### Atualiza a tela com os dados do banco ###
        for item in tree.get_children():
            tree.delete(item)
        for aluno in listar_alunos():
            id_ = aluno[0]
            nome = aluno[1]
            data_nasc = aluno[2]
            turma = aluno[3]
            idade = calcular_idade(data_nasc)

            tree.insert("", "end", values=(id_, nome, idade, turma))


    def inserir_dados():
        nome = entry_nome_alunos.get().strip()
        datanasc = entry_datnasc_alunos.get().strip()
        turma = entry_turma_alunos.get().strip()

        try:
            verificar_idade(datanasc)
        except:
            messagebox.showwarning("Atenção", "Data inválida! Use DD/MM/AAAA")
            return

        if not turma or not nome:
            messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
            return

        cadastrar_alunos(nome, datanasc, turma)
        carregar_dados_alunos()
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

        try:
            verificar_idade(datanasc)
        except:
            messagebox.showwarning("Atenção", "Data inválida! Use DD/MM/AAAA")
            return

        if not nome or not turma:
            messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
            return

        atualizar_alunos(id_, nome, datanasc, turma)
        carregar_dados_alunos()
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
            carregar_dados_alunos()
            limpar_dados()
            messagebox.showinfo("Removido", f"{nome} foi excluído.")


    def atualizar_dados():
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, datanasc, turma FROM alunos")
        
        for aluno in cursor.fetchall():
            id_, nome, data_nasc, turma  = aluno
            idade = calcular_idade(data_nasc)
            tree.insert("", "end", values=(id_, nome, idade, turma))
        
        conn.close()


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
            id_ = valores[0]
            aluno = buscar_alunos(id_)
            entry_nome_alunos.delete(0, "end")
            entry_datnasc_alunos.delete(0, "end")
            entry_turma_alunos.delete(0, "end")
            if aluno:
                entry_nome_alunos.insert(0, aluno[0])
                entry_datnasc_alunos.insert(0, aluno[1])
                entry_turma_alunos.insert(0, aluno[2])


    # ---------------- Campos de entrada ----------------
    entry_nome_alunos = ctk.CTkEntry(frame, placeholder_text='* Nome completo...', width=250)
    entry_nome_alunos.pack()

    entry_datnasc_alunos = ctk.CTkEntry(frame, placeholder_text='* Data de Nascimento (DD/MM/AAAA)...', width=250)
    entry_datnasc_alunos.pack(pady=15)

    entry_turma_alunos = ctk.CTkEntry(frame, placeholder_text='* Turma...', width=250)
    entry_turma_alunos.pack(pady=(0, 15))

    # -------------- Botões --------------
    ctk.CTkButton(frame, text='CADASTRAR ALUNOS', fg_color='black', text_color='purple', width=250, 
                  font=('arial bold', 14), hover_color='grey', command=inserir_dados).pack(pady=(0, 5))

    ctk.CTkButton(frame, text='EDITAR ALUNOS', fg_color='black', text_color='purple', width=250,
                  font=('arial bold', 14), hover_color='grey', command=editar_dados).pack(pady=(0, 5))
    
    ctk.CTkButton(frame, text='EXCLUIR ALUNOS', fg_color='black', text_color='purple', width=250,
                  font=('arial bold', 14), hover_color='grey', command=excluir_dados).pack(pady=(0, 5))

    ctk.CTkButton(frame, text='LIMPAR CAMPOS', fg_color='black', text_color='purple', width=250,
                  font=('arial bold', 14), hover_color='grey', command=limpar_dados).pack()


    # -------------- Treeview de alunos --------------
    style = ttk.Style(frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="grey",
                    foreground="white",
                    fieldbackground="grey",
                    rowheight=25,
                    font=("Arial", 12))

    frame_tree = ctk.CTkFrame(frame, corner_radius=10)
    frame_tree.pack(side="bottom", expand=True, fill="both", padx=10, pady=10)

    tree = ttk.Treeview(frame_tree, columns=("ID", "Nome", "Idade", "Turma"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Turma", text="Turma")
    tree.column("ID", width=10, anchor="center")
    tree.column("Nome", width=200, anchor="center")
    tree.column("Idade", width=10 , anchor="center")
    tree.column("Turma", anchor="center")

    # -------------- Barra de rolagem --------------
    scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree.bind("<<TreeviewSelect>>", ao_selecionar)

    # -------------- Inicialização --------------
    carregar_dados_alunos()
