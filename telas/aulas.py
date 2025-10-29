import customtkinter as ctk
from tkinter import ttk, messagebox
from banco import *

# -------------- Aulas --------------
def criar_tela_aulas(frame):
# ---------------- Funções internas ----------------
    def carregar_dados_aulas():
        for item in tree.get_children():
            tree.delete(item)
        for aula in listar_aulas():
            id_ = aula[0]
            disciplina = aula[1]
            professor = aula[2]
            turma = aula[3]
            horario = aula[4]
            sala = aula[5]

            tree.insert("", "end", values=(id_, disciplina, professor, turma, horario, sala))


    def inserir_aula():
        disciplina = entry_disciplina.get().strip()
        professor = entry_professor.get().strip()
        turma = entry_turma.get().strip()
        horario = entry_horario.get().strip()
        sala = entry_sala.get().strip()

        if not all([disciplina, professor, turma, horario]):
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios!")
            return

        cadastrar_aula(disciplina, professor, turma, horario, sala)
        carregar_dados_aulas()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Aula cadastrada com sucesso!")

    def editar_aula():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma aula para editar.")
            return

        id_ = tree.item(selecionado[0], "values")[0]
        disciplina = entry_disciplina.get().strip()
        professor = entry_professor.get().strip()
        turma = entry_turma.get().strip()
        horario = entry_horario.get().strip()
        sala = entry_sala.get().strip()

        atualizar_aula(id_, disciplina, professor, turma, horario, sala)
        carregar_dados_aulas()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Aula atualizada!")

    def excluir_aula_tree():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma aula para excluir.")
            return

        id_, disciplina = tree.item(selecionado[0], "values")[0:2]
        if messagebox.askyesno("Confirmação", f"Excluir aula de {disciplina}?"):
            excluir_aula(id_)
            carregar_dados_aulas()
            limpar_campos()
            messagebox.showinfo("Removido", f"Aula de {disciplina} excluída!")

    def limpar_campos():
        entry_disciplina.delete(0, "end")
        entry_professor.delete(0, "end")
        entry_turma.delete(0, "end")
        entry_horario.delete(0, "end")
        entry_sala.delete(0, "end")
        tree.selection_remove(tree.selection())

    def ao_selecionar(event):
        selecionado = tree.selection()
        if selecionado:
            valores = tree.item(selecionado[0], "values")
            entry_disciplina.delete(0, "end")
            entry_professor.delete(0, "end")
            entry_turma.delete(0, "end")
            entry_horario.delete(0, "end")
            entry_sala.delete(0, "end")
            entry_disciplina.insert(0, valores[1])
            entry_professor.insert(0, valores[2])
            entry_turma.insert(0, valores[3])
            entry_horario.insert(0, valores[4])
            entry_sala.insert(0, valores[5])

    # ---------------- Widgets ----------------
    entry_disciplina = ctk.CTkEntry(frame, placeholder_text="* Disciplina...", width=250)
    entry_disciplina.pack()

    entry_professor = ctk.CTkEntry(frame, placeholder_text="* Professor...", width=250)
    entry_professor.pack(pady=15)

    entry_turma = ctk.CTkEntry(frame, placeholder_text="* Turma...", width=250)
    entry_turma.pack(pady=(0, 15))

    entry_horario = ctk.CTkEntry(frame, placeholder_text="* Horário...", width=250)
    entry_horario.pack(pady=(0, 15))

    entry_sala = ctk.CTkEntry(frame, placeholder_text="Sala...", width=250)
    entry_sala.pack(pady=(0, 15))

    ctk.CTkButton(frame, text="CADASTRAR AULA", fg_color="black", text_color="purple", width=250,
                font=("arial bold", 14), hover_color="grey", command=inserir_aula).pack(pady=(0, 5))

    ctk.CTkButton(frame, text="EDITAR AULA", fg_color="black", text_color="purple", width=250,
                font=("arial bold", 14), hover_color="grey", command=editar_aula).pack(pady=(0, 5))

    ctk.CTkButton(frame, text="EXCLUIR AULA", fg_color="black", text_color="purple", width=250,
                font=("arial bold", 14), hover_color="grey", command=excluir_aula_tree).pack(pady=(0, 5))

    ctk.CTkButton(frame, text="LIMPAR CAMPOS", fg_color="black", text_color="purple", width=250,
                font=("arial bold", 14), hover_color="grey", command=limpar_campos).pack()

    # ---------------- Treeview ----------------
    frame_tree = ctk.CTkFrame(frame, corner_radius=10)
    frame_tree.pack(side="bottom", expand=True, fill="both", padx=10, pady=10)

    tree = ttk.Treeview(frame_tree, columns=("ID", "Disciplina", "Professor", "Turma", "Horário", "Sala"), show="headings")
    for col in ("ID", "Disciplina", "Professor", "Turma", "Horário", "Sala"):
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree.bind("<<TreeviewSelect>>", ao_selecionar)

    # ---------------- Inicialização ----------------
    carregar_dados_aulas()
