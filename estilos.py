
import tkinter as tk
from tkinter import ttk

def crear_estilos():
    color_fondo = 'lightblue'
    color_letra = 'blue'
    color_texto_boton = 'blue'
    color_fondo_boton = 'lightblue'

    ttk.Style().configure('Gray.TFrame', background='grey', borderwidth=1)
    ttk.Style().configure('Ligthblue.TFrame', background='lightblue', borderwidth=1)
    ttk.Style().configure('FrameBlanco.TFrame', background='white')
    ttk.Style().configure('Red.TFrame', background='red', borderwidth=1)
    
    ttk.Style().configure('Button.TButton', background=color_fondo_boton, foreground=color_texto_boton, font=('Helvetica','18','bold'),borderwidth=10)
   
    ttk.Style().configure('labelAzul.TLabel', background='lightblue')
    ttk.Style().configure('labelAzulGrande.TLabel', background='lightblue', font=("Helvetica", 12))
    ttk.Style().configure('labelBlanco.TLabel', background='white', foreground='black', font=("Helvetica", 14))
    ttk.Style().configure('labelRojo.TLabel', background= 'white', foreground= 'red', font=("Helvetica", 14))
    ttk.Style().configure('titulo.TLabel', font=("Helvetica", 14, 'bold'), foreground=color_letra, background=color_fondo)
    ttk.Style().configure('tituloazul.TLabel', font=("Helvetica", 14, 'bold'), foreground=color_letra, background='white')
    ttk.Style().configure('titulogris.TLabel', foreground='white', background='grey', font=("Helvetica", 14))
    ttk.Style().configure('labelBlancoPequeño.TLabel', background='white', foreground='black', font=("Helvetica", 8))
    ttk.Style().configure('labelBlancoMediano.TLabel', background='white', foreground='black', font=("Helvetica", 13))
    ttk.Style().configure('tituloazulPequeño.TLabel', font=("Helvetica", 8, 'bold'), foreground=color_letra, background='white')

    ttk.Style().configure('pruebas.TCheckbutton', foreground='blue', background='lightblue', font=("Helvetica", 14))
    
    ttk.Style().configure('pruebas.TRadiobutton', foreground='blue', background='lightblue', font=("Helvetica", 10))

    s_entry = ttk.Style()
    s_entry.map("EntryStyle.TEntry", foreground=[("disabled", 'blue')])
    s_entry.element_create("plain.field", "from", "clam")
    s_entry.layout("EntryStyle.TEntry",
                    [('Entry.plain.field', {'children': [(
                        'Entry.background', {'children': [(
                            'Entry.padding', {'children': [(
                                'Entry.textarea', {'sticky': 'nswe'})],
                        'sticky': 'nswe'})], 'sticky': 'nswe'})],
                        'border':'0', 'sticky': 'nswe'})])
    s_entry.configure("EntryStyle.TEntry",
                    background="lightblue", 
                    foreground="blue",
                    fieldbackground="lightblue",
                    font=("Helvetica", 14, 'bold'))

    s_notebook = ttk.Style()
    s_notebook.configure('TNotebook.Tab', font=('Helvetica','18','bold') )
    s_notebook.map("TNotebook.Tab", foreground=[("selected", 'blue')]);
