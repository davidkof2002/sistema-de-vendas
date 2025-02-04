import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados SQLite
Base = declarative_base()
engine = create_engine('sqlite:///vendas.db')
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)

# Modelo de Produto
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)
    estoque = Column(Integer)

# Criação das tabelas
Base.metadata.create_all(engine)

# Funções da Interface
def cadastrar_cliente():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome and telefone and email:
        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        session.add(cliente)
        session.commit()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

def cadastrar_produto():
    nome = entry_produto_nome.get()
    preco = entry_produto_preco.get()
    estoque = entry_produto_estoque.get()

    if nome and preco and estoque:
        produto = Produto(nome=nome, preco=float(preco), estoque=int(estoque))
        session.add(produto)
        session.commit()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")

# Interface Gráfica Tkinter
app = tk.Tk()
app.title("Sistema de Vendas")

# Frame para Cadastro de Clientes
frame_cliente = tk.Frame(app)
frame_cliente.pack(padx=10, pady=10)

tk.Label(frame_cliente, text="Cadastro de Cliente").grid(row=0, columnspan=2)
tk.Label(frame_cliente, text="Nome:").grid(row=1, column=0)
entry_nome = tk.Entry(frame_cliente)
entry_nome.grid(row=1, column=1)

tk.Label(frame_cliente, text="Telefone:").grid(row=2, column=0)
entry_telefone = tk.Entry(frame_cliente)
entry_telefone.grid(row=2, column=1)

tk.Label(frame_cliente, text="Email:").grid(row=3, column=0)
entry_email = tk.Entry(frame_cliente)
entry_email.grid(row=3, column=1)

tk.Button(frame_cliente, text="Cadastrar Cliente", command=cadastrar_cliente).grid(row=4, columnspan=2)

# Frame para Cadastro de Produtos
frame_produto = tk.Frame(app)
frame_produto.pack(padx=10, pady=10)

tk.Label(frame_produto, text="Cadastro de Produto").grid(row=0, columnspan=2)
tk.Label(frame_produto, text="Nome:").grid(row=1, column=0)
entry_produto_nome = tk.Entry(frame_produto)
entry_produto_nome.grid(row=1, column=1)

tk.Label(frame_produto, text="Preço:").grid(row=2, column=0)
entry_produto_preco = tk.Entry(frame_produto)
entry_produto_preco.grid(row=2, column=1)

tk.Label(frame_produto, text="Estoque:").grid(row=3, column=0)
entry_produto_estoque = tk.Entry(frame_produto)
entry_produto_estoque.grid(row=3, column=1)

tk.Button(frame_produto, text="Cadastrar Produto", command=cadastrar_produto).grid(row=4, columnspan=2)

app.mainloop()
