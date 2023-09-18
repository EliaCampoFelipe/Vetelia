import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from sqlite3 import Error
import os.path
from PIL import ImageTk, Image
from idiomas import leer_idioma_actual, strRellenarDatos, strDatosObligatorios, strPerroNoEncontrado, strPerroNoEncontradoPorDni, strDNIincorrecto
from idiomas import strintroduzcaDNI, strtelefonoincorrecto, strintroduzcanumerodetelefono, strintroduzcaDNIinombredelperro, strrellenarDNIielnombredelperro, strlaborables
from idiomas import strurgencias, strdatosdelpaciente, strnombre, strgenero
from idiomas import strmacho, strhembra, stredad, strpeso, strvacunado, strleishmania, strfilaria, strdatosdecontacto
from idiomas import strnombredelpropietario, strtelefono, strDNI, strbuscar, strguardar

# datos que guardamos de un perro
class DatosPerro:
    nombre_perro =''
    edad=1.0
    peso=10.0
    vacuna_leishmania = False
    vacuna_moquillo = False
    vacuna_parvovirus = False
    vacuna_filaria = False
    tipo_vacuna='puppy'

    def guardar_edad(self, e):
        self.edad = float(e)
    def guardar_peso(self, p):
        self.peso = float(p)
    def guardar_vacuna_leishmania(self, vl):
        self.vacuna_leishmania = vl
    def guardar_vacuna_moquillo(self, vm):
        self.vacuna_moquillo = vm
    def guardar_vacuna_parvovirus(self, vp):
        self.vacuna_parvovirus = vp
    def guardar_vacuna_filaria(self, vf):
        self.vacuna_filaria = vf
    def guardar(self, n, e, p, vl, vf, v):
        self.nombre_perro=n
        self.guardar_edad(e)
        self.guardar_peso(p)
        self.guardar_vacuna_leishmania(vl)
        self.guardar_vacuna_filaria(vf)
        if v == 'no':
            self.guardar_vacuna_moquillo(False)
            self.guardar_vacuna_parvovirus(False)
        elif v == 'puppy':
            self.guardar_vacuna_moquillo(True)
            self.guardar_vacuna_parvovirus(False)
        elif v == 'tetra':
            self.guardar_vacuna_moquillo(True)
            self.guardar_vacuna_parvovirus(False)
        else:
            self.guardar_vacuna_moquillo(True)
            self.guardar_vacuna_parvovirus(True)
    

perro = DatosPerro()  # global

#####################################################################################
###############      guardar ficha del perro en base de datos    ####################
#####################################################################################
def guardar_perro_bbdd(n, g, e, p, v_l, v_f, v, prop, tel, dni):
    peso = float(p)
    edad = float(e)
    bbddPath = f"{os.getcwd()}\perros.db"
    bbdd = sqlite3.connect(bbddPath)
    new_cur = bbdd.cursor()
    new_cur.execute("CREATE TABLE IF NOT EXISTS perros\
                    (propietario, dni, telefono, nombre_perro, genero, edad, peso, vacuna_leishmania, vacuna_filaria, vacunas)")
    bbdd.commit()
    res = new_cur.execute("SELECT dni, nombre_perro FROM perros WHERE dni=? AND nombre_perro=?", (dni, n))
    if res.fetchone() == None:
        new_cur.execute("INSERT INTO perros VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (prop, dni, tel, n, g, edad, peso, v_l, v_f, v))
        bbdd.commit()
    else:
        new_cur.execute("UPDATE perros SET propietario=?, dni=?, telefono=?, nombre_perro=?, genero=?, edad=?, peso=?, vacuna_leishmania=?, vacuna_filaria=?, vacunas=? WHERE dni=? AND nombre_perro=?",
                        (prop, dni, tel, n, g, edad, peso, v_l, v_f, v, dni, n) )
        bbdd.commit()
    bbdd.close()

def buscar_perro_bbdd(n, g, e, p, v_l, v_f, v, prop, tel, dni):
    bbddPath = f"{os.getcwd()}\perros.db"
    bbdd = sqlite3.connect(bbddPath)
    idioma_actual = leer_idioma_actual()
    new_cur = bbdd.cursor()
    new_cur.execute("CREATE TABLE IF NOT EXISTS perros(propietario, dni, telefono, nombre_perro, genero, edad, peso, vacuna_leishmania, vacuna_filaria, vacunas)")
    bbdd.commit()
    res = new_cur.execute("SELECT propietario, dni, telefono, nombre_perro, genero, edad, peso, vacuna_leishmania, vacuna_filaria, vacunas\
                           FROM perros WHERE dni=? AND nombre_perro=?", (dni, n))
    record = res.fetchall()
    if record == None:       
        messagebox.showerror(strPerroNoEncontrado[idioma_actual], strPerroNoEncontradoPorDni[idioma_actual]) 
        bbdd.commit()
    else:
        found = False
        for row in record:
            found = True
            prop = row[0]
            dni = row[1]
            tel= row[2]
            n = row[3]
            g = row[4]
            e = row[5]
            p = row[6]
            v_l = row[7]
            v_f = row[8]
            v = row[9]
            break
        if found == False:
             messagebox.showerror(strPerroNoEncontrado[idioma_actual], strPerroNoEncontradoPorDni[idioma_actual])        
        bbdd.commit()
        bbdd.close()
        return found, n, g, e, p, v_l, v_f, v, prop, tel, dni

#####################################################################################
###############      ficha de datos perro       #####################################
#####################################################################################
def tel_ok(tel : str):
    if len(tel) == 9:
        for i in range(0, 9):
            if tel[i].isdigit() == False:
                return False       
        return True
    return False

def dni_ok(dni : str):
    if len(dni) == 9:
        for i in range(0, 8):
            if dni[i].isdigit() == False:
                return False
        if dni[8].isalpha() == False:
            return False
        return True
    return False

def crear_ficha_datos_perro(tab_datos):
    idioma_actual = leer_idioma_actual()

    def leer_datos_perro_ficha():
        n = nombre_perro.get()
        g = genero_perro.get()
        e = float(edad.get())
        p = float(peso.get())
        v_l = vacuna_leishmania.get()
        v_f = vacuna_filaria.get()
        global perro
        v =  perro.tipo_vacuna
        prop = propietario.get()
        tel = telefono.get()
        d = dni.get()
        return n, g, e, p, v_l, v_f, v, prop, tel, d

    def guardar_perro():
        idioma_actual = leer_idioma_actual()
        n, g, e, p, v_l, v_f, v, prop, tel, d = leer_datos_perro_ficha()
        if len(d) <=0 or len(tel) <=0 or len(prop) <=0 or len(n) <=0:
            messagebox.showerror(strRellenarDatos[idioma_actual], strDatosObligatorios[idioma_actual]) 
            return
        if dni_ok(d) == False:
            messagebox.showerror(strDNIincorrecto[idioma_actual] , strintroduzcaDNI[idioma_actual]) 
            return
        if tel_ok(tel) == False:
            messagebox.showerror(strtelefonoincorrecto[idioma_actual], strintroduzcanumerodetelefono[idioma_actual]) 
            return
        guardar_perro_bbdd(n, g, e, p, v_l, v_f, v, prop, tel, d)
        global perro
        perro.guardar(n, e, p, v_l, v_f, v)

    def buscar_perro():
        idioma_actual = leer_idioma_actual()
        n, g, e, p, v_l, v_f, v, prop, tel, d = leer_datos_perro_ficha()
        if len(d) <=0 or len(n) <=0:
            messagebox.showerror(strintroduzcaDNIinombredelperro[idioma_actual], strrellenarDNIielnombredelperro[idioma_actual]) 
            return
        if dni_ok(d) == False:
            messagebox.showerror(strDNIincorrecto[idioma_actual], strrellenarDNIielnombredelperro[idioma_actual]) 
            return
        res, n, g, e, p, v_l, v_f, v, prop, tel, d = buscar_perro_bbdd(n, g, e, p, v_l, v_f, v, prop, tel, d)
        if res == True:
            nombre_perro.set(n)
            genero_perro.set(g)
            edad.set(e)
            peso.set(p)
            vacuna_leishmania.set(v_l)
            vacuna_filaria.set(v_f)
            propietario.set(prop)
            telefono.set(tel)
            dni.set(d)
            combo_vacunado.set(v)
            global perro
            perro.guardar(n, e, p, v_l, v_f, v)


    # variables de la ficha donde estan los valores introducidos  ---------------------------------------------------------------------
    nombre_perro = tk.StringVar(value='')
    genero_perro = tk.IntVar() 
    edad = tk.DoubleVar(value=1.0)
    peso = tk.DoubleVar(value=10.0)
    vacuna_leishmania = tk.BooleanVar()
    vacuna_filaria = tk.BooleanVar()
    propietario = tk.StringVar(value='')
    telefono = tk.StringVar(value='')
    dni = tk.StringVar(value='')

    def on_cambiar_leishmania():
        vl = vacuna_leishmania.get()
        global perro
        perro.guardar_vacuna_leishmania(vl)

    def on_cambiar_filaria():
        vf = vacuna_filaria.get()
        global perro
        perro.guardar_vacuna_filaria(vf)



    # ficha  ---------------------------------------------------------------------------------------------------------------------------
    idioma_actual = leer_idioma_actual()
    datos_frame = ttk.Frame(tab_datos, width=950, height=600, style='Gray.TFrame')  
    datos_frame.grid(row=0, column=0, padx=5, pady=0, sticky='nw')
    datos_frame_button = ttk.Frame(tab_datos, width=950, style='Gray.TFrame')
    datos_frame_button.grid(row=1, column=0, padx=0, pady=0)
   
    logo_frame = ttk.Frame(tab_datos, style='Ligthblue.TFrame')
    logo_frame.grid(row=0, column=1, padx=130, pady=0)
    imagePath = f"{os.getcwd()}\logo.jpg"
    img = Image.open(imagePath)
    img = img.resize((350, 480))
    img = ImageTk.PhotoImage(img)  
    logo = ttk.Label(logo_frame, image=img)
    logo.grid(row=0, column=0, padx=0, pady=0)
  
    elia = ttk.Label(logo_frame, text='     VETELIA     ',font=("Helvetica", 14, 'bold'), style='labelAzul.TLabel')
    elia.grid(row=1, column=0, padx=0, pady=0,  sticky='w')
    mail = ttk.Label(logo_frame, text='     e.campo.felipe@gmail.com    ',font=("Helvetica", 13), style='labelAzul.TLabel')
    mail.grid(row=2, column=0, padx=0, pady=5,  sticky='w')
    tel = ttk.Label(logo_frame, text= strlaborables[idioma_actual],font=("Helvetica", 13), style='labelAzul.TLabel')
    tel.grid(row=3, column=0, padx=0, pady=5,  sticky='w')
    urgencias = ttk.Label(logo_frame, text= strurgencias[idioma_actual],font=("Helvetica", 13), style='labelAzul.TLabel')
    urgencias.grid(row=4, column=0, padx=0, pady=5,  sticky='w')
       
    # datos del perro ---------------------------------------------------------------------------------------------------------------------------
    datos = ttk.Label(datos_frame, text=strdatosdelpaciente[idioma_actual], style='titulo.TLabel')
    datos.grid(column=0, row=0, padx=20, pady=20, columnspan=10)
    datos.grid_rowconfigure(30, weight=10)    
    ttk.Label(datos_frame, text=strnombre[idioma_actual], anchor=tk.W, style='titulogris.TLabel').grid(column=0, row=1, padx=10, pady=15, sticky='ew')
    
    nombre_entry = ttk.Entry(datos_frame, textvariable=nombre_perro, foreground='black', background='grey')
    nombre_entry.grid(column=1, row=1, padx=10, pady=15, sticky='ew')

    ttk.Label(datos_frame, text=strgenero[idioma_actual], style='titulogris.TLabel').grid(column=0, row=2, padx=10, pady=15, sticky='ew')
    macho = tk.Radiobutton(datos_frame, text=strmacho[idioma_actual], variable=genero_perro, 
                value=1, foreground='white', background='grey',selectcolor='gray')
    macho.grid(column=1, row=2, padx=10, pady=0,sticky='w')
    hembra = tk.Radiobutton(datos_frame, text=strhembra[idioma_actual], variable=genero_perro,
                value=2, foreground='white', background='grey',selectcolor='gray')
    hembra.grid(column=2, row=2, padx=0, pady=0,sticky='w')   
    
    ttk.Label(datos_frame, text=stredad[idioma_actual], anchor=tk.W, style='titulogris.TLabel').grid(column=0, row=5, padx=10, pady=10, sticky='ew')
    edad_entry = ttk.Entry(datos_frame, textvariable=edad, foreground='black', background='grey')
    edad_entry.grid(column=1, row=5, padx=10, pady=10, sticky='ew')
    def on_cambiar_edad(*args):
        text = edad_entry.get().lower()
        if len(text) > 0:
            global perro
            perro.guardar_edad(float(text))
    edad.trace_add("write", on_cambiar_edad)

    ttk.Label(datos_frame, text= strpeso[idioma_actual], anchor=tk.W, foreground='white', background='grey', font=("Helvetica", 14)).grid(column=0, row=6, padx=10, pady=15, sticky='ew')
    peso_entry = ttk.Entry(datos_frame, textvariable=peso, foreground='black', background='grey')
    peso_entry.grid(column=1, row=6, padx=10, pady=15, sticky='ew')
    def on_cambiar_peso(*args):
        text = peso_entry.get().lower()
        if len(text) > 0:
            global perro
            perro.guardar_peso(float(text))
    peso.trace_add("write", on_cambiar_peso)

    ttk.Label(datos_frame, text=strvacunado[idioma_actual], anchor=tk.W, style='titulogris.TLabel').grid(column=0, row=7, padx=10, pady=15, sticky='ew')
    combo_vacunado = ttk.Combobox(datos_frame, state='readonly', values=  ['no', 'puppy', 'tetra', 'penta', 'hexa'])
    combo_vacunado.grid(column=1, row=7, padx=10, pady=15)
    combo_vacunado.set('puppy')
    global perro
    perro.tipo_vacuna = 'puppy'
    def on_cambiar_vacuna(*args):
        vacunas= combo_vacunado.get()
        global perro
        perro.tipo_vacuna = vacunas
        if vacunas == 'no': 
            perro.guardar_vacuna_moquillo(False)
            perro.guardar_vacuna_parvovirus(False)
        elif vacunas == 'puppy': 
            perro.guardar_vacuna_moquillo(True)
            perro.guardar_vacuna_parvovirus(False)
        elif  vacunas == 'tetra': 
            perro.guardar_vacuna_moquillo(True)
            perro.guardar_vacuna_parvovirus(False)
        else: #penta
            perro.guardar_vacuna_moquillo(True)
            perro.guardar_vacuna_parvovirus(True)
    combo_vacunado.bind("<<ComboboxSelected>>", on_cambiar_vacuna)

    check_vacunado_leishmania = tk.Checkbutton(datos_frame,  text=strleishmania[idioma_actual], variable=vacuna_leishmania, command= on_cambiar_leishmania, foreground='white', background='grey',selectcolor='gray')
    check_vacunado_leishmania.grid(column=2, row=7, padx=0, pady=15)
    check_vacunado_filaria = tk.Checkbutton(datos_frame,  text=strfilaria[idioma_actual], variable=vacuna_filaria, command= on_cambiar_filaria, foreground='white', background='grey',selectcolor='gray')
    check_vacunado_filaria.grid(column=3, row=7, padx=0, pady=15)

    # datos del propietario  ---------------------------------------------------------------------------------------------------------------------------
    contacto = ttk.Label(datos_frame, text=strdatosdecontacto[idioma_actual], anchor=tk.W, style='titulo.TLabel')
    contacto.grid(column=0, row=8, padx=30, pady=30, columnspan=10)
    ttk.Label(datos_frame, text=strnombredelpropietario[idioma_actual], anchor=tk.W, style='titulogris.TLabel').grid(column=0, row=9, padx=10, pady=15, sticky='ew')
    propietario_entry = ttk.Entry(datos_frame, textvariable=propietario, foreground='black', background='grey')
    propietario_entry.grid(column=1, row=9, padx=10, pady=5, sticky='ew')
    ttk.Label(datos_frame, text=strtelefono[idioma_actual], anchor=tk.W, style='titulogris.TLabel').grid(column=0, row=10, padx=10, pady=5, sticky='ew')
    telefono_entry = ttk.Entry(datos_frame, textvariable=telefono, foreground='black', background='grey')
    telefono_entry.grid(column=1, row=10, padx=10, pady=5, sticky='ew')
    ttk.Label(datos_frame, text=strDNI[idioma_actual], anchor=tk.W, style='titulogris.TLabel').grid(column=0, row=11, padx=10, pady=5, sticky='ew')
    dni_entry = ttk.Entry(datos_frame, textvariable=dni, foreground='black', background='grey')
    dni_entry.grid(column=1, row=11, padx=10, pady=5, sticky='ew')

    # botones  ----------------------------------------------------------------------------------------------------------------------------------------
    ttk.Button(datos_frame_button, text=strbuscar[idioma_actual], style='Button.TButton',command=buscar_perro).grid(row=0,  column=1,  padx=20,  pady=10, sticky='ne')
    ttk.Button(datos_frame_button, text=strguardar[idioma_actual], style='Button.TButton', command=guardar_perro).grid(row=0,  column=3,  padx=50,  pady=10, sticky='ne')
    return logo_frame, logo, img
