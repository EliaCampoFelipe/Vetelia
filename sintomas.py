import tkinter as tk
from tkinter import ttk
from idiomas import leer_idioma_actual, strtos, strdisnea, strsangradonasal, stramigdalitis, strneumonia, strblefaritis
from idiomas import strlagrimeoconpus, strulcerascornia, strconjuntivitis, strmocosoculares, strulcerasconpus
from idiomas import strdiarreas, strdiarreasconsangre, strbebemuchaagua, strvomitos, strvomitosseveros, strnoapetito
from idiomas import strascitis, stranorexia, strmareos, strespasmos, strdesmayossinejercicio, strrigidez
from idiomas import stralmhodillasrugosas, strtrufainchada, strperdidadepelo, strheridasalmhoadillas
from idiomas import strclorrojoalrededordelaboca, strserascamucho, strdermatitisconpus, strerupcionesenlapiel
from idiomas import strdescamacion, strlatidosintensos, strruidostorax, stranemiasintomas, strmucosaspalidas
from idiomas import strpulsofemoraldisminuido, strpulsoyugular, strvasculitis, strmuchopis, strorinaconsangre
from idiomas import strictericia, strfiebre, strdeshidratacion, strsintomasrespiratorios, strsintomasoculares
from idiomas import struveitis, strsintomasdigestivos, strsintomasneurologicos, strsintomasdermicos
from idiomas import strsintomascierculatorio, strsintomasnefriticos, strsintomasotros

class sintoma:
    
    nombre=''
    valor: False
    def __init__(self, n, v):
        self.nombre = n
        self.valor = v

sintomas=[]
def inicializar_sintomas():
    idioma_actual = leer_idioma_actual()
    global sintomas
    sintomas = [sintoma(strtos[idioma_actual], False), 
        sintoma(strdisnea[idioma_actual],  False), 
        sintoma(strsangradonasal[idioma_actual],  False), 
        sintoma(stramigdalitis[idioma_actual], False), 
        sintoma(strneumonia[idioma_actual],  False), 
        
        sintoma( strblefaritis[idioma_actual], False), 
        sintoma( strlagrimeoconpus[idioma_actual], False),
        sintoma( strulcerascornia[idioma_actual], False), 
        sintoma( strconjuntivitis[idioma_actual], False),
        sintoma( strmocosoculares[idioma_actual], False), 
        sintoma( strulcerasconpus[idioma_actual], False), 

        sintoma( strdiarreas[idioma_actual], False), 
        sintoma( strdiarreasconsangre[idioma_actual], False),
        sintoma( strbebemuchaagua[idioma_actual], False),
        sintoma( strvomitos[idioma_actual], False),
        sintoma( strvomitosseveros[idioma_actual], False), 
        sintoma( strnoapetito[idioma_actual], False),
        sintoma( strascitis[idioma_actual], False),
        sintoma( stranorexia[idioma_actual], False), 
        sintoma( strmareos[idioma_actual], False),
        sintoma( strespasmos[idioma_actual], False), 
        sintoma( strdesmayossinejercicio[idioma_actual], False), 
        sintoma( strrigidez[idioma_actual], False),

        sintoma( stralmhodillasrugosas[idioma_actual], False), 
        sintoma( strtrufainchada[idioma_actual], False),
        sintoma( strperdidadepelo[idioma_actual], False),
        sintoma( strheridasalmhoadillas[idioma_actual], False), 
        sintoma( strclorrojoalrededordelaboca[idioma_actual], False), 
        sintoma( strserascamucho[idioma_actual], False), 
        sintoma( strdermatitisconpus[idioma_actual], False), 
        sintoma( strerupcionesenlapiel[idioma_actual], False), 
        sintoma( strdescamacion[idioma_actual], False), 

        sintoma( strlatidosintensos[idioma_actual], False),
        sintoma( strruidostorax[idioma_actual], False), 
        sintoma( stranemiasintomas[idioma_actual], False),  
        sintoma( strmucosaspalidas[idioma_actual], False), 
        sintoma( strpulsofemoraldisminuido[idioma_actual], False), 
        sintoma( strpulsoyugular[idioma_actual], False), 
        sintoma( strvasculitis[idioma_actual], False), 

        sintoma( strmuchopis[idioma_actual], False),  
        sintoma( strorinaconsangre[idioma_actual], False),  
        sintoma( strictericia[idioma_actual], False), 

        sintoma( strfiebre[idioma_actual], False),  
        sintoma( strdeshidratacion[idioma_actual], False)
    ]

def leer_sintomas():
    global sintomas
    return sintomas

def cambio_sintoma(nombre, valor):
    global sintomas
    for sintoma in sintomas:
        if sintoma.nombre == nombre:
            sintoma.valor= valor.get()
            break

def crear_ficha_sintomas(tab_sintomas):
    idioma_actual = leer_idioma_actual()
    tos_value = tk.BooleanVar()
    disnea_value = tk.BooleanVar()
    sangrado_value = tk.BooleanVar()
    amigdalitis_value = tk.BooleanVar()
    neumonia_value = tk.BooleanVar()

    blefaritis_value = tk.BooleanVar()
    lagrimeo_pus_value = tk.BooleanVar()
    ulceras_cornea_value = tk.BooleanVar()
    conjuntivitis_value = tk.BooleanVar()
    mocos_oculares_value = tk.BooleanVar()
    ulceras_con_pus_value = tk.BooleanVar()
    uveitis_value = tk.BooleanVar()
   
    diarreas_value = tk.BooleanVar()
    diarreas_con_sangre_value = tk.BooleanVar()
    bebe_mucha_agua_value = tk.BooleanVar()
    vomitos_value = tk.BooleanVar()
    vomitos_severos_value = tk.BooleanVar()
    no_apetito_value = tk.BooleanVar()
    ascitis_value = tk.BooleanVar()
    anorexia_value = tk.BooleanVar()
        
    mareos_value = tk.BooleanVar()
    desmayos_sin_ejercicio_value =  tk.BooleanVar()
    rigidez_parálisis_value =  tk.BooleanVar()
    espasmos_value = tk.BooleanVar()

    almohadillas_rugosas_value = tk.BooleanVar()
    trufa_hinchada_value =  tk.BooleanVar()
    pérdida_de_pelo_alrededor_de_nariz_orejas_y_ojos_value = tk.BooleanVar()
    heridas_en_las_almohadillas_value =  tk.BooleanVar()
    color_rojo_alrededor_de_la_boca_value = tk.BooleanVar()
    se_rasca_mucho_value = tk.BooleanVar()
    dermatitis_con_pus_value =  tk.BooleanVar()
    erupciones_en_la_piel_value = tk.BooleanVar()
    decamacion_value = tk.BooleanVar()

    latidos_del_corazon_intenso_value =  tk.BooleanVar()
    ruidos_en_el_torax_value =  tk.BooleanVar()
    anemia_value = tk.BooleanVar()
    mucosas_palidas_value = tk.BooleanVar()
    pulso_femoral_diminuido_value = tk.BooleanVar()
    pulso_yugular_value = tk.BooleanVar()
    vasculitis_value = tk.BooleanVar()

    mucho_pis_value = tk.BooleanVar()
    orina_con_sangre_value =  tk.BooleanVar()
    ictericia_value = tk.BooleanVar()
    #glomerulonefritis_value = tk.BooleanVar()
    fiebre_value = tk.BooleanVar()
    deshidratacion_value = tk.BooleanVar()

    sintomas_frame  =  ttk.Frame(tab_sintomas, width=600, height=600)  
    sintomas_frame.grid(row=0, column=0, padx=45, pady=5, sticky='nw')

    W= 100
    sintomas_respiratorios  =  ttk.Frame(sintomas_frame, width=W, height=600)
    sintomas_respiratorios.grid(row=0, column=0, padx=10, pady=5, sticky='nw')
    sintomas_respiratorios.rowconfigure(6, minsize=10)
    sintomas_respiratorios.columnconfigure(2, minsize=10)
    #sintomas_respiratorios.grid_rowconfigure(5)
    ttk.Label(sintomas_respiratorios, text=strsintomasrespiratorios[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='n', columnspan=2)
    tos_checkbox = ttk.Checkbutton(sintomas_respiratorios, text=strtos[idioma_actual], variable=tos_value, command= lambda: cambio_sintoma(strtos[idioma_actual], tos_value))
    tos_checkbox.grid(row=1,  column=0,  padx=5,  pady=5, sticky='nw')
    disnea_checkbox = ttk.Checkbutton(sintomas_respiratorios, text=strdisnea[idioma_actual], variable=disnea_value, command=lambda: cambio_sintoma(strdisnea[idioma_actual], disnea_value))
    disnea_checkbox.grid(row=2,  column=0,  padx=5,  pady=5, sticky='nw')
    sangrado_checkbox = ttk.Checkbutton(sintomas_respiratorios, text=strsangradonasal[idioma_actual], variable=sangrado_value, command= lambda: cambio_sintoma(strsangradonasal[idioma_actual], sangrado_value))
    sangrado_checkbox.grid(row=3,  column=0,  padx=5,  pady=5, sticky='nw')
    # hipertension_pulmonar_value =  tk.BooleanVar()
    # hipertension_pulmonar_checkbox = ttk.Checkbutton(sintomas_respiratorios, text="Hipertensión pulmonar", variable=hipertension_pulmonar_value)
    # hipertension_pulmonar_checkbox.grid(row=4, column=0, padx=5, pady=5, sticky='nw')
    amigdalitis_checkbox = ttk.Checkbutton(sintomas_respiratorios, text=stramigdalitis[idioma_actual], variable=amigdalitis_value, command=lambda: cambio_sintoma(stramigdalitis[idioma_actual], amigdalitis_value))
    amigdalitis_checkbox.grid(row=4,  column=0,  padx=5,  pady=5, sticky='nw')
    neumonia_checkbox = ttk.Checkbutton(sintomas_respiratorios, text=strneumonia[idioma_actual],variable=neumonia_value, command=lambda: cambio_sintoma(strneumonia[idioma_actual], neumonia_value))
    neumonia_checkbox.grid(row=5,  column=0,  padx=5,  pady=5, sticky='nw')

    sintomas_oculares  =  ttk.Frame(sintomas_frame,  width=W,  height=600)
    sintomas_oculares.grid(row=0,  column=1,  padx=10,  pady=5, sticky='nw')
    sintomas_oculares.columnconfigure(2, minsize=70)
    ttk.Label(sintomas_oculares,  text=strsintomasoculares[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='n', columnspan=2)
    blefaritis_checkbox = ttk.Checkbutton(sintomas_oculares, text=strblefaritis[idioma_actual], variable=blefaritis_value, command=lambda: cambio_sintoma(strblefaritis[idioma_actual], blefaritis_value))
    blefaritis_checkbox.grid(row=1,  column=0,  padx=5,  pady=5, sticky='nw')
    lagrimeo_pus_checkbox = ttk.Checkbutton(sintomas_oculares, text=strlagrimeoconpus[idioma_actual], variable=lagrimeo_pus_value, command=lambda: cambio_sintoma(strlagrimeoconpus[idioma_actual], lagrimeo_pus_value))
    lagrimeo_pus_checkbox.grid(row=2,  column=0,  padx=5,  pady=5, sticky='nw')
    ulceras_cornea_checkbox = ttk.Checkbutton(sintomas_oculares, text=strulcerascornia[idioma_actual], variable=ulceras_cornea_value, command=lambda: cambio_sintoma(strulcerascornia[idioma_actual], ulceras_cornea_value))
    ulceras_cornea_checkbox.grid(row=3,  column=0,  padx=5,  pady=5, sticky='nw')
    conjuntivitis_checkbox = ttk.Checkbutton(sintomas_oculares, text=strconjuntivitis[idioma_actual], variable=conjuntivitis_value, command=lambda: cambio_sintoma(strconjuntivitis[idioma_actual], conjuntivitis_value))
    conjuntivitis_checkbox.grid(row=4,  column=0,  padx=5,  pady=5, sticky='nw')
    mocos_oculares_checkbox = ttk.Checkbutton(sintomas_oculares, text=strmocosoculares[idioma_actual], variable=mocos_oculares_value, command=lambda: cambio_sintoma(strmocosoculares[idioma_actual], mocos_oculares_value))
    mocos_oculares_checkbox.grid(row=5,  column=0,  padx=5,  pady=5, sticky='nw')
    ulceras_con_pus_checkbox = ttk.Checkbutton(sintomas_oculares, text=strulcerasconpus[idioma_actual], variable=ulceras_con_pus_value, command=lambda: cambio_sintoma(strulcerasconpus[idioma_actual], ulceras_con_pus_value))
    ulceras_con_pus_checkbox.grid(row=6, column=0, padx=5, pady=5, sticky='nw')
    uveitis_checkbox = ttk.Checkbutton(sintomas_oculares, text=struveitis[idioma_actual], variable=uveitis_value, command=lambda: cambio_sintoma(struveitis[idioma_actual], uveitis_value) )
    uveitis_checkbox.grid(row=7, column=0, padx=5, pady=5, sticky='nw')
   
    sintomas_digestivos =  ttk.Frame(sintomas_frame,  width=W,  height=600)
    sintomas_digestivos.grid(row=0,  column=2,  padx=10,  pady=5, sticky='nw')
    ttk.Label(sintomas_digestivos,  text=strsintomasdigestivos[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw', columnspan=2)
    diarreas_checkbox = ttk.Checkbutton(sintomas_digestivos, text=strdiarreas[idioma_actual], variable=diarreas_value, command=lambda: cambio_sintoma(strdiarreas[idioma_actual], diarreas_value))
    diarreas_checkbox.grid(row=1,  column=0,  padx=5,  pady=5, sticky='nw')
    diarreas_con_sangre_checkbox = ttk.Checkbutton(sintomas_digestivos, text=strdiarreasconsangre[idioma_actual], variable=diarreas_con_sangre_value, command=lambda: cambio_sintoma(strdiarreasconsangre[idioma_actual], diarreas_con_sangre_value))
    diarreas_con_sangre_checkbox.grid(row=1,  column=1,  padx=5,  pady=5, sticky='nw')
    vomitos_checkbox = ttk.Checkbutton(sintomas_digestivos, text=strvomitos[idioma_actual], variable=vomitos_value, command=lambda: cambio_sintoma(strvomitos[idioma_actual], vomitos_value))
    vomitos_checkbox.grid(row=3,  column=0,  padx=5,  pady=5, sticky='nw')
    vomitos_severos_checkbox = ttk.Checkbutton(sintomas_digestivos, text=strvomitosseveros[idioma_actual], variable=vomitos_severos_value, command=lambda: cambio_sintoma(strvomitosseveros[idioma_actual], vomitos_severos_value))
    vomitos_severos_checkbox.grid(row=3,  column=1,  padx=5,  pady=5, sticky='nw')
    no_apetito_checkbox = ttk.Checkbutton(sintomas_digestivos, text=strnoapetito[idioma_actual], variable=no_apetito_value, command=lambda: cambio_sintoma(strnoapetito[idioma_actual], no_apetito_value))
    no_apetito_checkbox.grid(row=4,  column=0,  padx=5,  pady=5, sticky='nw')
    ascitis_checkbox = ttk.Checkbutton(sintomas_digestivos, text=strascitis[idioma_actual], variable=ascitis_value, command=lambda: cambio_sintoma(strascitis[idioma_actual], ascitis_value))
    ascitis_checkbox.grid(row=6,  column=0,  padx=5,  pady=5, sticky='nw')
    anorexia_checkbox = ttk.Checkbutton(sintomas_digestivos, text=stranorexia[idioma_actual], variable=anorexia_value, command=lambda: cambio_sintoma(stranorexia[idioma_actual], anorexia_value))
    anorexia_checkbox.grid(row=7, column=0, padx=5, pady=5, sticky='nw')
    
    sintomas_neurologicos  =  ttk.Frame(sintomas_frame,  width=W, height=600)
    sintomas_neurologicos.grid(row=0,  column=3,  padx=10,  pady=5, sticky='nw')
    ttk.Label(sintomas_neurologicos,  text=strsintomasneurologicos[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw', columnspan=2)
    mareos_checkbox = ttk.Checkbutton(sintomas_neurologicos, text=strmareos[idioma_actual], variable=mareos_value, command=lambda: cambio_sintoma(strmareos[idioma_actual], mareos_value))
    mareos_checkbox.grid(row=1,  column=0,  padx=5,  pady=5, sticky='nw')
    espasmos_checkbox = ttk.Checkbutton(sintomas_neurologicos, text=strespasmos[idioma_actual], variable=espasmos_value, command=lambda: cambio_sintoma(strespasmos[idioma_actual], espasmos_value))
    espasmos_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky='nw')
    desmayos_sin_ejercicio_checkbox = ttk.Checkbutton(sintomas_neurologicos, text=strdesmayossinejercicio[idioma_actual], variable=desmayos_sin_ejercicio_value, command=lambda: cambio_sintoma(strdesmayossinejercicio[idioma_actual], desmayos_sin_ejercicio_value))
    desmayos_sin_ejercicio_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky='nw')
    rigidez_parálisis_checkbox = ttk.Checkbutton(sintomas_neurologicos, text=strrigidez[idioma_actual], variable=rigidez_parálisis_value, command=lambda: cambio_sintoma(strrigidez[idioma_actual], rigidez_parálisis_value))
    rigidez_parálisis_checkbox.grid(row=3, column=0, padx=5, pady=5, sticky='nw')

    sintomas_dérmicos  =  ttk.Frame(sintomas_frame,  width=W,  height=600)
    sintomas_dérmicos.grid(row=1,  column=0,  padx=10,  pady=5,  sticky='nw')
    ttk.Label(sintomas_dérmicos,  text=strsintomasdermicos[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw', columnspan=2)
    alomohadillas_rugosas_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=stralmhodillasrugosas[idioma_actual], variable=almohadillas_rugosas_value, 
                                                     command=lambda: cambio_sintoma(stralmhodillasrugosas[idioma_actual], almohadillas_rugosas_value))
    alomohadillas_rugosas_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky='nw')
    trufa_hinchada_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strtrufainchada[idioma_actual], variable=trufa_hinchada_value, 
                                              command=lambda: cambio_sintoma(strtrufainchada[idioma_actual], trufa_hinchada_value))
    trufa_hinchada_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky='nw')
    pérdida_de_pelo_alrededor_de_nariz_orejas_y_ojos_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strperdidadepelo[idioma_actual], 
                                                                                variable=pérdida_de_pelo_alrededor_de_nariz_orejas_y_ojos_value,
                                                                                command=lambda: cambio_sintoma(strperdidadepelo[idioma_actual], pérdida_de_pelo_alrededor_de_nariz_orejas_y_ojos_value) )
    pérdida_de_pelo_alrededor_de_nariz_orejas_y_ojos_checkbox.grid(row=3, column=0, padx=5, pady=5, sticky='nw')
    heridas_en_las_almohadillas_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strheridasalmhoadillas[idioma_actual], variable=heridas_en_las_almohadillas_value,
                                                           command=lambda: cambio_sintoma(strheridasalmhoadillas[idioma_actual], heridas_en_las_almohadillas_value))
    heridas_en_las_almohadillas_checkbox.grid(row=4, column=0, padx=5, pady=5, sticky='nw')
    color_rojo_alrededor_de_la_boca_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strclorrojoalrededordelaboca[idioma_actual], 
                                                               variable= color_rojo_alrededor_de_la_boca_value, 
                                                               command=lambda: cambio_sintoma(strclorrojoalrededordelaboca[idioma_actual], color_rojo_alrededor_de_la_boca_value))
    color_rojo_alrededor_de_la_boca_checkbox.grid(row=5, column=0, padx=5, pady=5, sticky='nw')
    se_rasca_mucho_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strserascamucho[idioma_actual], 
                                              variable= se_rasca_mucho_value, command=lambda: cambio_sintoma(strserascamucho[idioma_actual], se_rasca_mucho_value))
    se_rasca_mucho_checkbox.grid(row=6, column=0, padx=5, pady=5, sticky='nw')
    dermatitis_con_pus_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strdermatitisconpus[idioma_actual], 
                                                  variable=dermatitis_con_pus_value, command=lambda: cambio_sintoma(strdermatitisconpus[idioma_actual], dermatitis_con_pus_value))
    dermatitis_con_pus_checkbox.grid(row=7, column=0, padx=5, pady=5, sticky='nw')
    erupciones_en_la_piel_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strerupcionesenlapiel[idioma_actual], 
                                                     variable=erupciones_en_la_piel_value, command=lambda: cambio_sintoma(strerupcionesenlapiel[idioma_actual], erupciones_en_la_piel_value))
    erupciones_en_la_piel_checkbox.grid(row=8, column=0, padx=5, pady=5, sticky='nw')
    descamacion_checkbox = ttk.Checkbutton(sintomas_dérmicos, text=strdescamacion[idioma_actual],
                                            variable=decamacion_value, command=lambda: cambio_sintoma(strdescamacion[idioma_actual], decamacion_value))
    descamacion_checkbox.grid(row=9, column=0, padx=5, pady=5, sticky='nw')

    sintomas_circulatorios  =  ttk.Frame(sintomas_frame,  width=W,  height=600)
    sintomas_circulatorios.grid(row=1, column=1, padx=10, pady=5, sticky='nw')
    sintomas_circulatorios.columnconfigure(2, minsize=50)
    ttk.Label(sintomas_circulatorios, text=strsintomascierculatorio[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw', columnspan=2)
    latidos_del_corazon_intenso_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=strlatidosintensos[idioma_actual], 
                                                           variable=latidos_del_corazon_intenso_value, command=lambda: cambio_sintoma(strlatidosintensos[idioma_actual], latidos_del_corazon_intenso_value))
    latidos_del_corazon_intenso_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky='nw')
    ruidos_en_el_torax_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=strruidostorax[idioma_actual], 
                                                  variable= ruidos_en_el_torax_value, command=lambda: cambio_sintoma(strruidostorax[idioma_actual], ruidos_en_el_torax_value))
    ruidos_en_el_torax_checkbox.grid(row=2,column=0, padx=5, pady=5, sticky='nw')
    anemia_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=stranemiasintomas[idioma_actual], variable= anemia_value, command=lambda: cambio_sintoma(stranemiasintomas[idioma_actual], anemia_value))
    anemia_checkbox.grid(row=3,  column=0,  padx=5,  pady=5, sticky='nw')
    mucosas_palidas_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=strmucosaspalidas[idioma_actual], 
                                               variable=mucosas_palidas_value, command=lambda: cambio_sintoma(strmucosaspalidas[idioma_actual], mucosas_palidas_value))
    mucosas_palidas_checkbox.grid(row=4, column=0, padx=5, pady=5, sticky='nw')
    pulso_femoral_diminuido_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=strpulsofemoraldisminuido[idioma_actual], 
                                                       variable=pulso_femoral_diminuido_value, command=lambda: cambio_sintoma(strpulsofemoraldisminuido[idioma_actual], pulso_femoral_diminuido_value))
    pulso_femoral_diminuido_checkbox.grid(row=5, column=0, padx=5, pady=5,sticky='nw')
    pulso_yugular_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=strpulsoyugular[idioma_actual], 
                                             variable= pulso_yugular_value, command=lambda: cambio_sintoma(strpulsoyugular[idioma_actual], pulso_yugular_value))
    pulso_yugular_checkbox.grid(row=6, column=0, padx=5, pady=5, sticky='nw')
    vasculitis_checkbox = ttk.Checkbutton(sintomas_circulatorios, text=strvasculitis[idioma_actual], variable=vasculitis_value, command=lambda: cambio_sintoma(strvasculitis[idioma_actual], vasculitis_value))
    vasculitis_checkbox.grid(row=7, column=0, padx=5, pady=5, sticky='nw')
                                          
    sintomas_rinon  =  ttk.Frame(sintomas_frame,  width=W,  height=600)
    sintomas_rinon.grid(row=1,  column=2,  padx=10,  pady=5, sticky='nw')
    sintomas_rinon.columnconfigure(2, minsize=30)
    ttk.Label(sintomas_rinon,  text=strsintomasnefriticos[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw', columnspan=2)
    mucho_pis_checkbox = ttk.Checkbutton(sintomas_rinon, text=strmuchopis[idioma_actual], variable=mucho_pis_value, command=lambda: cambio_sintoma(strmuchopis[idioma_actual], mucho_pis_value))
    mucho_pis_checkbox.grid(row=5,  column=0,  padx=5,  pady=5, sticky='nw')
    orina_con_sangre_checkbox = ttk.Checkbutton(sintomas_rinon, text=strorinaconsangre[idioma_actual], 
                                                variable=orina_con_sangre_value, command=lambda: cambio_sintoma(strorinaconsangre[idioma_actual], orina_con_sangre_value))
    orina_con_sangre_checkbox.grid(row=6,  column=0,  padx=5,  pady=5, sticky='nw')
    ictericia_checkbox = ttk.Checkbutton(sintomas_rinon, text=strictericia[idioma_actual], variable=ictericia_value, command=lambda: cambio_sintoma(strictericia[idioma_actual], ictericia_value))
    ictericia_checkbox.grid(row=7,  column=0,  padx=5,  pady=5, sticky='nw')
    bebe_mucha_agua_checkbox = ttk.Checkbutton(sintomas_rinon, text=strbebemuchaagua[idioma_actual], variable=bebe_mucha_agua_value, command=lambda: cambio_sintoma(strbebemuchaagua[idioma_actual], bebe_mucha_agua_value))
    bebe_mucha_agua_checkbox.grid(row=8,  column=0,  padx=5,  pady=5, sticky='nw')
    #glomerulonefritis_checkbox = ttk.Checkbutton(sintomas_rinon, text="Glomerulonefritis", variable=glomerulonefritis_value, command=lambda: cambio('Glomerulonefritis', glomerulonefritis_value))
    #glomerulonefritis_checkbox.grid(row=8, column=0, padx=5, pady=5, sticky='nw')
    sintomas_otros =  ttk.Frame(sintomas_frame,  width=W,  height=600)
    sintomas_otros.grid(row=1, column=3, padx=5, pady=5, sticky='nw')
    sintomas_otros.columnconfigure(2, minsize=30)
    ttk.Label(sintomas_otros,  text=strsintomasotros[idioma_actual],style='titulo.TLabel').grid(row=0,  column=0,  padx=5,  pady=5, sticky='nw', columnspan=2)
    fiebre_checkbox =  ttk.Checkbutton(sintomas_otros, text=strfiebre[idioma_actual], variable=fiebre_value, command=lambda: cambio_sintoma(strfiebre[idioma_actual], fiebre_value))
    fiebre_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky='nw')
    deshidratacion_checkbox = ttk.Checkbutton(sintomas_otros, text=strdeshidratacion[idioma_actual], variable=deshidratacion_value, command=lambda: cambio_sintoma(strdeshidratacion[idioma_actual], deshidratacion_value))
    deshidratacion_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky='nw')
    