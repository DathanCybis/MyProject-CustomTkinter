import customtkinter as ctk
from tkinter import ttk, messagebox
from banco import listar_professores, cadastrar_professor, atualizar_professor, excluir_professor, buscar_professor
from funcao import calcular_idade, verificar_idade

def criar_tela_professores(frame):
    # ---------------- Funções internas ----------------
    def carregar_dados_professores():
        """Atualiza a Treeview com os dados do banco"""
        for item in tree.get_children():
            tree.delete(item)
        for professor in listar_professores():
            id_ = professor[0]
            nome = professor[1]
            data_nasc = professor[2]
            especialidade = professor[3]
            telefone = professor[4]
            email = professor[5]
            idade = calcular_idade(data_nasc)

            tree.insert("", "end", values=(id_, nome, idade, especialidade, telefone, email))


    def inserir_professor():
        nome = entry_nome.get().strip()
        data_nasc = entry_data_nasc.get().strip()
        especialidade = entry_especialidade.get().strip()
        telefone = entry_telefone.get().strip()
        email = entry_email.get().strip()

        try:
            verificar_idade(data_nasc)
        except:
            messagebox.showwarning("Atenção", "Data inválida! Use DD/MM/AAAA")
            return

        if not nome or not data_nasc or not especialidade:
            messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
            return

        cadastrar_professor(nome, data_nasc, especialidade, telefone, email)
        carregar_dados_professores()
        limpar_campos()
        messagebox.showinfo("Sucesso", f"Professor {nome} foi cadastrado!")


    def editar_professor():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um professor para editar.")
            return

        id_ = tree.item(selecionado[0], "values")[0]
        nome = entry_nome.get().strip()
        data_nasc = entry_data_nasc.get().strip()
        especialidade = entry_especialidade.get().strip()
        telefone = entry_telefone.get().strip()
        email = entry_email.get().strip()

        try:
            verificar_idade(data_nasc)
        except:
            messagebox.showwarning("Atenção", "Data inválida! Use DD/MM/AAAA")
            return

        if not nome or not data_nasc or not especialidade:
            messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
            return

        atualizar_professor(id_, nome, data_nasc, especialidade, telefone, email)
        carregar_dados_professores()
        limpar_campos()
        messagebox.showinfo("Sucesso", f"Dados de {nome} foram atualizados!")


    def excluir_dados_professor():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um professor para excluir.")
            return

        id_, nome = tree.item(selecionado[0], "values")[0:2]
        if messagebox.askyesno("Confirmação", f"Excluir {nome}?"):
            excluir_professor(id_)
            carregar_dados_professores()
            limpar_campos()
            messagebox.showinfo("Removido", f"{nome} foi excluído.")

    def limpar_campos():
        entry_nome.delete(0, "end")
        entry_data_nasc.delete(0, "end")
        entry_especialidade.delete(0, "end")
        entry_telefone.delete(0, "end")
        entry_email.delete(0, "end")
        tree.selection_remove(tree.selection())


    def ao_selecionar_professor(event):
        selecionado = tree.selection()
        if selecionado:
            valores = tree.item(selecionado[0], "values")
            id_ = valores[0]
            professor = buscar_professor(id_)
            entry_nome.delete(0, "end")
            entry_data_nasc.delete(0, "end")
            entry_especialidade.delete(0, "end")
            entry_telefone.delete(0, "end")
            entry_email.delete(0, "end")
            if professor:
                entry_nome.insert(0, professor[0])
                entry_data_nasc.insert(0, professor[1])
                entry_especialidade.insert(0, professor[2])
                entry_telefone.insert(0, professor[3])
                entry_email.insert(0, professor[4])


    # ---------------- Campos de entrada ----------------
    entry_nome = ctk.CTkEntry(frame, placeholder_text="* Nome completo...", width=250)
    entry_nome.pack()

    entry_data_nasc = ctk.CTkEntry(frame, placeholder_text="* Data de Nascimento (DD/MM/AAAA)...", width=250)
    entry_data_nasc.pack(pady=15)

    entry_especialidade = ctk.CTkEntry(frame, placeholder_text="* Especialidade...", width=250)
    entry_especialidade.pack(pady=(0, 15))

    entry_telefone = ctk.CTkEntry(frame, placeholder_text="Telefone...", width=250)
    entry_telefone.pack(pady=(0, 15))

    entry_email = ctk.CTkEntry(frame, placeholder_text="E-mail...", width=250)
    entry_email.pack(pady=(0, 15))

    # ---------------- Botões ----------------
    ctk.CTkButton(frame, text="CADASTRAR PROFESSOR", fg_color="black", text_color="purple", width=250,
                  font=('arial bold', 14), hover_color="grey", command=inserir_professor).pack(pady=(0, 5))

    ctk.CTkButton(frame, text="EDITAR PROFESSOR", fg_color="black", text_color="purple", width=250,
                  font=('arial bold', 14), hover_color="grey", command=editar_professor).pack(pady=(0, 5))

    ctk.CTkButton(frame, text="EXCLUIR PROFESSOR", fg_color="black", text_color="purple", width=250,
                  font=('arial bold', 14), hover_color="grey", command=excluir_dados_professor).pack(pady=(0, 5))

    ctk.CTkButton(frame, text="LIMPAR CAMPOS", fg_color="black", text_color="purple", width=250,
                  font=('arial bold', 14), hover_color="grey", command=limpar_campos).pack()

    # ---------------- Treeview ----------------
    style = ttk.Style(frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="grey",
                    foreground="white",
                    fieldbackground="grey",
                    rowheight=25,
                    font=("Arial", 12))

    frame_tree = ctk.CTkFrame(frame, corner_radius=10)
    frame_tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree = ttk.Treeview(frame_tree, columns=("ID", "Nome", "Idade", "Especialidade", "Telefone", "E-mail"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Especialidade", text="Especialidade")
    tree.heading("Telefone", text="Telefone")
    tree.heading("E-mail", text="E-mail")
    tree.column("ID", width=40, anchor="center")
    tree.column("Nome", width=150, anchor="center")
    tree.column("Idade", width=120, anchor="center")
    tree.column("Especialidade", width=150, anchor="center")
    tree.column("Telefone", width=120, anchor="center")
    tree.column("E-mail", width=180, anchor="center")

    scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree.bind("<<TreeviewSelect>>", ao_selecionar_professor)

    # ---------------- Inicialização ----------------
    carregar_dados_professores()
