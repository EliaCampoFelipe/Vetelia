from enum import Enum
import tkinter as tk
from tkinter import ttk
from enfermedades import  Enfermedad
from enfermedades import AceptarEnfermedad, RechazarEnfermedad, SiguientePrueba
from idiomas import leer_idioma_actual, strfilaria, strtos, strbebemuchaagua, strmuchopis, strascitis, strmareos
from idiomas import strdesmayossinejercicio, strserascamucho, strruidostorax, strheridasalmhoadillas, strdisnea
from idiomas import strnoapetito, strsangradonasal, strictericia, strorinaconsangre, strfiebre, strmucosaspalidas
from idiomas import strpulsofemoraldisminuido, strlatidosintensos, strpulsoyugular,  strdieta, stranemia
from idiomas import strbajaengrasas, strfluidoterapia, strmedicacion, strdia0, strprednisona, str1semana
from idiomas import strcantidad1, str2semana, strcantidad1_2, str3i4semana, strcantidad1_3, strdia1
from idiomas import strdoxicilina, strdurante4semanas, strcantidad4, strmelarsominadiclorhidrat, strcantidad3_1
from idiomas import strantihistamínicosyglucocorticoides, strVigilardurante8horas, strcantidad2, strDia1al28
from idiomas import strcantidad3, strdia30, strdia60, str1inyeccion, strcantidad5, strdia90, strsegundainyeccion
from idiomas import strdia91, strtercerainyeccion, strdia120, strdurante30dias, strtestElisaanalisisdesangre
from idiomas import strradiografiadetorax, strelectroyeco

class Filaria(Enfermedad):
    def inicializar_enfermedad(self): 
        idioma_actual = leer_idioma_actual()
        self.name =strfilaria[idioma_actual]
        self.sintomas = [(strtos[idioma_actual], 50),
                (strbebemuchaagua[idioma_actual], 70),
                (strmuchopis[idioma_actual], 60),
                (strascitis[idioma_actual], 60),
                (strmareos[idioma_actual], 90),
                (strdesmayossinejercicio[idioma_actual], 100),
                (strserascamucho[idioma_actual], 80),
                (strruidostorax[idioma_actual], 95), 
                (strheridasalmhoadillas[idioma_actual], 10),
                (strdisnea[idioma_actual], 10),
                (strnoapetito[idioma_actual],10 ),
                (strsangradonasal[idioma_actual], 30),
                (strictericia[idioma_actual], 20),
                (strorinaconsangre[idioma_actual], 40),
                (strfiebre[idioma_actual], 10),
                (strmucosaspalidas[idioma_actual], 50),
                (strpulsofemoraldisminuido[idioma_actual], 80),
                (strlatidosintensos[idioma_actual], 80),
                (strpulsoyugular[idioma_actual], 80)]
        self.pruebas = [strtestElisaanalisisdesangre[idioma_actual], 
                        strradiografiadetorax[idioma_actual],
                        strelectroyeco[idioma_actual]]

    def calcular_diagnostico(self, resultado, num_prueba):
        if num_prueba == 0:
            if resultado == False:
                if self.puntos < 60:
                    return RechazarEnfermedad,0
            return SiguientePrueba,num_prueba
        elif num_prueba == 1:
            if resultado == False:
                return SiguientePrueba,num_prueba
            return AceptarEnfermedad,0
        elif num_prueba == 2:
            if resultado == False:
                return RechazarEnfermedad,0
            return AceptarEnfermedad,0

    def es_grave(self):
        if self.puntos > 150:
            return True
        return False
    def es_muy_grave(self):
        if self.puntos > 400:
            return True
        return False
    
    def necesita_hospitalizacion(self, renal, hepatica, anemia):
        if hepatica != 0 or self.necesita_cirugia()== True:
            return True
        return False
    def necesita_cirugia(self):
        if self.muchos == True:
            return True
        return False
    
    def rellenar_medicacion(self, perro, ventana, renal, hepatica, anemia):
        idioma_actual = leer_idioma_actual()
        fila = 0
        if anemia == True or hepatica != 0:
            dieta = ttk.Frame(ventana, width=200, height=100, style='FrameBlanco.TFrame')
            dieta.grid(row=0, column=0, padx=0, pady=10, sticky='nw')
            dieta.rowconfigure(10, minsize=700)
            ttk.Label(dieta, text=strdieta[idioma_actual], style='tituloazul.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
            fila = fila + 1

        if anemia == True:
            ttk.Label(dieta, text=stranemia[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=0, padx=3, pady=5, sticky='nw')
            fila = fila + 1
        if hepatica != 0: 
            ttk.Label(dieta, text=strbajaengrasas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=0, padx=3, pady=5, sticky='nw')
            fila = fila + 1
            ttk.Label(dieta, text=strfluidoterapia[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=0, padx=3, pady=5, sticky='nw')
            fila = fila + 1

        fila = 0
        medicacion = ttk.Frame(ventana,  width=200, height=200, style='FrameBlanco.TFrame')
        medicacion.grid(row=0, column=1, padx=3, pady=10, sticky='nw')
        ttk.Label(medicacion, text=strmedicacion[idioma_actual], style='tituloazul.TLabel').grid(row=fila, column=0, padx=10, pady=5, sticky='nw')
        medicacion.columnconfigure(10, minsize=750)
        fila = fila + 1

        dia_0 =ttk.Label(medicacion, text=strdia0[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_0.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strprednisona[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1,padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=str1semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1 = str(round(perro.peso*0.5,2))+strcantidad1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=str2semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1_2 = str(round(perro.peso*0.5,2))+strcantidad1_2[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1_2, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila= fila + 1

        ttk.Label(medicacion, text=str3i4semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1_3 = str(round(perro.peso*0.5,2))+strcantidad1_3[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1_3, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')        
        fila = fila + 1
        
        dia_1 = ttk.Label(medicacion, text= strdia1[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_1.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdurante4semanas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_4 = str(round(perro.peso*10,2))+strcantidad4[idioma_actual]
        ttk.Label(medicacion, text=cantidad_4, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1
        
        ttk.Label(medicacion, text=strmelarsominadiclorhidrat[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_3_1 = str(round(perro.peso*2.14,2))+strcantidad3_1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strantihistamínicosyglucocorticoides[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strVigilardurante8horas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_2 = str(round(perro.peso*10,2))+strcantidad2[idioma_actual]
        ttk.Label(medicacion, text=cantidad_2, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=6, sticky='nw')
        fila = fila + 1

        dia_1_al_28 = ttk.Label(medicacion, text=strDia1al28[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_1_al_28.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdurante4semanas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_3 = str(round(perro.peso*10,2))+strcantidad3[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=6, sticky='nw')
        fila = fila + 1

        dia_30 = ttk.Label(medicacion, text=strdia30[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_30.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdurante4semanas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_4 = str(round(perro.peso*10,2))+strcantidad4[idioma_actual]
        ttk.Label(medicacion, text=cantidad_4, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strmelarsominadiclorhidrat[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_3_1 = str(round(perro.peso*2.14,2))+strcantidad3_1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=6, sticky='nw')   
        fila = fila + 1

        dia_60 = ttk.Label(medicacion, text=strdia60[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_60.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdurante4semanas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_4 = str(round(perro.peso*10,2))+strcantidad4[idioma_actual]
        ttk.Label(medicacion, text=cantidad_4, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strmelarsominadiclorhidrat[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_3_1 = str(round(perro.peso*2.14,2))+strcantidad3_1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=str1inyeccion[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_5 = str(round(perro.peso*2.5,2))+strcantidad5[idioma_actual]
        ttk.Label(medicacion, text=cantidad_5, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila +1

        ttk.Label(medicacion, text=strprednisona[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1,padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=str1semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1 = str(round(perro.peso*0.5,2))+strcantidad1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=str2semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1_2 = str(round(perro.peso*0.5,2))+strcantidad1_2[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1_2, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=str3i4semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1_3 = str(round(perro.peso*0.5,2))+strcantidad1_3[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1_3, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=6, sticky='nw')
        fila = fila + 1

        dia_90 = ttk.Label(medicacion, text=strdia90[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_90.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdurante4semanas[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_4 = str(round(perro.peso*10,2))+strcantidad4[idioma_actual]
        ttk.Label(medicacion, text=cantidad_4, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strmelarsominadiclorhidrat[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_3_1 = str(round(perro.peso*2.14,2))+strcantidad3_1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_3_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=strsegundainyeccion[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_6 =  str(round(perro.peso*2.5,2))+strcantidad5[idioma_actual]
        ttk.Label(medicacion, text=cantidad_6, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=6, sticky='nw')
        fila = fila + 1
        
        dia_91 = ttk.Label(medicacion, text=strdia91[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_91.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strtercerainyeccion[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        cantidad_7 = str(round(perro.peso*2.5,2))+strcantidad5[idioma_actual]
        ttk.Label(medicacion, text=cantidad_7, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1
        
        ttk.Label(medicacion, text=strprednisona[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1,padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=str1semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1 = str(round(perro.peso*0.5,2))+strcantidad1[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=str2semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1_2 = str(round(perro.peso*0.5,2))+strcantidad1_2[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1_2, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')
        fila = fila + 1

        ttk.Label(medicacion, text=str3i4semana[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_1_3 = str(round(perro.peso*0.5,2))+strcantidad1_3[idioma_actual]
        ttk.Label(medicacion, text=cantidad_1_3, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=6, sticky='nw')
        fila = fila + 1

        dia_120 = ttk.Label(medicacion, text=strdia120[idioma_actual], style='tituloazulPequeño.TLabel')
        dia_120.grid(row=fila, column=0, padx=10, pady=1, sticky='nw')  
        ttk.Label(medicacion, text=strdoxicilina[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=1, padx=10, pady=1, sticky='nw')
        ttk.Label(medicacion, text=strdurante30dias[idioma_actual], style='labelBlancoPequeño.TLabel').grid(row=fila, column=2, padx=10, pady=1, sticky='nw')
        cantidad_8 = str(round(perro.peso*10,2))+strcantidad4[idioma_actual]
        ttk.Label(medicacion, text=cantidad_8, style='labelBlancoPequeño.TLabel').grid(row=fila, column=3, padx=10, pady=1, sticky='nw')

filaria = Filaria()