from enum import Enum
import tkinter as tk
from tkinter import ttk
from enfermedades import  Enfermedad
from enfermedades import AceptarEnfermedad, RechazarEnfermedad, SiguientePrueba
from idiomas import leer_idioma_actual, strleishmania, strsangradonasal, strbebemuchaagua, strmuchopis
from idiomas import strblefaritis, strconjuntivitis, strperdidadepelo, strheridasalmhoadillas, strnoapetito
from idiomas import strdiarreas, strvomitos, stranemiasintomas, strictericia, strfiebre, stralmhodillasrugosas
from idiomas import strtrufainchada, strdermatitisconpus, strdescamacion, strvasculitis, struveitis
from idiomas import strGlomerulonefritis, strtestrapido, strtestElisa, strproteinograma, strcitologia, strdieta
from idiomas import stranemia, strbajaengrasas, strfluidoterapia, strmedicacion, stralopurinol, strdurante6_12_meses
from idiomas import strcantidad6, strcalcitriol, strcadadia, strantimoniat, strcada4_8_semanas, strviaIM
from idiomas import strmitelsofina, strdurante4semanas, strvalorareutanasia

class Leishmania(Enfermedad): 
   
    def inicializar_enfermedad(self):
         idioma_actual = leer_idioma_actual()
         self.name =strleishmania[idioma_actual]
         self.sintomas = [(strsangradonasal[idioma_actual], 50),
                (strbebemuchaagua[idioma_actual], 80),
                (strmuchopis[idioma_actual], 40),
                (strblefaritis[idioma_actual], 70),
                (strconjuntivitis[idioma_actual], 60),
                (strperdidadepelo[idioma_actual], 100),
                (strheridasalmhoadillas[idioma_actual], 90),
                (strnoapetito[idioma_actual], 10),
                (strdiarreas[idioma_actual], 10),
                (strvomitos[idioma_actual], 10),
                (stranemiasintomas[idioma_actual], 10), 
                (strictericia[idioma_actual], 10),
                (strfiebre[idioma_actual], 10),
                (stralmhodillasrugosas[idioma_actual], 90),
                (strtrufainchada[idioma_actual], 80),
                (strdermatitisconpus[idioma_actual], 90),
                (strdescamacion[idioma_actual], 100),
                (strvasculitis[idioma_actual], 20),
                (struveitis[idioma_actual], 80),
                (strGlomerulonefritis[idioma_actual], 60)]
         self.pruebas = [strtestrapido[idioma_actual], 
                         strtestElisa[idioma_actual], 
                         strproteinograma[idioma_actual], 
                         strcitologia[idioma_actual]]




    def calcular_diagnostico(self,  resultado, num_prueba):
        if num_prueba == 0:
            if resultado == False:  # test rapido negativo y pocos sintomas
                if self.puntos < 50:
                    return RechazarEnfermedad, 0           
            return SiguientePrueba, num_prueba   # -> ELISA
        elif num_prueba == 1: 
            if resultado == False:  # pocos anticuerpos
                if self.puntos < 50:    # pocos sintomas
                    return RechazarEnfermedad, 0
                return SiguientePrueba, num_prueba   # pocos anticuerpos, muchos sintomas -> PROTEINOGRAMA
            else:  # muchos anticuerpos
               return AceptarEnfermedad, 0
        elif num_prueba == 2:
            if resultado==True:
               return AceptarEnfermedad, 0  
            return SiguientePrueba, num_prueba   # -> CITOLOGIA
        else:
            if resultado == False:
                return RechazarEnfermedad, 0   
            else:
                return AceptarEnfermedad, 0  
             
    def es_grave(self):
        if self.puntos > 150:
            return True
        return False
    def es_muy_grave(self):
        if self.puntos > 400:
            return True
        return False

    def necesita_hospitalizacion(self, renal, hepatica, anemia):
        if hepatica != 0:
            return True
        return False
    
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

        ttk.Label(medicacion, text=stralopurinol[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strdurante6_12_meses[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad=str(round(perro.peso*10))+strcantidad6[idioma_actual]
        ttk.Label(medicacion, text=cantidad, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
       
        if renal != 0: # si tiene enfermedad renal
            ttk.Label(medicacion, text=strcalcitriol[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
            ttk.Label(medicacion, text=strcadadia[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
            cantidad_4=str(round(perro.peso*120,2))+strcantidad6[idioma_actual]
            ttk.Label(medicacion, text=cantidad_4, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
            fila = fila + 1

        # caso leve
        if self.es_grave()== False:  
            return
        
        # caso grave
        if hepatica == 0:    # animoniat de meglumina solo si no tiene enfermadad hepatica        
            ttk.Label(medicacion, text=strantimoniat[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
            ttk.Label(medicacion, text=strcada4_8_semanas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
            cantidad_2=str(round(perro.peso*0.33,2))+strviaIM[idioma_actual]
            ttk.Label(medicacion, text=cantidad_2, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
            fila = fila + 1
        
        ttk.Label(medicacion, text=strmitelsofina[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        ttk.Label(medicacion, text=strdurante4semanas[idioma_actual], style='labelBlanco.TLabel').grid(row=fila, column=1, padx=10, pady=5, sticky='nw')
        cantidad_3 = str(round(perro.peso*2))+strcantidad6[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3, style='labelBlanco.TLabel').grid(row=fila, column=2, padx=10, pady=5, sticky='nw')
        fila = fila + 1
        
        if self.es_muy_grave() == False:  
           return 
            
        # caso muy grave       
        if  renal == 2 and hepatica == 2 and perro.edad > 12:
           ttk.Label(medicacion, text=strvalorareutanasia[idioma_actual], style='labelRojo.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
       
# variable global
leishmania =  Leishmania()