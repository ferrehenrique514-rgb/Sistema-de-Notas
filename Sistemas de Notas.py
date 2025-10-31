import tkinter as tk
from tkinter import ttk, messagebox


#Lista para guardar os alunos
alunos = []


#Adiciona aluno na lista
def adicionar_aluno():
    turma = entrada_turma.get().strip()
    professor = entrada_professor.get().strip()
    nome = entrada_nome.get().strip()


    if not turma or not professor:
        messagebox.showwarning("Atenção", "Preencha turma e Professor.")
        return
    if not nome:
        messagebox.showwarning("Atenção", "Digite o nome do aluno.")
        return
   
    try:
        n1 = float(entrada_nota1.get())
        n2 = float(entrada_nota2.get())
        n3 = float(entrada_nota3.get())
        n4 = float(entrada_nota4.get())
    except ValueError:
        messagebox.showerror("Erro","Digite números válidos para notas.")
        return
   
    if any(n < 0 or n > 10 for n in (n1, n2, n3, n4)):
        messagebox.showerror("Erro","Digite notas entre 0 e 10.")
        return
   
    #Calcular a média
    media = (n1 + n2 + n3 + n4) / 4
    situacao = "Aprovado" if media >= 6 else "Reprovado"


    #Guardar informações
    alunos.append([nome, n1, n2, n3, n4, media, situacao])


    messagebox.showinfo("Sucesso", f"{nome} adicionado.\nMédia: {media:.2f} - {situacao}")


    #Limpar os campos (Mantem turma e professor)
    entrada_nome.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)
    entrada_nota3.delete(0, tk.END)
    entrada_nota4.delete(0, tk.END)


#Mostra as informações na tabela
def mostrar_resultados():
    turma = entrada_turma.get().strip()
    professor = entrada_professor.get().strip()
    label_turma.config(text=f"Turma: {turma}")
    label_professor.config(text=f"Professor: {professor}")


    #Limpar a tabela antes de preencher
    for item in tabela.get_children():
        tabela.delete(item)


    for aluno in alunos:
        cor = "Aprovado" if aluno[6] == "Aprovado" else "Reprovado"
        tabela.insert("", tk.END, values=aluno, tags=(cor,))


    tabela.tag_configure("Aprovado", foreground="green")
    tabela.tag_configure("Reprovado", foreground="red")




#Cria janela principal
janela = tk.Tk()
janela.title("Sistema de Notas")
janela.geometry("800x500")


#Linha da turma e professor
tk.Label(janela, text="Turma: ").grid(row=0, column=0, padx=6, pady=8, sticky="e")
entrada_turma = tk.Entry(janela, width=25)
entrada_turma.grid(row=0, column=1, padx=6, pady=8, sticky="w")


tk.Label(janela, text="Professor: ").grid(row=0, column=2, padx=6, pady=8, sticky="e")
entrada_professor = tk.Entry(janela, width=25)
entrada_professor.grid(row=0, column=3, padx=6, pady=8, sticky="w")


#Linha nome do aluno
tk.Label(janela, text="Nome do aluno: ").grid(row=1, column=0, padx=6, pady=8, sticky="e")
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.grid(row=1, column=1, padx=6, pady=8, sticky="w")


#Linhas das notas
tk.Label(janela, text="Nota1: ").grid(row=2, column=0, padx=6, sticky="e")
entrada_nota1 = tk.Entry(janela, width=8)
entrada_nota1.grid(row=2, column=1, padx=6, sticky="w")


tk.Label(janela, text="Nota2: ").grid(row=2, column=2, padx=6, sticky="e")
entrada_nota2 = tk.Entry(janela, width=8)
entrada_nota2.grid(row=2, column=3, padx=6, sticky="w")


tk.Label(janela, text="Nota3: ").grid(row=3, column=0, padx=6, sticky="e")
entrada_nota3 = tk.Entry(janela, width=8)
entrada_nota3.grid(row=3, column=1, padx=6, sticky="w")


tk.Label(janela, text="Nota4: ").grid(row=3, column=2, padx=6, sticky="e")
entrada_nota4 = tk.Entry(janela, width=8)
entrada_nota4.grid(row=3, column=3, padx=6, sticky="w")


#Botões
btn_adicionar = tk.Button(janela, text="Adicionar", width=15, command=adicionar_aluno)
btn_adicionar.grid(row=4, column=1, pady=12)


btn_mostrar = tk.Button(janela, text="Mostrar Resultado",width=18, command=mostrar_resultados)
btn_mostrar.grid(row=4, column=2, pady=12)


#Mostrar turma/ professor na area de resultados
label_turma = tk.Label(janela, text="Turma: ")
label_turma.grid(row=5, column=0, columnspan=2, sticky="w", padx=6)


label_professor= tk.Label(janela, text="Professor: ")
label_professor.grid(row=5, column=2, columnspan=2, sticky="w", padx=6)


#Tabela para exibir resultados
colunas = ("Nome", "N1", "N2", "N3", "N4", "Média", "Situação",)
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=12)
for c in colunas:
    tabela.heading(c, text=c)
#Ajuste das larguras
tabela.column("Nome", width=220)
tabela.column("N1", width=60, anchor="center")
tabela.column("N2", width=60, anchor="center")
tabela.column("N3", width=60, anchor="center")
tabela.column("N4", width=60, anchor="center")
tabela.column("Média", width=80, anchor="center")
tabela.column("Situação", width=100, anchor="center")


tabela.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


#Permitir que a tabela cresça com a janela
janela.grid_rowconfigure(6, weight=1)
janela.grid_columnconfigure(3, weight=1)


janela.mainloop()