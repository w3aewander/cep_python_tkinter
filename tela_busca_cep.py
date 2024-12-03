# -*- coding: utf-8 -*-
import ttkbootstrap as ttk, tkinter
from tkinter import messagebox

from cep import *

def fechar_app():
    root.destroy()
def preenche_endereco() -> None:
    cep = txt_cep.get().strip()
    try:
        if ( cep ):
            endereco = obter_endereco(cep)
            txt_logradouro.delete(0, tkinter.END)
            txt_logradouro.insert(0, endereco['logradouro'])
            txt_bairro.delete(0, tkinter.END)
            txt_bairro.insert(0,endereco['bairro'])
            txt_cidade.delete(0, tkinter.END)
            txt_cidade.insert(0, endereco['localidade'])
            txt_uf.delete(0, tkinter.END)
            txt_uf.insert(0, endereco['uf'])
        else:
            mostrar_mensagem('Aviso', 'Deve ser informado um cep válido')
    except:
        mostrar_mensagem('Erro','CEP não localizado ou digitado incorretamente.\nO CEP deve ter 8 dígitos.')

def mostrar_mensagem(tipo: str, msg: str):
    messagebox.showinfo(tipo, msg)

root = ttk.Window('App CEP')
frame_titulo = ttk.Frame()
lbl_titulo = ttk.Label(frame_titulo,bootstyle='default', font='Verdana', text='Buscador de endereço', background='lightblue')
lbl_titulo.pack(fill=BOTH)
frame_titulo.pack(fill=BOTH,expand=True)

frame = ttk.Frame(root)
frame.pack(fill=X, expand=True)
lbl_cep=ttk.Label(frame , text='Digite o cep(99999999)', padding=10,  width=20)
lbl_cep.pack( side=LEFT )
txt_cep = ttk.Entry(frame, bootstyle='info')
txt_cep.pack(side=LEFT, padx=5, pady=5)

frame1 = ttk.Frame(root)
frame1.pack(fill=X, expand=True)
lbl_logradouro=ttk.Label(frame1, text='Logradouro', padding=10, width=20)
lbl_logradouro.pack(side=LEFT)
txt_logradouro = ttk.Entry(frame1, width=50)
txt_logradouro.pack(side=RIGHT, padx=5, pady=5)

frame2 = ttk.Frame(root)
frame2.pack(fill=X, expand=True)
lbl_bairro=ttk.Label(frame2, text='Bairro', padding=5, width=20)
lbl_bairro.pack(side=LEFT, padx=5, pady=5)
txt_bairro = ttk.Entry(frame2, width=50)
txt_bairro.pack(side=RIGHT, padx=5, pady=5  )

frame3 = ttk.Frame(root)
frame3.pack(fill=X, expand=True)
lbl_cidade=ttk.Label(frame3, text='Cidade', padding=5, width=20)
lbl_cidade.pack(side=LEFT, padx=5, pady=5)
txt_cidade = ttk.Entry(frame3, width=50)
txt_cidade.pack(side=RIGHT, padx=5, pady=5)

frame4 = ttk.Frame(root)
frame4.pack(fill=X, expand=True)
lbl_uf=ttk.Label(frame4, text='Estado(UF)', padding=5, width=20)
lbl_uf.pack(side=LEFT, padx=5, pady=5)
txt_uf=ttk.Entry(frame4, width=50)
txt_uf.pack(side=RIGHT, padx=5, pady=5)
#
frame5 = ttk.Frame(root)
frame5.pack(side=RIGHT, padx=10)
btn_buscar = ttk.Button( frame5,text='Buscar',
                         style='SUCCESS',
                         padding=5,
                         command=preenche_endereco)


btn_fechar = ttk.Button(frame5,text='Sair',
                         style='DANGER',
                         padding=5, command=fechar_app)


btn_buscar.pack(side=LEFT, pady=5)
btn_fechar.pack(side=RIGHT, pady=5)

root.mainloop()