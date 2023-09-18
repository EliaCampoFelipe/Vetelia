CASTELLANO = 0
CATALAN = 1

idioma_actual = CATALAN

def cambiar_idioma(idioma):
    global idioma_actual
    idioma_actual = idioma

def leer_idioma_actual():
    global idioma_actual
    return idioma_actual

strLeve = ['(Leve)', '(Lleu)']
strGrave = ['(Grave)', '(Greu)']
strMuyGrave = ['(Muy Grave)', '(Molt greu)']
strmoquillo = ['Moquillo', 'Brom']
strparvovirus = ['Parvovirus', 'Parvovirus']
strcastellano = ['castellano', 'castellà']
strcatalan = ['catalan', 'Català']

#tabs
strdatos = [' Datos ', ' Dades ']
strsintomas = [' Síntomas ', 'Símptomes ']
strpruebas = [' Pruebas ', 'Proves ']
strtratamiento = [' Tratamiento ', 'Tractament ']
strayudaaldiagnostico = ['Ayuda al diagnóstico', 'Ajuda al diagnòstic']


#ficha de datos
strPerroNoEncontrado= ['Error: Perro no encontrado', 'Error: Gos no trobat']
strPerroNoEncontradoPorDni = ['Error: Perro no encontrado. Búsqueda por nombre del perro y DNI del propietario', 'Error: Gos no trobat. Cerca per nom del gos i DNI del propietari']
strRellenarDatos = ['Error: Debe rellenar todos los campos', 'Error: Ompliu tots els camps']
strDatosObligatorios= ['Error: Todos los campos son obligatorios', 'Error: Tots els camps són obligatoris']
strDNIincorrecto = ['Error: DNI incorrecto', 'Error: DNI incorrecte']
strintroduzcaDNI = ['Introduzca un DNI correcto', 'Introdueixi un DNI correcte']
strtelefonoincorrecto = ['Error: Teléfono incorrecto', 'Error: Telèfon incorrecte']
strintroduzcanumerodetelefono = ['Introduzca un número de teléfono correcto', 'Introdueixi un número de telèfon correcte']
strintroduzcaDNIinombredelperro = ['Error: Búsqueda por DNI del propietario y nombre de perro', 'Error: Cerca per DNI del propietari i nom del gos']
strrellenarDNIielnombredelperro = ['Error: Debe rellenar los campos de DNI y nombre del perro', 'Error: Ompliu els camps de DNI i nom del gos']
strenfermedaderronia = ['Error: Enfermedad no encontrada', 'Error: Malaltia no trobada']
strenfermedaderronia2 = ['Error: No es ninguna enfermedad de las estudiadas. Revise los síntomas', 'Error: No es cap malaltia de les estudiades. Revisis els símptomes']

strlaborables = ['Laborables: 647 54 28 44 (10h-20h)', 'Laborals: 647 54 28 44 (10h-20h)']
strurgencias = ['Urgencias: 647 54 28 44', 'Urgencies: 647 54 28 44']
strdatosdelpaciente = ['                DATOS DEL PACIENTE                        ', '                DADES DEL PACIENT                        ']
strnombre = ['Nombre', 'Nom']
strgenero = ['Género', 'Gènere']
strmacho = ['Macho', 'Mascle']
strhembra = ['Hembra', 'Femella']
stredad = ['Edad', 'Edat']
strpeso = ['Peso', 'Pes']
strvacunado = ['Vacunado', 'Vacunat']
strleishmania = ['Leishmania', 'Leishmània']
strfilaria = ['Filaria','Filària']
strdatosdecontacto = ['               DATOS DE CONTACTO                        ', '               DADES DE CONTACTE                        ']
strnombredelpropietario = ['Nombre propietario', 'Nom del propietari']
strtelefono = ['Teléfono', 'Telèfon']
strDNI = ['DNI', 'DNI']
strbuscar = ['Buscar', 'Buscar']
strguardar = ['Guardar', 'Guardar']

#sintomas
strsintomasrespiratorios =[ ' Respiratorios     ',' Respiratoris    '] 
strsintomasoculares = [' Oculares        ', ' Oculars     ']
strsintomasdigestivos = [' Digestivos      ', ' Digestius    ']
strsintomasneurologicos = [' Neurológicos ', ' Neurològics    ']
strsintomasdermicos = [' Dérmicos            ', ' Dèrmics    ']
strsintomascierculatorio = [' Circulatorios  ', ' Circulatoris   ']
strsintomasnefriticos = [' Nefríticos         ', ' Nefrítics   ']
strsintomasotros = [' Otros        ', ' Altres   ']
strtos = ['Tos', 'Tos']
strbebemuchaagua = ['Bebe mucha agua', 'Beu molta aigua']
strmuchopis = ['Mucho pis', 'Molt pis']
strascitis = ['Ascitis', 'Ascitis']
strmareos = ['Mareos', 'Marejos']
strdesmayossinejercicio = ['Desmayos sin ejercicio', 'Desmais sense exercici']
strserascamucho = ['Se rasca mucho', 'Es rasca molt']
strruidostorax = ['Ruidos tórax', 'Sorolls tòrax']
strheridasalmhoadillas = ['Heridas almohadillas', 'Ferides als coixinets']
strdisnea = ['Disnea', 'Dispnea']
strnoapetito = ['No apetito', 'No apetit']
strsangradonasal = ['Sangrado Nasal', 'Sangrat Nasal']
strictericia = ['Ictericia', 'Icterícia']
strorinaconsangre = ['Orina con sangre', 'Orina amb sang']
strfiebre = ['Fiebre', 'Febre']
strmucosaspalidas = ['Mucosas pálidas', 'Mucoses pàl·lides']
strpulsofemoraldisminuido = ['Pulso femoral disminuido', 'Pols femoral disminuit']
strlatidosintensos = ['Latidos intensos', 'Batecs intensos']
strpulsoyugular = ['Pulso yugular', 'Pols jugular']
strblefaritis = ['Blefaritis', 'Blefaritis']
strconjuntivitis = ['Conjuntivitis', 'Conjuntivitis']
strperdidadepelo = ['Pérdida de pelo (nariz, orejas y ojos)', 'Pèrdua de pél (nas, orelles i ulls)']
strdiarreas = ['Diarreas', 'Diarrees']
strvomitos = ['Vómitos', 'Vòmits']
stranemiasintomas = ['Anemia', 'Anèmia']
stralmhodillasrugosas = ['Almohadillas rugosas', 'Coixinets rugosos']
strtrufainchada = ['Trufa hinchada', 'Musell inflamat']
strdermatitisconpus = ['Dermatitis con pus', 'Dermatitis amb pus']
strdescamacion = ['Descamación', 'Descamació']
strvasculitis = ['Vasculitis', 'Vasculitis']
struveitis = ['uveítis', 'Uveïtis']
strGlomerulonefritis = ['Glomerulonefritis', 'Glomerulonefritis']
strlagrimeoconpus = ['Lagrimeo con pus', 'Llagrimeig amb pus']
stramigdalitis = ['Amigdalitis', 'Amigdalitis']
stranorexia = ['Anorexia', 'Anorèxia']
strulcerascornia = ['Ulceras córnea', 'Ulceres còrnia']
strulcerasconpus = ['Ulceras con pus', 'Ulceres amb pus']
strespasmos = ['Espasmos/Convulsiones', 'Espasmes/Convulsionis']#Me parece raro
strrigidez = ['Rigidez/parálisis', 'Rigidesa/pràlisis']
strmocosoculares = ['Mocos oculares', 'Mocs oculars']
strdeshidratacion = ['Deshidratación', 'Deshidratació']
strneumonia = ['Neumonía', 'Pneumònia']
strerupcionesenlapiel = ['Erupciones en la piel', 'Erupcions a la pell']
stredema = ['Edema del SNC', 'Edema del SNC']
strneuritisoptica = ['Neuritis óptica', 'Neuritis òptica']
strvomitosseveros = ['Vómitos severos', 'Vòmits severs']
strdiarreasconsangre = ['Diarreas con sangre', 'Diarrees amb sang']
strclorrojoalrededordelaboca = ['Color rojo alrededor de la boca', 'Color vermell al voltant de la boca']



#Pruebas
strprueba1 = ['PCR + Análisis de sangre (microscopio)','PCR + Anàlisis de sang (microscopi)']
strprueba2 = ['Radiografía de tórax', 'Radiografia de tòrax']
strprueba3 = ['Electrocardiograma + ecocardiografía', 'Electrocardiograma + ecocardiografia']
strtestrapido = ['TEST RAPIDO (Sangre)', 'TEST RÀPID ( Sang)']
strtestElisa = ['TEST ELISA', 'TEST ELISA']
strproteinograma = ['PROTEINOGRAMA', 'PROTEÏNOGRAMA']
strcitologia = ['CITOLOGIA (pelo, riñon)', 'CITOLÒGIA ( Pél, ronyó)']
strimmunocromatografia =['Immunocromatografía', 'Immunocromatografia']
strElisaheces =['TEST ELISA heces', 'TEST ELISA femptes']
strPCR =['PCR', 'PCR']
strpruebadeantigenossangre = ['Prueba de antigenos(sangre)', 'Prova antigens(sang)']
strPCRheces = ['PCR de heces', 'PCR de femptes']
stranalisisdeorinaysangre = ['ANALISIS DE ORINA Y SANGRE', 'ANÀLISIS ORINA I SANG']
strenfermedadrenal = ['Enfermedad renal', 'Malaltia renal']
strno = ['No', 'No']
strsi = ['Si','Si']
strenfermedadhepatica = ['Enfermedad hepática', 'Malatia hepàtica']
strpruebasespecificas = ['PRUEBAS ESPECIFICAS','PROVES ESPECIFIQUES']
strpositiva = ['Positiva', 'Positiva']
strnegativa = ['Negativa', 'Negativa']
strmuchos = ['Muchos', 'Molts']
strtestElisaanalisisdesangre = ['Test Elisa + analisis de sangre', 'Test Elisa + anàlisi de sang' ]
strradiografiadetorax = ['RadiografÍa de tórax', 'Radiografia de tòrax' ]
strelectroyeco = ['Electrocardiograma y ecocardiografía', 'Electrocardiograma i ecocardiografia']



#Medicacion Filaria
strdieta = ['DIETA:', 'DIETA:']
stranemia = ['Rica en proteinas, hierro y vitamina B-12', 'Rica en proteïnes, ferro i vinamines B-12']
strbajaengrasas  = ['Baja en grasas', 'Baixa en greixos']
strfluidoterapia = ['Fluidoterapia    24 horas', 'Fluidoterapia    24']
strmedicacion = ['MEDICACIÓN:', 'MEDICACIÓ:']
strdia0 = ['Día 0', 'Dia 0']
strprednisona = ['Prednisona', 'Prednisona']
str1semana = ['1º semana', '1º setmana']
strcantidad1 = [' mg, BID', ' mg, BID']
str2semana = ['2º semana', '2º setmana']
strcantidad1_2 = [' mg, SID', ' mg, SID']
str3i4semana = ['3º y 4º semana', '3º i 4º setmana']
strcantidad1_3 = [' mg, cada 2 dias', ' mg, cada 2 dies']
strdia1 = ['Día 1', 'Dia 1']
strdoxicilina = ['Doxicilina', 'Doxicilina']
strdurante4semanas = ['Durante 4 semana', 'Durant 4 setmanes']
strcantidad4 = [' mg, SID', ' mg, SID']
strmelarsominadiclorhidrat = ['Melarsomina diclorhidrato', 'Melarsomina diclorhidrat ']
strcantidad3_1 =[' ml, BID', ' ml, BID']
strantihistamínicosyglucocorticoides = ['Antihistamínicos y glucocorticoides', 'Antihistamínics i glucortcoides']
strVigilardurante8horas = ['Vigilar durante 8 horas', 'Vigilar durant 8 hores']
strcantidad2 = [' mg', ' mg']
strDia1al28 = ['Día 1 al 28', 'Dia 1 al 28']
strcantidad3 = [' mg, BID', ' mg, bid']
strdia30 = ['Día 30', 'Dia 30']
strdia60 = ['Día 60', 'Dia 60']
str1inyeccion = ['Primera inyección de melarsomina', 'Primera injeció de melarsomina']
strcantidad5 = [' mg, via IM', ' mg, via IM']
strdia90 = ['Día 90', 'Dia 90']
strsegundainyeccion = ['Segunda inyección de melarsomina', 'Segona ijecció de melarsomina']
strdia91 = ['Día 91', 'Dia 91']
strtercerainyeccion = ['Tercera inyección de melarsomina', 'Tercera injecció de melarsomina']
strdia120 = ['Día 120', 'Dia 120']
strdurante30dias = ['Durante 30 dias', 'Durant 30 dies']
#Medicaion Leishmania
stralopurinol = ['Alopurinol', 'Alopurinol']
strdurante6_12_meses = ['Cada 12 horas durante 6-12 meses', 'Cada 12 hores durant 6-12 mesos']
strcantidad6 = [' mg, via VO', ' mg, via VO']
strcalcitriol = ['Calcitriol', 'Calcitriol']
strcadadia = ['Cada dia', 'Cada dia']
strantimoniat = ['Antimoniato de meglumina', 'Antimoniat de meglumina']
strcada4_8_semanas = ['Cada 12 horas durante 4-8 semanas', 'Cada 12 hores durant 4-8 setmanes']
strviaIM = [' ml, via IM', ' ml, via IM']
strmitelsofina = ['Miltefosina', 'Miltefosina']
strvalorareutanasia = ['Valorar Eutanasia', 'Valorar Eutanàsia']
#Medicacion Moquillo
strampicilinayamoxicilina = ['Ampicilina y amoxicilina', 'Ampicilina i amoxicilina']
strcada8horas = ['Cada 8 horas durante 7 dias', 'Cada 8 hores durant 7 dies']
str3tiposdevia =[' mg, via VO, SC o IV', ' mg, via VO, SC o IV']
strcada12horas = ['Cada 12 horas durante 7 dias', 'Cada 12 hores durant 7 dies']
strviaVOyIV = [' mg, via VO o IV', ' mg, via VO o IV']
strcloranfenicol = ['Cloranfenicol', 'Cloranfenicol']
strviaVOySC = [' mg, via VO o SC', ' mg, via VO o SC']
strflorfenicol = ['Florfenicol', 'Florfenicol']
strcada8horasdurante3_5dias = ['Cada 8 horas de 3-5 dias', 'Cada 8 hores de 3-5 dies']
strviaIMySC = [' mg, via IM o SC', ' mg, via IM o SC']
strcefapirina = ['Cefapirina', 'Cefapirina']
strcada6_8horas = ['Cada 6-8 horas de 3-5 dias', 'Cada 6-8 hores de 3-5 dies']
strviaIMySCyIV = [' mg, via IM, SC o IV', ' mg, via IM, SC o IV']
strfenobarvital = ['Fenobarbital (convulsiones)', 'Fenobarbital (convulsions)']
strcada12horas_1 = ['Cada 12 horas', 'Cada 12 hores']
strviaIMyVOyIV = [' mg, via IM, VO o IV', ' mg, via IM, VO o IV']
strdexametasonainyectable = ['Dexametasona inyectable', 'Dexametasono injectable']
strcada24horas = ['Cada 24 horas', 'Cada 24 hores']
strmlviaIVySC = [' ml, via IV o SC', ' ml, via IV o SC']
strcada24durante1dia = ['Cada 24 horas durante 1 día', 'Cada 24 hores durant 1 dia']
strviaIV = [' mg, via IV', ' mg, via IV']
strcada24de6_5dias = ['Cada 24 horas de 3-5 dias', 'Cada 24 hores de 3-5 dies']
#Medicacion Parvo
strobligaracomer = ['Obligar a comer', 'Obligar a menjar']
strcontroldevomitos = ['Control de vómitos', 'Control de vòmits']
strmetronidrazol = ['Metronidazol', 'Metranidazol']
strBID = ['BID', 'BID']
strefovencina = ['Efovecina', 'Efovencina']
strviaSC = [' mg, via SC', ' mg, via SC']
strmaropitan = ['Maropitan', 'Maropitan']
strbuprenofina = ['Buprenorfina', 'Buprenorfina']
strcad8horas_1 = ['Cada 8 horas', 'Cada 8 hores']
strsuplementos = ['Suplementos: potasio VO y cristaloides SC', 'Suplements: potasi VO i cristal·loides SC']
strcada6horas = ['Cada 6 horas', 'Cada 6 hores']
strml = [' ml', ' ml']
strjarabe = ['Jarabe de maíz', 'Xarop de blat de moro']
strmlVO = [' ml, via VO', ' ml, via VO']
strtamiflu = ['Tamiflu ', 'Tamiflu']
strcada24horasduraante10dias = ['Cada 24 horas durante 10 dias', 'Cada 24 hores durant 10 dies']



#otros textos
strdiagnosticar = ['Diagnosticar ','Diagnòstic ']
strposibleenfermedad = [' POSIBLE ENFERMEDAD         ','POSIBLE MALALTIA']
strsiguiente = ['Siguiente','Següent']
stracceptaediagnostico = ['Aceptar diagnóstico', 'Acceptar diagnòstic']
strhospitalizacion = ['Hospitalización', 'Hospitalització']
strcirugia = ['Cirugía', 'Cirugia']