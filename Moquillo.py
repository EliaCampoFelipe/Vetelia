from enum import Enum
import tkinter as tk
from tkinter import ttk
from enfermedades import  Enfermedad
from enfermedades import AceptarEnfermedad, RechazarEnfermedad, SiguientePrueba
from enfermedades import enfermedades_estudiadas
from idiomas import leer_idioma_actual, strmoquillo, strlagrimeoconpus, strsangradonasal, stramigdalitis
from idiomas import strdisnea, strtos, stranorexia, strvomitos, strdiarreas, strconjuntivitis
from idiomas import strulcerascornia, strheridasalmhoadillas, strulcerasconpus, strespasmos, strrigidez
from idiomas import strfiebre, strmocosoculares, stralmhodillasrugosas, strtrufainchada, strdeshidratacion
from idiomas import strneumonia, strnoapetito, strdermatitisconpus, strerupcionesenlapiel, struveitis
from idiomas import strimmunocromatografia, strElisaheces, strPCR, strdieta, stranemia, strbajaengrasas
from idiomas import strfluidoterapia, strmedicacion, strampicilinayamoxicilina, strcada8horas, str3tiposdevia
from idiomas import strdoxicilina, strcada12horas, strviaVOyIV, strcloranfenicol, strviaVOySC, strflorfenicol
from idiomas import strcada8horasdurante3_5dias, strviaIMySC, strcefapirina, strcada6_8horas, strviaIMySCyIV
from idiomas import strfenobarvital, strcada12horas_1, strviaIMyVOyIV, strdexametasonainyectable, strcada24horas
from idiomas import strmlviaIVySC, stredema, strcada24durante1dia, strviaIV, strneuritisoptica, strcada24de6_5dias
from idiomas import strvalorareutanasia

class Moquillo(Enfermedad):
    def inicializar_enfermedad(self): 
        idioma_actual = leer_idioma_actual()
        self.name = strmoquillo[idioma_actual]
        self.sintomas = [(strlagrimeoconpus[idioma_actual], 50),
                (strsangradonasal[idioma_actual], 50),
                (stramigdalitis[idioma_actual], 50),
                (strdisnea[idioma_actual], 50),
                (strtos[idioma_actual], 50),
                (stranorexia[idioma_actual], 3),
                (strvomitos[idioma_actual], 50),
                (strdiarreas[idioma_actual], 80),
                (strconjuntivitis[idioma_actual], 10),
                (strulcerascornia[idioma_actual], 50),
                (strheridasalmhoadillas[idioma_actual], 50),
                (strulcerasconpus[idioma_actual], 50),
                (strespasmos[idioma_actual], 20),
                (strrigidez[idioma_actual], 30),
                (strfiebre[idioma_actual], 40),
                (strmocosoculares[idioma_actual], 50),
                (stralmhodillasrugosas[idioma_actual], 50),
                (strtrufainchada[idioma_actual], 50),
                (strdeshidratacion[idioma_actual], 80),
                (strneumonia[idioma_actual], 50),
                (strnoapetito[idioma_actual], 20),
                (strdermatitisconpus[idioma_actual], 90),
                (strerupcionesenlapiel[idioma_actual], 80),
                (struveitis[idioma_actual], 80)]
        self.pruebas = [strimmunocromatografia[idioma_actual], strElisaheces[idioma_actual], strPCR[idioma_actual]]

    def calcular_diagnostico(self, resultado, num_prueba):
       if num_prueba == 0:
            if resultado == False:
                if self.puntos < 60:
                    return RechazarEnfermedad,0
            return SiguientePrueba,num_prueba
       elif num_prueba == 1:
            if resultado == False:
                if self.puntos < 60:
                     return RechazarEnfermedad,0
                else:
                    return SiguientePrueba,num_prueba
            else:
                return AceptarEnfermedad,0
       elif num_prueba == 2:
            if resultado == False:
                return RechazarEnfermedad,0
            else:
                return AceptarEnfermedad,0
       return RechazarEnfermedad,0
    
    def es_grave(self):
        if self.puntos > 150:
            return True
        return False
    def es_muy_grave(self):
        if self.puntos > 400:
            return True
        return False
    
    def necesita_hospitalizacion(self, renal, hepatica, anemia):
        return True
    
    def rellenar_medicacion(self, perro, ventana, renal, hepatica, anemia):
        idioma_actual = leer_idioma_actual()
        fila = 0       
        if anemia == True or hepatica != 0:
            dieta = ttk.Frame(ventana, width=200, height=100, style='FrameBlanco.TFrame')
            dieta.grid(row=1, column=0, padx=0, pady=10, sticky='nw')
            dieta.rowconfigure(5, minsize=40)
            dieta.columnconfigure(10, minsize=700)
            ttk.Label(dieta, text=strdieta[idioma_actual], style='tituloazul.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
            fila = fila + 1

        if anemia == True:
            ttk.Label(dieta, text='', style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
            ttk.Label(dieta, text=stranemia[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
            fila = fila + 1
        if hepatica != 0: 
            ttk.Label(dieta, text='', style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
            ttk.Label(dieta, text=strbajaengrasas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
            fila = fila + 1
            ttk.Label(dieta, text=strfluidoterapia[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
            fila = fila + 1

        fila = 0
        medicacion = ttk.Frame(ventana,  width=200, height=200, style='FrameBlanco.TFrame')
        medicacion.grid(row=3, column=0, padx=0, pady=10, sticky='nw')
        ttk.Label(medicacion, text=strmedicacion[idioma_actual], style='tituloazul.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        medicacion.columnconfigure(10, minsize=700)
        fila = fila + 1
           
        ttk.Label(medicacion, text=strampicilinayamoxicilina[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada8horas[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_1 = str(round(perro.peso*20,2))+str3tiposdevia[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada12horas[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_2 = str(round(perro.peso*7.5,2))+strviaVOyIV[idioma_actual]  
        ttk.Label(medicacion, text=cantidad_2, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strcloranfenicol[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada8horas[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_3 = str(round(perro.peso*20,2))+strviaVOySC[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strflorfenicol[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada8horasdurante3_5dias[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_4 = str(round(perro.peso*37.5,2))+strviaIMySC[idioma_actual]
        ttk.Label(medicacion, text=cantidad_4, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strcefapirina[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada6_8horas[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_5 = str(round(perro.peso*10,2))+strviaIMySCyIV[idioma_actual]
        ttk.Label(medicacion, text=cantidad_5, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        for i in self.sintomas_detectados:
            if i == strespasmos[idioma_actual]:
                ttk.Label(medicacion, text=strfenobarvital[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
                ttk.Label(medicacion, text=strcada12horas_1[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
                cantidad_6 =  str(round(perro.peso*2,2))+strviaIMyVOyIV[idioma_actual]
                ttk.Label(medicacion, text=cantidad_6, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
                fila = fila + 1
                break

        ttk.Label(medicacion, text=strdexametasonainyectable[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada24horas[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_9 = str(round(perro.peso*0.04,2))+strmlviaIVySC[idioma_actual]
        ttk.Label(medicacion, text=cantidad_9, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=stredema[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada24durante1dia[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_10 = str(round(perro.peso*1.5,2))+strviaIV[idioma_actual] 
        ttk.Label(medicacion, text=cantidad_10, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strneuritisoptica[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada24de6_5dias[idioma_actual], style='labelBlancoMediano.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw') 
        cantidad_11 =  str(round(perro.peso*0.1,2))+str3tiposdevia[idioma_actual]
        ttk.Label(medicacion, text=cantidad_11, style='labelBlancoMediano.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        if renal == 2 and hepatica == 2 and perro.edad > 12:
            ttk.Label(medicacion, text=strvalorareutanasia[idioma_actual], style='labelRojo.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        
      
moquillo =  Moquillo()