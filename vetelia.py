#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk, messagebox
import os.path
import sys
from datos_perro import crear_ficha_datos_perro, perro
from enfermedades import  Enfermedad, enfermedades_estudiadas
from enfermedades import empezar_diagnostico, get_enfermedad_actual, get_prueba_actual, siguiente_diagnostico_internal, siguiente_enfermedad_internal
from enfermedades import AceptarEnfermedad, RechazarEnfermedad
from estilos import crear_estilos
from sintomas import crear_ficha_sintomas,inicializar_sintomas, leer_sintomas
from Filaria import filaria
from Parvovirus import parvovirus
from Leishmania import leishmania
from Moquillo import moquillo
from idiomas import cambiar_idioma, leer_idioma_actual, CASTELLANO, CATALAN
from idiomas import strMuyGrave, strleishmania, strmoquillo, strparvovirus, strfilaria, strenfermedaderronia, strenfermedaderronia2
from idiomas import stranalisisdeorinaysangre, strenfermedadrenal, strno, strsi, strGrave, strenfermedadhepatica
from idiomas import stranemiasintomas, strpruebasespecificas, strpositiva, strnegativa, strmuchos, strcastellano
from idiomas import strcatalan, strayudaaldiagnostico, strdatos, strsintomas, strpruebas, strtratamiento
from idiomas import strdiagnosticar, strposibleenfermedad, strsiguiente, stracceptaediagnostico, strhospitalizacion
from idiomas import strcirugia


root = tk.Tk()     

# enfermedades
enfermedad_mas_probable = tk.StringVar()

# medicacion
enfermedad_aceptada = tk.StringVar()
medicacion_frame = ttk.Frame()

# pruebas
indice_prueba = 0
renal_value = tk.IntVar()
hepatica_value = tk.IntVar()
anemia_value = tk.IntVar()

class PruebasDeEnfermedad:
    pruebas_nombres = []
    pruebas_valores = []
    pruebas_entries = []
    pruebas_positivas = []
    pruebas_negativas = []
    pruebas_muchos = []

    def ver_prueba(self):
        global indice_prueba
        indice_prueba = get_prueba_actual()
        self.limpiar_pruebas(indice_prueba)    
        self.pruebas_nombres[indice_prueba].set(enfermedades_estudiadas[get_enfermedad_actual()].pruebas[indice_prueba])   
        self.pruebas_entries[indice_prueba].grid()
        self.pruebas_positivas[indice_prueba].grid()
        if self.pruebas_muchos[indice_prueba] != None and enfermedades_estudiadas[get_enfermedad_actual()].name == strfilaria[idioma_actual]:
            self.pruebas_muchos[indice_prueba].grid()
        self.pruebas_negativas[indice_prueba].grid()    
        self.pruebas_valores[indice_prueba].set(-1)   
 
    def limpiar_pruebas(self, desde):
        for i in range(desde, len(self.pruebas_nombres)):
            self.pruebas_nombres[i].set('')
            self.pruebas_valores[i].set(-1)
            if self.pruebas_muchos[i] != None:
                self.pruebas_muchos[i].grid_remove()
            self.pruebas_positivas[i].grid_remove()
            self.pruebas_negativas[i].grid_remove()  

prueba = PruebasDeEnfermedad()       


def poner_enfermedad_mas_probable():
    idioma_actual = leer_idioma_actual()
    e: Enfermedad = enfermedades_estudiadas[get_enfermedad_actual()]
    global enfermedad_mas_probable
   # enfermedad_mas_probable.set(e.name + e.retornar_puntos() + e.nivel_gravedad())
    enfermedad_mas_probable.set(e.name + e.nivel_gravedad())
    if e.nivel_gravedad() == strMuyGrave[idioma_actual]:
        enfermedad_entry.config(foreground='red')
        medicacion_enfermedad_entry.config(foreground='red')
    else:
        enfermedad_entry.config(foreground='black')
        medicacion_enfermedad_entry.config(foreground='black')
    enfermedad_entry.update()
    medicacion_enfermedad_entry.update()

#####################################################################################
##############      diagnostico                 #####################################
#####################################################################################
def diagnosticar():  
    for e in enfermedades_estudiadas:
        e.init()

    s= leer_sintomas()
    for sintoma in s:
        if sintoma.valor == True:
            for e in enfermedades_estudiadas:
                e.sumar_sintoma(sintoma.nombre)

    def aplicar_vacuna(enfermedad, puntos):
        for e in enfermedades_estudiadas:
            if e.name == enfermedad:
                e.restar_puntos_por_vacuna(puntos)
                break

    global perro
    idioma_actual = leer_idioma_actual()
    if perro.vacuna_leishmania == True:
       aplicar_vacuna(strleishmania[idioma_actual], 50)
    if perro.vacuna_moquillo == True:
       aplicar_vacuna(strmoquillo[idioma_actual], 50)
    if perro.vacuna_parvovirus == True:
       aplicar_vacuna(strparvovirus[idioma_actual], 50)
    if perro.vacuna_filaria == True:
       aplicar_vacuna(strfilaria[idioma_actual], 50)

    if empezar_diagnostico() == False:
        messagebox.showerror(strenfermedaderronia[idioma_actual], strenfermedaderronia2[idioma_actual])    
        return
    poner_enfermedad_mas_probable()
    prueba.ver_prueba()
    tabControl.select(2)

#####################################################################################
##############      pruebas                     #####################################
##################################################################################### 
def prueba_positiva():
    resultado_prueba(True)
    
def prueba_negativa():
    resultado_prueba(False)

def prueba_mucho():
    enfermedades_estudiadas[get_enfermedad_actual()].muchos = True
    prueba_positiva()
    
def crear_ficha_pruebas(tab_pruebas):
    global prueba
    idioma_actual = leer_idioma_actual()
    
    prueba1_nombre = tk.StringVar()
    prueba2_nombre = tk.StringVar()
    prueba3_nombre = tk.StringVar()
    prueba4_nombre = tk.StringVar()
    prueba5_nombre = tk.StringVar()

    pruebas1_val = tk.IntVar()
    pruebas2_val = tk.IntVar()
    pruebas3_val = tk.IntVar()
    pruebas4_val = tk.IntVar()
    pruebas5_val = tk.IntVar()
    prueba.pruebas_valores.append(pruebas1_val)
    prueba.pruebas_valores.append(pruebas2_val)
    prueba.pruebas_valores.append(pruebas3_val)
    prueba.pruebas_valores.append(pruebas4_val)
    prueba.pruebas_valores.append(pruebas5_val)
   
    pruebas_frame  =  ttk.Frame(tab_pruebas,  width=200,  height=200, style='Ligthblue.TFrame')
    pruebas_frame.grid(row=1, column=0, padx=0, pady=10, sticky='nw')
    pruebas_frame.rowconfigure(3, minsize=30)
    pruebas_frame.columnconfigure(10, minsize=700)
    ttk.Label(pruebas_frame, text=stranalisisdeorinaysangre[idioma_actual], style='titulo.TLabel').grid(row=0, column=0, padx=5, pady=5,sticky='nw')
    ttk.Label(pruebas_frame, text=strenfermedadrenal[idioma_actual], style='labelAzulGrande.TLabel').grid(row=1, column=1, padx=5, pady=5,sticky='nw')
    renal_entry_no = ttk.Radiobutton(pruebas_frame, text=strno[idioma_actual], variable= renal_value, value=0, style='pruebas.TRadiobutton').grid(row=1, column=2, padx=20, pady=5)
    renal_entry_si = ttk.Radiobutton(pruebas_frame, text=strsi[idioma_actual], variable= renal_value, value=1, style='pruebas.TRadiobutton').grid(row=1, column=3, padx=20, pady=5)
    renal_entry_grave = ttk.Radiobutton(pruebas_frame, text=strGrave[idioma_actual], variable= renal_value, value=2, style='pruebas.TRadiobutton').grid(row=1, column=4, padx=20, pady=5)
    ttk.Label(pruebas_frame, text=strenfermedadhepatica[idioma_actual], style='labelAzulGrande.TLabel'). grid(row=2, column=1, padx=5, pady=5, sticky='nw')
    hepatica_entry_no = ttk.Radiobutton(pruebas_frame, text=strno[idioma_actual], variable=hepatica_value, value=0, style='pruebas.TRadiobutton').grid(row=2, column=2,padx=20, pady=5)
    hepatica_entry_Si = ttk.Radiobutton(pruebas_frame, text=strsi[idioma_actual], variable=hepatica_value, value=1, style='pruebas.TRadiobutton'). grid(row=2, column=3, padx=20, pady=5)
    hepatica_entry_grave = ttk.Radiobutton(pruebas_frame, text=strGrave[idioma_actual], variable=hepatica_value, value=2, style='pruebas.TRadiobutton').grid(row=2, column=4, padx=20, pady=5)
    ttk.Label(pruebas_frame, text=stranemiasintomas[idioma_actual], style='labelAzulGrande.TLabel'). grid(row=3, column=1, padx=5, pady=5, sticky='nw')
    anemia_entry_no = ttk.Radiobutton(pruebas_frame, text=strno[idioma_actual], variable=anemia_value, value=0, style='pruebas.TRadiobutton').grid(row=3, column=2,padx=20, pady=5)
    anemia_entry_Si = ttk.Radiobutton(pruebas_frame, text=strsi[idioma_actual], variable=anemia_value, value=1, style='pruebas.TRadiobutton'). grid(row=3, column=3, padx=20, pady=5)
        
    pruebas_especificas_frame  =  ttk.Frame(tab_pruebas,  width=200,  height=100, style='Ligthblue.TFrame')
    pruebas_especificas_frame.grid(row=2, column=0, padx=0, pady=10, sticky='nw')
    pruebas_especificas_frame.rowconfigure(5, minsize=40)
    pruebas_especificas_frame.columnconfigure(10, minsize=700)
    ttk.Label(pruebas_especificas_frame, text=strpruebasespecificas[idioma_actual], style='titulo.TLabel').grid(row=0, column=0, padx=5, pady=5,sticky='nw')
    prueba1_entry = ttk.Entry(pruebas_especificas_frame, textvariable=prueba1_nombre, style='EntryStyle.TEntry', width=50)
    prueba1_entry.grid(row=1, column=0, padx=10, pady=5, sticky='nw')
    prueba1_entry.config(state= tk.DISABLED)
    prueba1_positiva = ttk.Radiobutton(pruebas_especificas_frame, text=strpositiva[idioma_actual], variable=prueba.pruebas_valores[0], command=prueba_positiva, value=1, style='pruebas.TRadiobutton')
    prueba1_positiva.grid(row=1, column=2, padx=10, pady=0,sticky='w')
    prueba1_negativa = ttk.Radiobutton(pruebas_especificas_frame, text=strnegativa[idioma_actual], variable=prueba.pruebas_valores[0], command=prueba_negativa, value=2, style='pruebas.TRadiobutton')
    prueba1_negativa.grid(row=1, column=1, padx=10, pady=0,sticky='w')   
    #prueba1_entry.grid_remove()
    prueba1_positiva.grid_remove()
    prueba1_negativa.grid_remove()
    #global prueba
    prueba.pruebas_nombres.append(prueba1_nombre)
    prueba.pruebas_entries.append(prueba1_entry)
    prueba.pruebas_muchos.append(None)
    prueba.pruebas_positivas.append(prueba1_positiva)
    prueba.pruebas_negativas.append(prueba1_negativa)

    prueba2_entry = ttk.Entry(pruebas_especificas_frame, textvariable=prueba2_nombre, style='EntryStyle.TEntry', width=50)
    prueba2_entry.grid(row=2, column=0, padx=10, pady=5, sticky='nw')
    prueba2_entry.config(state= tk.DISABLED)
    prueba2_positiva = ttk.Radiobutton(pruebas_especificas_frame, text=strpositiva[idioma_actual], variable=prueba.pruebas_valores[1], command=prueba_positiva, value=1, style='pruebas.TRadiobutton')
    prueba2_positiva.grid(row=2, column=2, padx=10, pady=0,sticky='w')
    prueba2_negativa = ttk.Radiobutton(pruebas_especificas_frame, text=strnegativa[idioma_actual], variable=prueba.pruebas_valores[1], command=prueba_negativa, value=2, style='pruebas.TRadiobutton')
    prueba2_negativa.grid(row=2, column=1, padx=10, pady=0,sticky='w')   
    #prueba2_entry.grid_remove()
    prueba2_positiva.grid_remove()
    prueba2_negativa.grid_remove()
    prueba.pruebas_nombres.append(prueba2_nombre)
    prueba.pruebas_entries.append(prueba2_entry)
    prueba.pruebas_muchos.append(None)
    prueba.pruebas_positivas.append(prueba2_positiva)
    prueba.pruebas_negativas.append(prueba2_negativa)

    prueba3_entry = ttk.Entry(pruebas_especificas_frame, textvariable=prueba3_nombre, style='EntryStyle.TEntry', width=50)
    prueba3_entry.grid(row=3, column=0, padx=10, pady=5, sticky='nw')
    prueba3_entry.config(state= tk.DISABLED)
    prueba3_muchos = ttk.Radiobutton(pruebas_especificas_frame, text=strmuchos[idioma_actual], variable=prueba.pruebas_valores[2], command=prueba_mucho, value=3, style='pruebas.TRadiobutton')
    prueba3_muchos.grid(row=3, column=3, padx=10, pady=0,sticky='w')
    prueba3_positiva = ttk.Radiobutton(pruebas_especificas_frame, text=strpositiva[idioma_actual], variable=prueba.pruebas_valores[2], command=prueba_positiva, value=1, style='pruebas.TRadiobutton')
    prueba3_positiva.grid(row=3, column=2, padx=10, pady=0,sticky='w')   
    prueba3_negativa = ttk.Radiobutton(pruebas_especificas_frame, text=strnegativa[idioma_actual], variable=prueba.pruebas_valores[2], command=prueba_negativa, value=2, style='pruebas.TRadiobutton')
    prueba3_negativa.grid(row=3, column=1, padx=10, pady=0,sticky='w')   
    
    #prueba3_entry.grid_remove()
    prueba3_muchos.grid_remove()
    prueba3_positiva.grid_remove()
    prueba3_negativa.grid_remove()
    prueba.pruebas_nombres.append(prueba3_nombre)
    prueba.pruebas_entries.append(prueba3_entry)
    prueba.pruebas_positivas.append(prueba3_positiva)
    prueba.pruebas_negativas.append(prueba3_negativa)
    prueba.pruebas_muchos.append(prueba3_muchos)

    prueba4_entry = ttk.Entry(pruebas_especificas_frame, textvariable=prueba4_nombre, style='EntryStyle.TEntry', width=50)
    prueba4_entry.grid(row=4, column=0, padx=10, pady=5, sticky='nw')
    prueba4_entry.config(state= tk.DISABLED)
    prueba4_positiva = ttk.Radiobutton(pruebas_especificas_frame, text=strpositiva[idioma_actual], variable=prueba.pruebas_valores[3], command=prueba_positiva, value=1, style='pruebas.TRadiobutton')
    prueba4_positiva.grid(row=4, column=2, padx=10, pady=0,sticky='w')
    prueba4_negativa = ttk.Radiobutton(pruebas_especificas_frame, text=strnegativa[idioma_actual], variable=prueba.pruebas_valores[3], command=prueba_negativa, value=2, style='pruebas.TRadiobutton')
    prueba4_negativa.grid(row=4, column=1, padx=10, pady=0,sticky='w')   
    #prueba4_entry.grid_remove()
    prueba4_positiva.grid_remove()
    prueba4_negativa.grid_remove()
    prueba.pruebas_nombres.append(prueba4_nombre)
    prueba.pruebas_entries.append(prueba4_entry)
    prueba.pruebas_muchos.append(None)
    prueba.pruebas_positivas.append(prueba4_positiva)
    prueba.pruebas_negativas.append(prueba4_negativa)

    prueba5_entry = ttk.Entry(pruebas_especificas_frame, textvariable=prueba5_nombre, style='EntryStyle.TEntry', width=50)
    prueba5_entry.grid(row=5, column=0, padx=10, pady=5, sticky='nw')
    prueba5_entry.config(state= tk.DISABLED)
    prueba5_positiva = ttk.Radiobutton(pruebas_especificas_frame, text=strpositiva[idioma_actual], variable=prueba.pruebas_valores[4], command=prueba_positiva, value=1, style='pruebas.TRadiobutton')
    prueba5_positiva.grid(row=5, column=2, padx=10, pady=0,sticky='w')
    prueba5_negativa = ttk.Radiobutton(pruebas_especificas_frame, text=strnegativa[idioma_actual], variable=prueba.pruebas_valores[4], command=prueba_negativa, value=2, style='pruebas.TRadiobutton')
    prueba5_negativa.grid(row=5, column=1, padx=10, pady=0,sticky='w')       
    prueba5_positiva.grid_remove()
    prueba5_negativa.grid_remove()
    prueba.pruebas_nombres.append(prueba5_nombre)
    prueba.pruebas_entries.append(prueba5_entry)
    prueba.pruebas_muchos.append(None)
    prueba.pruebas_positivas.append(prueba5_positiva)
    prueba.pruebas_negativas.append(prueba5_negativa)

    
def error_no_hay_mas_enfermedades():
    idioma_actual = leer_idioma_actual()
    messagebox.showerror(strenfermedaderronia[idioma_actual], strenfermedaderronia2[idioma_actual])    
    global enfermedad_mas_probable
    enfermedad_mas_probable.set('')
    global prueba
    prueba.limpiar_pruebas(0)
    tabControl.select(1)

def siguiente_prueba():
    a = get_enfermedad_actual()
    if siguiente_diagnostico_internal() == False:
       error_no_hay_mas_enfermedades()
    else:
        poner_enfermedad_mas_probable()
        global prueba
        if a != get_enfermedad_actual():
            prueba.limpiar_pruebas(0)
        prueba.ver_prueba()      

def aceptar_enfermedad():
    enfermedad_aceptada.set(enfermedad_mas_probable.get()) 
    tabControl.select(3)
    limpiar_ventana_medicacion()
    global perro
    e:Enfermedad=enfermedades_estudiadas[get_enfermedad_actual()]   
    global medicacion_frame
    e.rellenar_medicacion(perro, medicacion_frame, renal_value.get(), hepatica_value.get(), anemia_value.get())
    if e.necesita_hospitalizacion(renal_value.get(), hepatica_value.get(), anemia_value.get()) == True:
         hospitalizacion_label.grid(row=0, column=5, padx=10, pady=5, sticky='nw')
    else:
         hospitalizacion_label.grid_remove()
    if e.necesita_cirugia() == True:
         cirugia_label.grid(row=0, column=6, padx=5, pady=5, sticky='nw')
    else:
         cirugia_label.grid_remove()
    
        
def siguiente_enfermedad():
    res = siguiente_enfermedad_internal()
    if res == False:
        error_no_hay_mas_enfermedades()
        return False
    poner_enfermedad_mas_probable()
    global prueba
    prueba.limpiar_pruebas(0)
    prueba.ver_prueba()      
    return True

def resultado_prueba(res):
    global indice_prueba
    indice_prueba = get_prueba_actual()
    e : Enfermedad = enfermedades_estudiadas[get_enfermedad_actual()]
    res, n_prueba = e.calcular_diagnostico(res, indice_prueba)
    if res == AceptarEnfermedad:   
        aceptar_enfermedad()
    elif res == RechazarEnfermedad:
        siguiente_enfermedad()
    else:
        siguiente_prueba()    

def limpiar_ventana_medicacion():
    global medicacion_frame
    medicacion_frame.destroy()
    crear_ventana_medicacion(tab_medicacion)

def crear_ventana_medicacion(tab):
    idioma_actual = leer_idioma_actual()
    global medicacion_frame
    medicacion_frame = ttk.Frame(tab, style='Gray.TFrame')
    medicacion_frame.grid(row=1, column=0, padx=0, pady=10, sticky='nw')

#####################################################################################
#####################################################################################
if __name__ == '__main__': 
    
    if len(sys.argv) > 1:
        idioma_actual = leer_idioma_actual()
        if sys.argv[1]== 'castellano':
            cambiar_idioma(CASTELLANO)
        elif sys.argv[1] == 'catalan':
            cambiar_idioma(CATALAN)
    idioma_actual = leer_idioma_actual()
    
    crear_estilos()
    inicializar_sintomas()
    leishmania.inicializar_enfermedad()
    parvovirus.inicializar_enfermedad()
    filaria.inicializar_enfermedad()
    moquillo.inicializar_enfermedad()
    enfermedades_estudiadas.append(leishmania)
    enfermedades_estudiadas.append(parvovirus)
    enfermedades_estudiadas.append(filaria)
    enfermedades_estudiadas.append(moquillo)
    root.geometry("970x700")
    root.resizable(0,0)
    iconPath = f"{os.getcwd()}\dog.ico"
    root.iconbitmap(iconPath)
   
    root.title(strayudaaldiagnostico[idioma_actual])
    root.config(bg="skyblue")
    
    sTab = ttk.Style()
    sTab.map('TNotebook', background= [("selected", "green3")])
   
    tabControl = ttk.Notebook(root)
    t_datos = ttk.Frame(tabControl, style='Gray.TFrame')
    tab_sintomas = ttk.Frame(tabControl, style='Gray.TFrame')
    tab_pruebas = ttk.Frame(tabControl, style='Gray.TFrame')
    tab_medicacion = ttk.Frame(tabControl, style='Gray.TFrame')
    tabControl.add(t_datos, text=strdatos[idioma_actual])
    tabControl.add(tab_sintomas, text=strsintomas[idioma_actual])
    tabControl.add(tab_pruebas, text=strpruebas[idioma_actual])
    tabControl.add(tab_medicacion, text=strtratamiento[idioma_actual])
    tabControl.pack(expand=1, fill="both")

    ##########################################################################################
    ############################# datos del perro ############################################
    ##########################################################################################
    i = leer_idioma_actual()
    logo_frame, logo, img = crear_ficha_datos_perro(t_datos)
    logo = ttk.Label(logo_frame, image=img)
   
    ##################################################################################
    # Sintomas   #####################################################################
    ##################################################################################
    crear_ficha_sintomas(tab_sintomas)
    # botones
    sintomas_frame_button  =  ttk.Frame(tab_sintomas, width=600, style='Ligthblue.TFrame')
    sintomas_frame_button.grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(sintomas_frame_button, text=strdiagnosticar[idioma_actual], style='Button.TButton', command=diagnosticar).grid(row=3,  column=0,  padx=0,  pady=0, sticky='nw')
   
    ##################################################################################
    # Pruebas       ##################################################################
    ##################################################################################
    enfermedad_frame = ttk.Frame(tab_pruebas,  width=200,  height=200, style='Ligthblue.TFrame')
    enfermedad_frame.grid(row=0, column=0, padx=0, pady=10, sticky='nw')
    enfermedad_frame.columnconfigure(10, minsize=550)
    ttk.Label(enfermedad_frame, text=strposibleenfermedad[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw')
    enfermedad_entry = ttk.Entry(enfermedad_frame, textvariable=enfermedad_mas_probable, foreground='black', background='grey', font=("Helvetica", 24), width=25)
    enfermedad_entry.grid(row=1, column=0, padx=10, pady=15, sticky='nw')
    enfermedad_entry.config(state= tk.DISABLED)
    #pruebas
    crear_ficha_pruebas(tab_pruebas)
    #botones
    pruebas_frame_button = ttk.Frame(tab_pruebas, width=600, style='Gray.TFrame')
    pruebas_frame_button.grid(row=3, column=0, padx=0, pady=5)
    ttk.Button(pruebas_frame_button, text=strsiguiente[idioma_actual], style='Button.TButton', command=siguiente_enfermedad).grid(row=0, column=0, padx=20, pady=0, sticky='ne')
    ttk.Button(pruebas_frame_button, text=stracceptaediagnostico[idioma_actual], style='Button.TButton', command=aceptar_enfermedad).grid(row=0, column=2, padx=20, pady=0, sticky='ne')

    ##################################################################################
    # Tratamiento     ################################################################
    ##################################################################################
    medicacion_enfermedad_frame = ttk.Frame(tab_medicacion,  width=200,  height=700, style='Ligthblue.TFrame')
    medicacion_enfermedad_frame.grid(row=0, column=0, padx=0, pady=10, sticky='nw')
    medicacion_enfermedad_frame.columnconfigure(250, minsize=540)
    medicacion_enfermedad_entry = ttk.Entry(medicacion_enfermedad_frame, textvariable=enfermedad_aceptada, foreground='black', background='grey', font=("Helvetica", 24), width=25)
    medicacion_enfermedad_entry.grid(row=0, column=0, padx=10, pady=5, sticky='nw')
    medicacion_enfermedad_entry.config(state= tk.DISABLED)
    hospitalizacion_label = ttk.Label(medicacion_enfermedad_frame, text=strhospitalizacion[idioma_actual], foreground='red', background='lightblue', font=("Helvetica", 24))
    hospitalizacion_label.grid(row=0, column=5, padx=4, pady=5, sticky='nw')
    hospitalizacion_label.grid_remove()
    cirugia_label = ttk.Label(medicacion_enfermedad_frame, text=strcirugia[idioma_actual], foreground='red', background='lightblue', font=("Helvetica", 24))
    cirugia_label.grid(row=0, column=6, padx=5, pady=5, sticky='nw')
    cirugia_label.grid_remove()
    crear_ventana_medicacion(tab_medicacion)
    
    ##################################################################################
    ##################################################################################
    root.mainloop()
