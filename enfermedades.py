from enum import Enum
from idiomas import strGrave, strLeve, strMuyGrave, leer_idioma_actual 

AceptarEnfermedad = 1
RechazarEnfermedad = 0
SiguientePrueba = -1

class Enfermedad:
    name =' '
    puntos = 0
    
    def init (self):
        self.puntos=0
        self.sintomas_detectados.clear()
        self.muchos = False

    def sumar_sintoma(self, sintoma):                
        for s, v in self.sintomas:
            if s == sintoma: 
                self.puntos += v
                self.sintomas_detectados.append(sintoma)
                break

    def restar_puntos_por_vacuna(self, resta):
        self.puntos = self.puntos - resta
        if self.puntos < 0:
            self.puntos = 0

    def retornar_puntos(self):
        return str(self.puntos)
    
    def es_grave(self):
        return False
    def es_muy_grave(self):
        return False
    def nivel_gravedad(self):
        idioma_actual = leer_idioma_actual()
        if self.es_grave() == False:
            return strLeve[idioma_actual]
        elif self.es_muy_grave() == False:
            return strGrave[idioma_actual]
        return strMuyGrave[idioma_actual]
    
    def necesita_hospitalizacion(self, renal, hepatica, anemia):
        return False
    def necesita_cirugia(self):
        return False    
    def rellenar_medicacion(self, perro, ventana_dieta, ventana_medicacion, renal, hepatica, anemia):
        return False

    def calcular_diagnostico(self, resultado, num_prueba):
        return RechazarEnfermedad, 0
        
    sintomas = []
    pruebas = []
    sintomas_detectados =[]
    muchos = False
   

enfermedades_estudiadas = []

#pruebas
enfermedad_actual = 0
prueba_actual = 0

def calcular_maximo():
    maximo = 0
    global enfermedad_actual
    enfermedad_actual = 0
    for i in range(0, len(enfermedades_estudiadas)):
        if enfermedades_estudiadas[i].puntos > maximo:
            maximo = enfermedades_estudiadas[i].puntos
            enfermedad_actual = i
    if maximo == 0:
        return False
    return True

def empezar_diagnostico():  
    res = calcular_maximo()    
    global prueba_actual
    prueba_actual = 0
    return res
    

def get_enfermedad_actual():
    global enfermedad_actual
    return enfermedad_actual

def get_prueba_actual():
    global prueba_actual
    return prueba_actual


def siguiente_diagnostico_internal():
    global prueba_actual
    global enfermedad_actual
    if prueba_actual >= len(enfermedades_estudiadas[enfermedad_actual].pruebas) -1:
       res = siguiente_enfermedad_internal()
       if res == False:
           return False
    else:
        prueba_actual = prueba_actual + 1
    return True
 
def siguiente_enfermedad_internal():
    global enfermedad_actual
    enfermedades_estudiadas[enfermedad_actual].init()  # esta no es-> la quitamos
    if calcular_maximo() == False:
       return False   
    global prueba_actual 
    prueba_actual = 0
    return True
 


