import customtkinter as ctk
from tkinter import ttk, messagebox
from banco import *

# -------------- Turmas --------------
def criar_tela_turmas(frame):
    # -------------- Funções da interface --------------
    def carregar_dados_turmas():
        ### Atualiza a tela com os dados do banco ###
        for item in tree.get_children():
            tree.delete(item)
        for t in listar_turmas():
            id_ = t[0]
            turma = t[1]
            professor = t[2]
            turno = t[3]
            capacidade = t[4]
            sala = t[5]

            tree.insert("", "end", values=(id_, turma, professor, turno, capacidade, sala))


    def inserir_dados_turmas():
        turma = entry_turma_turmas.get().strip()
        professor = entry_professor_turmas.get().strip()
        turno = entry_turno_turmas.get().strip()
        capacidade = entry_capacidade_turmas.get().strip()
        sala = entry_sala_turmas.get().strip()

        if not turma or not turno:
            messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
            return

        cadastrar_turmas(turma, professor, turno, capacidade, sala)
        carregar_dados_turmas()
        limpar_dados_turmas()
        messagebox.showinfo("Sucesso", f"{turma} foi cadastrado!")


    def editar_dados_turmas():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma turma para editar.")
            return

        id_ = tree.item(selecionado[0], "values")[0]
        turma = entry_turma_turmas.get().strip()
        professor = entry_professor_turmas.get().strip()
        turno = entry_turno_turmas.get().strip()
        capacidade = entry_capacidade_turmas.get().strip()
        sala = entry_sala_turmas.get().strip()


        if not turma or not turno:
            messagebox.showwarning("Atenção", "Preencha corretamente os campos.")
            return

        atualizar_turmas(id_, turma, professor, turno, capacidade, sala)
        carregar_dados_turmas()
        limpar_dados_turmas()
        messagebox.showinfo("Sucesso", f"Dados de {turma} foram atualizados!")


    def excluir_dados_turmas():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma pessoa para excluir.")
            return

        id_, turma = tree.item(selecionado[0], "values")[0:2]
        if messagebox.askyesno("Confirmação", f"Excluir {turma}?"):
            excluir_turmas(id_)
            carregar_dados_turmas()
            limpar_dados_turmas()
            messagebox.showinfo("Removido", f"{turma} foi excluído.")


    def atualizar_dados_turmas():
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT id, turma, professor, turno, capacidade, sala FROM turmas")
        
        for aluno in cursor.fetchall():
            id_, turma, professor, turno, capacidade, sala = aluno
            tree.insert("", "end", values=(id_, turma, professor, turno, capacidade, sala))
        conn.close()


    def limpar_dados_turmas():
        entry_turma_turmas.delete(0, "end")
        entry_professor_turmas.delete(0, "end")
        entry_turno_turmas.delete(0, "end")
        entry_capacidade_turmas.delete(0, "end")
        entry_sala_turmas.delete(0, "end")
        tree.selection_remove(tree.selection())


    def ao_selecionar_turmas(event):
        ### Preenche os campos ao clicar numa linha ###
        selecionado = tree.selection()
        if selecionado:
            valores = tree.item(selecionado[0], "values")
            id_ = valores[0]
            turma = buscar_turmas(id_)
            entry_turma_turmas.delete(0, "end")
            entry_professor_turmas.delete(0, "end")
            entry_turno_turmas.delete(0, "end")
            entry_capacidade_turmas.delete(0, "end")
            entry_sala_turmas.delete(0, "end")
            if turma:
                entry_turma_turmas.insert(0, turma[0])
                entry_professor_turmas.insert(0, turma[1])
                entry_turno_turmas.insert(0, turma[2])
                entry_capacidade_turmas.insert(0, turma[3])
                entry_sala_turmas.insert(0, turma[4])


    entry_turma_turmas = ctk.CTkEntry(frame, placeholder_text='Turma...', width=250)
    entry_turma_turmas.pack()

    entry_professor_turmas = ctk.CTkEntry(frame, placeholder_text='Professor...', width=250)
    entry_professor_turmas.pack(pady=15)

    entry_turno_turmas = ctk.CTkEntry(frame, placeholder_text='Turno...', width=250)
    entry_turno_turmas.pack(pady=(0, 15))

    entry_capacidade_turmas = ctk.CTkEntry(frame, placeholder_text='Capacidade...', width=250)
    entry_capacidade_turmas.pack(pady=(0, 15))

    entry_sala_turmas = ctk.CTkEntry(frame, placeholder_text='Sala...', width=250)
    entry_sala_turmas.pack(pady=(0, 15))

    ctk.CTkButton(frame, text='CADASTRAR TURMA', fg_color='black', text_color='purple', width=250, 
                font=('arial bold', 14), hover_color='grey', command=inserir_dados_turmas).pack(pady=(0, 5))

    ctk.CTkButton(frame, text='EDITAR TURMA', fg_color='black', text_color='purple', width=250,
                            font=('arial bold', 14), hover_color='grey', command=editar_dados_turmas).pack(pady=(0, 5))

    ctk.CTkButton(frame, text='EXCLUIR TURMA', fg_color='black', text_color='purple', width=250,
                            font=('arial bold', 14), hover_color='grey', command=excluir_dados_turmas).pack(pady=(0, 5))

    ctk.CTkButton(frame, text='LIMPAR DADOS', fg_color='black', text_color='purple', width=250,
                            font=('arial bold', 14), hover_color='grey', command=limpar_dados_turmas).pack()


    # -------------- Treeview de turmas --------------
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

    tree = ttk.Treeview(frame_tree, columns=("ID", "Turma", "Professor", "Turno", "Capacidade", "Sala"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Turma", text="Turma")
    tree.heading("Professor", text="Professor")
    tree.heading("Turno", text="Turno")
    tree.heading("Capacidade", text="Capacidade")
    tree.heading("Sala", text="Sala")
    tree.column("ID", width=10, anchor="center")
    tree.column("Turma", width=50)
    tree.column("Professor", width=200, anchor="center")
    tree.column("Turno", anchor="center")
    tree.column("Capacidade", width=15)
    tree.column("Sala", width=100 , anchor="center")
    tree.pack(expand=True, fill="both", padx=10, pady=10)


    # -------------- Barra de rolagem de turmas --------------
    scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")

    tree.bind("<<TreeviewSelect>>", ao_selecionar_turmas)

    # -------------- Inicialização --------------
    carregar_dados_turmas()

