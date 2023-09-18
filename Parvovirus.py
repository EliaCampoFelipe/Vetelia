from enum import Enum
import tkinter as tk
from tkinter import ttk
from enfermedades import  Enfermedad
from enfermedades import AceptarEnfermedad, RechazarEnfermedad, SiguientePrueba
from enfermedades import enfermedades_estudiadas
from idiomas import leer_idioma_actual, strparvovirus, strnoapetito, strvomitosseveros, strfiebre, strdeshidratacion
from idiomas import strdiarreasconsangre, strclorrojoalrededordelaboca, strlatidosintensos, struveitis
from idiomas import strpruebadeantigenossangre, strtestElisa, strPCRheces, strdieta, stranemia, strobligaracomer
from idiomas import strbajaengrasas, strfluidoterapia, strcontroldevomitos, strmedicacion, strmetronidrazol
from idiomas import strBID, strviaIV, strefovencina, strcada24horas, strviaSC, strmaropitan, strbuprenofina
from idiomas import strcad8horas_1, strsuplementos, strcada6horas, strml, strjarabe, strmlVO, strtamiflu
from idiomas import strcada24horasduraante10dias, strml, strvalorareutanasia

class Parvovirus(Enfermedad):
    def inicializar_enfermedad(self): 
        idioma_actual = leer_idioma_actual()
        self.name = strparvovirus[idioma_actual]
        self.sintomas = [(strnoapetito[idioma_actual], 10),
                (strvomitosseveros[idioma_actual], 200),
                (strfiebre[idioma_actual], 10),
                (strdeshidratacion[idioma_actual], 80),
                (strdiarreasconsangre[idioma_actual], 200),
                (strclorrojoalrededordelaboca[idioma_actual], 70),
                (strlatidosintensos[idioma_actual], 10),
                (struveitis[idioma_actual], 20)
               ]
        self.pruebas = [strpruebadeantigenossangre[idioma_actual],strtestElisa[idioma_actual], strPCRheces[idioma_actual]]

    def calcular_diagnostico(self,  resultado, num_prueba):      
      if num_prueba == 0:
          if resultado == False:
              if self.puntos < 80:
                  return RechazarEnfermedad,0
              else:
                  return SiguientePrueba,num_prueba
          else:
             return AceptarEnfermedad,0
      elif num_prueba == 1:
          if resultado == False:
             return SiguientePrueba,num_prueba
          else:
             return AceptarEnfermedad,0
      elif num_prueba == 2:
          if resultado == False:
              return RechazarEnfermedad,0
          else:
              return AceptarEnfermedad,0

    def es_grave(self):
        return True
    def es_muy_grave(self):
        if self.puntos > 400:
            return True
        return False
    def necesita_hospitalizacion(self, renal, hepatica, anemia):
        return True
    
    def rellenar_medicacion(self, perro, ventana, renal, hepatica, anemia):
        idioma_actual = leer_idioma_actual()
        fila = 0
        dieta = ttk.Frame(ventana, width=200, height=100, style='FrameBlanco.TFrame')
        dieta.grid(row=1, column=0, padx=0, pady=10, sticky='nw')
        dieta.rowconfigure(5, minsize=40)
        dieta.columnconfigure(10, minsize=700)
        ttk.Label(dieta, text=strdieta[idioma_actual], style='tituloazul.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        fila = fila + 1
       
        ttk.Label(dieta, text=stranemia[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        ttk.Label(dieta, text=strobligaracomer[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        ttk.Label(dieta, text=strbajaengrasas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        ttk.Label(dieta, text=strfluidoterapia[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        ttk.Label(dieta, text=strcontroldevomitos[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        
        fila = 0
        medicacion = ttk.Frame(ventana,  width=200, height=200, style='FrameBlanco.TFrame')
        medicacion.grid(row=3, column=0, padx=0, pady=10, sticky='nw')
        ttk.Label(medicacion, text=strmedicacion[idioma_actual], style='tituloazul.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        medicacion.columnconfigure(10, minsize=700)
        fila = fila + 1
        
        ttk.Label(medicacion, text=strmetronidrazol[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0,padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strBID[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_1 = str(round(perro.peso*25,2))+strviaIV[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strefovencina[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0,padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada24horas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_1 = str(round(perro.peso*8,2))+strviaSC[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strmaropitan[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada24horas[idioma_actual], style='labelBlanco.TLabel') .grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_2 = str(round(perro.peso*1,2))+strviaSC[idioma_actual]
        ttk.Label(medicacion, text=cantidad_2, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strbuprenofina[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcad8horas_1[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_3 = str(round(perro.peso*0.02,2))+strviaSC[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strsuplementos[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada6horas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_4 = str(round(perro.peso*30,2))+strml[idioma_actual]
        ttk.Label(medicacion, text=cantidad_4, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strjarabe[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada6horas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_5 = str(round(perro.peso*1,2))+strmlVO[idioma_actual]
        ttk.Label(medicacion, text=cantidad_5, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        
        ttk.Label(medicacion, text=strtamiflu[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strcada24horasduraante10dias[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_6 = str(round(perro.peso*2,2))+strml[idioma_actual]
        ttk.Label(medicacion, text=cantidad_6, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        if self.es_muy_grave() and renal == 2 and hepatica == 2 and perro.edad < 1:
           ttk.Label(medicacion, text=strvalorareutanasia[idioma_actual], style='labelRojo.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
       

parvovirus =  Parvovirus()