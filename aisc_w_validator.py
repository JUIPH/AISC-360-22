"""
Validador de Perfiles W según AISC 360
============================================================================
Valida perfiles W de acuerdo a los Capítulos D, E, F y H del AISC 360

Autor: Ing. Juan Isidro Pérez Hernández
Versión: 0.01
Fecha: 2025

Este script valida perfiles W para:
- Capítulo D: Diseño por Tensión
- Capítulo E: Diseño por Compresión (incluyendo E7 elementos esbeltos)
- Capítulo F: Diseño por Flexión
- Capítulo H: Interacción Flexo-Compresión

Se consideran tanto el eje fuerte como el eje débil.
"""

import math
from dataclasses import dataclass
from typing import Tuple, Dict, Optional
from enum import Enum

class TipoCarga(Enum):
    TENSION = "tension"
    COMPRESION = "compresion"
    FLEXION = "flexion"

class Eje(Enum):
    FUERTE = "fuerte"  # Eje mayor (x-x)
    DEBIL = "debil"    # Eje menor (y-y)

@dataclass
class PropiedadesPerfilW:
    """
    Propiedades geométricas del perfil W
    Todas las dimensiones en unidades consistentes (típicamente pulgadas para sistema inglés)
    """
    # Dimensiones básicas
    d: float      # Peralte total
    bf: float     # Ancho del patín
    tf: float     # Espesor del patín
    tw: float     # Espesor del alma
    
    # Áreas
    A: float      # Área bruta de la sección transversal
    
    # Propiedades del eje fuerte (x-x)
    Ix: float     # Momento de inercia respecto al eje x
    Sx: float     # Módulo de sección respecto al eje x
    Zx: float     # Módulo de sección plástico respecto al eje x
    rx: float     # Radio de giro respecto al eje x
    
    # Propiedades del eje débil (y-y)
    Iy: float     # Momento de inercia respecto al eje y
    Sy: float     # Módulo de sección respecto al eje y
    Zy: float     # Módulo de sección plástico respecto al eje y
    ry: float     # Radio de giro respecto al eje y
    ho: float     # Distancia entre centroides de los patines
    
    # Propiedades torsionales
    J: float      # Constante torsional
    Cw: float     # Constante de alabeo
    
    # Propiedades del material
    Fy: float     # Esfuerzo de fluencia
    Fu: float     # Esfuerzo último de tensión
    E: float = 2038902  # Módulo de elasticidad (kgf/cm^2)

@dataclass
class CondicionesCarga:
    """Cargas aplicadas y longitudes del miembro"""
    Pu: float           # Fuerza axial aplicada (+ tensión, - compresión)
    Mux: float          # Momento aplicado respecto al eje fuerte
    Muy: float          # Momento aplicado respecto al eje débil
    L: float            # Longitud no arriostrada
    Lx: float           # Longitud efectiva para pandeo respecto al eje x
    Ly: float           # Longitud efectiva para pandeo respecto al eje y
    Lt: float           # Longitud no arriostrada para pandeo lateral-torsional
    Cb: float = 1.0     # Factor de modificación por pandeo lateral-torsional

class ValidadorAISC:
    """
    Clase principal del validador para verificaciones de diseño de perfiles W según AISC
    """
    
    def __init__(self, perfil: PropiedadesPerfilW, cargas: CondicionesCarga):
        self.perfil = perfil
        self.cargas = cargas
        self.resultados = {}
    
    def validar_todo(self) -> Dict:
        """
        Realizar todas las verificaciones de diseño y retornar resultados comprensivos
        """
        resultados = {
            'tension': self.verificar_tension() if self.cargas.Pu > 0 else None,
            'compresion': self.verificar_compresion() if self.cargas.Pu < 0 else None,
            'flexion_eje_fuerte': self.verificar_flexion(Eje.FUERTE) if abs(self.cargas.Mux) > 0 else None,
            'flexion_eje_debil': self.verificar_flexion(Eje.DEBIL) if abs(self.cargas.Muy) > 0 else None,
            'clasificacion_seccion': self.clasificar_seccion(),
            'interaccion_flexo_compresion': None
        }
        
        # Verificar interacción flexo-compresión si hay cargas combinadas
        if (self.cargas.Pu < 0 and (abs(self.cargas.Mux) > 0 or abs(self.cargas.Muy) > 0)):
            resultados['interaccion_flexo_compresion'] = self.verificar_interaccion_flexo_compresion(resultados)
        
        return resultados
    
    def clasificar_seccion(self) -> Dict:
        """
        Clasificar sección como compacta, no compacta, o esbelta
        Basado en las Tablas B4.1a y B4.1b del AISC 360
        """
        # Relaciones ancho-espesor
        lambda_f = self.perfil.bf / (2 * self.perfil.tf)  # Relación a/e del patín
        lambda_w = (self.perfil.d - 2 * self.perfil.tf) / self.perfil.tw  # Relación a/e del alma
        
        # Relaciones límite de la Tabla B4.1a (compresión)
        lambda_p_f_comp = 0.56 * math.sqrt(self.perfil.E / self.perfil.Fy)  # Tabla B4.1a, Caso 1
        lambda_r_f_comp = 1.49 * math.sqrt(self.perfil.E / self.perfil.Fy)  # Tabla B4.1a, Caso 5

        # Relaciones límite de la Tabla B4.1b (flexión)
        # Relación para los patínes
        lambda_p_f_flex = 0.38 * math.sqrt(self.perfil.E / self.perfil.Fy)  # Tabla B4.1b, Caso 10
        lambda_r_f_flex = 1.0 * math.sqrt(self.perfil.E / self.perfil.Fy)   # Tabla B4.1b, Caso 10
        # Relación para el alma
        lambda_p_w_flex = 3.76 * math.sqrt(self.perfil.E / self.perfil.Fy)  # Tabla B4.1b, Caso 15
        lambda_r_w_flex = 5.70 * math.sqrt(self.perfil.E / self.perfil.Fy)  # Tabla B4.1b, Caso 15
        
        # Clasificación
        clasificacion = {
            'patin_compresion': self._clasificar_elemento(lambda_f, lambda_p_f_comp, lambda_r_f_comp),
            'patin_flexion': self._clasificar_elemento(lambda_f, lambda_p_f_flex, lambda_r_f_flex),
            'alma_flexion': self._clasificar_elemento(lambda_w, lambda_p_w_flex, lambda_r_w_flex),
            'relaciones': {
                'lambda_f': lambda_f,
                'lambda_w': lambda_w,
                'lambda_p_f_comp': lambda_p_f_comp,
                'lambda_r_f_comp': lambda_r_f_comp,
                'lambda_p_f_flex': lambda_p_f_flex,
                'lambda_r_f_flex': lambda_r_f_flex,
                'lambda_p_w_flex': lambda_p_w_flex,
                'lambda_r_w_flex': lambda_r_w_flex
            }
        }
        
        return clasificacion
    
    def _clasificar_elemento(self, lambda_val: float, lambda_p: float, lambda_r: float) -> str:
        """Clasificar elemento individual basado en la relación ancho-espesor"""
        if lambda_val <= lambda_p:
            return "compacta"
        elif lambda_val <= lambda_r:
            return "no_compacta"
        else:
            return "esbelta"
    
    def verificar_tension(self) -> Dict:
        """
        Capítulo D: Diseño por Tensión
        Ecuaciones D2-1 y D2-2 del AISC 360
        """

        phi_t_fluencia = 0.9  # Factor de resistencia LRFD

        # D2.1 Fluencia por tensión en la sección bruta
        Pn_fluencia = self.perfil.Fy * self.perfil.A  # Ecuación D2-1

        Pt_fluencia = phi_t_fluencia * Pn_fluencia   # Resistencia de diseño por tensión en fluencia
        
        # D2.2 Ruptura por tensión en la sección neta
        # Nota: Asumiendo Ae = A por ahora (suposición conservadora)
        # En la práctica, se necesitaría el cálculo real del área neta
        Ae = self.perfil.A  # Área efectiva neta (simplificado)
        Pn_ruptura = self.perfil.Fu * Ae  # Ecuación D2-2
        phi_t_ruptura = 0.75  # Factor de resistencia LRFD
        Pt_ruptura = phi_t_ruptura * Pn_ruptura
        
        # Capacidad gobernante
        Pt = min(Pt_fluencia, Pt_ruptura)
        
        # Relación demanda/capacidad
        RDC = abs(self.cargas.Pu) / Pt
        
        resultados = {
            'Pn_fluencia': Pn_fluencia,
            'Pt_fluencia': Pt_fluencia,
            'Pn_ruptura': Pn_ruptura,
            'Pt_ruptura': Pt_ruptura,
            'Pt_gobernante': Pt,
            'Pu_aplicada': self.cargas.Pu,
            'RDC': RDC,
            'estado': 'PASA' if RDC <= 1.0 else 'FALLA',
            'modo_gobernante': 'fluencia' if Pt_fluencia < Pt_ruptura else 'ruptura',
            'ecuaciones_ref': ['D2-1', 'D2-2']
        }
        
        return resultados
    
    def verificar_compresion(self) -> Dict:
        """
        Capítulo E: Diseño por Compresión
        """
        # Determinar sección aplicable (E3 para elementos no esbeltos, E7 para esbeltos)
        clasificacion = self.clasificar_seccion()
        
        if (clasificacion['patin_compresion'] == 'esbelta' or 
            clasificacion['alma_flexion'] == 'esbelta'):
            return self._verificar_compresion_esbeltos()
        else:
            return self._verificar_compresion_no_esbeltos()

    # Los siguiente lineas de código se implementaron la sección del E3
    # Del campitulo a compresión para mienbros W
    def _verificar_compresion_no_esbeltos(self) -> Dict:
        """
        E3: Pandeo flexional de miembros sin elementos esbeltos
        Ecuaciones E3-1, E3-2, E3-3, E3-4 del AISC 360
        """
        # Relaciones de longitud efectiva
        KL_r_x = self.cargas.Lx / self.perfil.rx
        KL_r_y = self.cargas.Ly / self.perfil.ry
        # Verificar para validación de mayor precisión para que valide
        # ambos sentidos
        KL_r = max(KL_r_x, KL_r_y)  # Relación de esbeltez gobernante
        
        # Esfuerzo de pandeo elástico (Ecuación E3-4)
        Fe = (math.pi**2 * self.perfil.E) / (KL_r**2)
        
        # Determinar Fcr basado en esbeltez (Ecuaciones E3-2 y E3-3)
        lambda_c = self.perfil.Fy / Fe
        
        if KL_r <= 4.71 * math.sqrt(self.perfil.E / self.perfil.Fy) or lambda_c <= 2.25:  # o λc ≤ 2.25
            # Ecuación E3-2: Pandeo inelástico
            Fcr = (0.658**(lambda_c)) * self.perfil.Fy
            modo_pandeo = "inelastico"
        else:
            # Ecuación E3-3: Pandeo elástico
            Fcr = 0.877 * Fe
            modo_pandeo = "elastico"
        
        # Resistencia nominal a compresión
        Pn = Fcr * self.perfil.A  # Ecuación E3-1
        
        # Factor de resistencia LRFD
        phi_c = 0.9
        Pc = phi_c * Pn
        
        # Relación demanda/capacidad
        RDC = abs(self.cargas.Pu) / Pc
        
        resultados = {
            'KL_r_x': KL_r_x,
            'KL_r_y': KL_r_y,
            'KL_r_gobernante': KL_r,
            'Fe': Fe,
            'lambda_c': lambda_c,
            'Fcr': Fcr,
            'Pn': Pn,
            'Pc': Pc,
            'Pu_aplicada': abs(self.cargas.Pu),
            'RDC': RDC,
            'estado': 'PASA' if RDC <= 1.0 else 'FALLA',
            'modo_pandeo': modo_pandeo,
            'ecuaciones_ref': ['E3-1', 'E3-2' if modo_pandeo == 'inelastico' else 'E3-3', 'E3-4']
        }
        
        return resultados

    # Implementar la parte de E4


    #  La siguiente función se implementaron las sección E7 para
    # Miembros esbeltos para elementos a compresión.
    # Unicamente para secciones W
    def _verificar_compresion_esbeltos(self) -> Dict:
        """
        E7: Miembros con elementos esbeltos
        Ecuaciones E7-1, E7-2, E7-3, E7-4, E7-5, E7-6, E7-7 del AISC 360
        """
        clasificacion = self.clasificar_seccion()
        
        # E7.1: Elementos esbeltos excluyendo HSS redondos
        
        # Factores de reducción del ancho efectivo c1 y c2 (Tabla E7.1)

        # Para elementos rigidizados excepto paredes de HSS cuadrados y rectangulares
        c1 = 0.22  # Tabla E7.1, caso (c) aplica para otros elementos
        c2 = 1.49  # Tabla E7.1, caso (c) aplica para otros elementos

        Fn = self._verificar_compresion_no_esbeltos()['Pc']  # Esfuerzo de pandeo reducido

        # Ancho efectivo reducido para patines esbeltos
        be_patin = self.perfil.bf

        if clasificacion['patin_compresion'] == 'esbelta':
            lambda_f = self.perfil.bf / (2 * self.perfil.tf)
            lambda_r_f = 1.03 * math.sqrt(self.perfil.E / self.perfil.Fy)
            
            # Esfuerzo local de pandeo del patín (Ecuación E7-5)
            Fcl_patin = (c2 * (lambda_r_f / lambda_f)**2) * self.perfil.Fy
            if Fcl_patin > self.perfil.Fy:
                Fcl_patin = self.perfil.Fy
            
            # Ancho efectivo reducido del patín (Ecuación E7-3)
            if lambda_f > lambda_r_f:
                #be_patin = self.perfil.bf * (1 - c1 * math.sqrt(self.perfil.Fy / Fcl_patin)) * math.sqrt(self.perfil.Fy / Fcl_patin)
                be_patin = self.perfil.bf * (1 - c1 * math.sqrt(Fcl_patin / Fn)) * math.sqrt(Fcl_patin / Fn)
            
        # Ancho efectivo reducido para alma esbelta
        be_alma = self.perfil.d - 2 * self.perfil.tf

        if clasificacion['alma_flexion'] == 'esbelta':
            lambda_w = (self.perfil.d - 2 * self.perfil.tf) / self.perfil.tw
            lambda_r_w = 5.70 * math.sqrt(self.perfil.E / self.perfil.Fy)
            
            # Esfuerzo local de pandeo del alma (Ecuación E7-5)
            Fcl_alma = (c2 * (lambda_r_w / lambda_w)**2) * self.perfil.Fy
            if Fcl_alma > self.perfil.Fy:
                Fcl_alma = self.perfil.Fy
            
            # Ancho efectivo reducido del alma (Ecuación E7-3)
            if lambda_w > lambda_r_w:
                #be_alma = (self.perfil.d - 2 * self.perfil.tf) * (1 - c1 * math.sqrt(self.perfil.Fy / Fcl_alma)) * math.sqrt(self.perfil.Fy / Fcl_alma)
                be_alma = (self.perfil.d - 2 * self.perfil.tf) * (1 - c1 * math.sqrt(Fcl_alma / Fn)) * math.sqrt(Fcl_alma / Fn)
        
        # Área efectiva reducida (Ecuación E7-1)
        Ae = self.perfil.A - 2 * (self.perfil.bf - be_patin) * self.perfil.tf - (self.perfil.d - 2 * self.perfil.tf - be_alma) * self.perfil.tw
        
        
        # Verificar que Ae no sea menor que el área bruta
        if Ae > self.perfil.A:
            Ae = self.perfil.A
        
        # Esfuerzo de fluencia modificado
        Fy_mod = self.perfil.Fy * (Ae / self.perfil.A)
        
        # Proceder con el análisis de pandeo global usando Ae y Fy_mod
        # Aplica nuvamente las sección E3 o E4. Utilizando las nuevas propiedades calculadas.

        KL_r_x = self.cargas.Lx / self.perfil.rx
        KL_r_y = self.cargas.Ly / self.perfil.ry
        KL_r = max(KL_r_x, KL_r_y)
        
        # Esfuerzo de pandeo elástico
        Fe = (math.pi**2 * self.perfil.E) / (KL_r**2)
        
        # Determinar Fcr
        lambda_c = math.sqrt(Fy_mod / Fe)
        
        if KL_r <= 4.71 * math.sqrt(self.perfil.E / Fy_mod) or lambda_c <= 2.25:
            # Pandeo inelástico
            Fcr = (0.658**(lambda_c**2)) * Fy_mod
            modo_pandeo = "inelastico"
        else:
            # Pandeo elástico
            Fcr = 0.877 * Fe
            modo_pandeo = "elastico"
        
        # Resistencia nominal a compresión para elementos esbeltos
        Pn = Fcr * Ae  # Ecuación E7-1 modificada
        
        # Factor de resistencia LRFD
        phi_c = 0.9
        Pc = phi_c * Pn
        
        # Relación demanda/capacidad
        RDC = abs(self.cargas.Pu) / Pc
        
        resultados = {
            'KL_r_x': KL_r_x,
            'KL_r_y': KL_r_y,
            'KL_r_gobernante': KL_r,
            'Fe': Fe,
            'lambda_c': lambda_c,
            'Fcr': Fcr,
            'Ae': Ae,
            'Fy_mod': Fy_mod,
            'be_patin': be_patin,
            'be_alma': be_alma,
            'Pn': Pn,
            'Pc': Pc,
            'Pu_aplicada': abs(self.cargas.Pu),
            'RDC': RDC,
            'estado': 'PASA' if RDC <= 1.0 else 'FALLA',
            'modo_pandeo': modo_pandeo,
            'tipo_analisis': 'elementos_esbeltos',
            'ecuaciones_ref': ['E7-1', 'E7-2', 'E7-3', 'E7-5']
        }
        
        return resultados
    
    def verificar_flexion(self, eje: Eje) -> Dict:
        """
        Capítulo F: Diseño por Flexión
        """
        if eje == Eje.FUERTE:
            return self._verificar_flexion_eje_fuerte()
        else:
            return self._verificar_flexion_eje_debil()

    # En la siguiente función se implementa la revisión por flexión para miembros de sección W
    # Sección F2
    def _verificar_flexion_eje_fuerte(self) -> Dict:
        """
        F2-F5: Flexión respecto al eje fuerte
        Ecuaciones F2-1, F2-2, F2-3, F2-4, F2-5, F2-6 del AISC 360
        """
        clasificacion = self.clasificar_seccion()
        
        # Parámetros de pandeo lateral-torsional
        # Longitud límite para zona plástica (Ecuación F2-5)
        Lp = 1.76 * self.perfil.ry * math.sqrt(self.perfil.E / self.perfil.Fy)

        ho = self.perfil.ho  # Distancia entre centroides de los patines

        # Radio de giro efectivo para pandeo lateral-torsional
        rts = math.sqrt(math.sqrt(self.perfil.Iy * self.perfil.Cw) / self.perfil.Sx)
        
        # Longitud límite para zona inelástica (Ecuación F2-6)
        c = 1.0  # Factor para secciones doblemente simétricas

        Lr = (1.95 * rts * (self.perfil.E / (0.7 * self.perfil.Fy)) *
              math.sqrt((self.perfil.J * c) / (self.perfil.Sx * ho) +
              math.sqrt(((self.perfil.J * c) / (self.perfil.Sx * ho))**2 +
              6.76 * (0.7 * self.perfil.Fy / self.perfil.E)**2)))
        
        # Determinar estado límite gobernante
        if self.cargas.Lt <= Lp:
            # F2.1: Secciones compactas con Lb ≤ Lp (fluencia)
            Mp = self.perfil.Fy * self.perfil.Zx
            Mn = Mp
            estado_limite = "fluencia"
            ecuacion_ref = "F2-1"
            
        elif self.cargas.Lt < Lr and self.cargas.Lt <= Lr:
            # F2.2: Pandeo lateral-torsional inelástico (Ecuación F2-2)
            Mp = self.perfil.Fy * self.perfil.Zx
            Mn = self.cargas.Cb * (Mp - (Mp - 0.7 * self.perfil.Fy * self.perfil.Sx) * (self.cargas.Lt - Lp) / (Lr - Lp))
            estado_limite = "pandeo_LT_inelastico"
            ecuacion_ref = "F2-2"
            
        else:
            # F2.3: Pandeo lateral-torsional elástico (Ecuación F2-3)
            Fcr = (((self.cargas.Cb * math.pi**2 * self.perfil.E) /(self.cargas.Lt / rts)**2) *
                   math.sqrt(1 + 0.078 * ((self.perfil.J * c) / (self.perfil.Sx * ho)) * (self.cargas.Lt / rts)**2))
            Mn = Fcr * self.perfil.Sx

            if Mn > self.perfil.Fy * self.perfil.Zx:
                Mn = self.perfil.Fy * self.perfil.Zx
            estado_limite = "pandeo_LT_elastico"
            ecuacion_ref = "F2-3"
        

        # Factor de resistencia LRFD
        phi_b = 0.9
        Mb = phi_b * Mn
        
        # Relación demanda/capacidad
        RDC = abs(self.cargas.Mux) / Mb
        
        resultados = {
            'Lp': Lp,
            'Lr': Lr,
            'Lt': self.cargas.Lt,
            'rts': rts,
            'Mn': Mn,
            'Mb': Mb,
            #'Fcr': Fcr if 'Fcr' in locals() else None,
            'Mux_aplicada': self.cargas.Mux,
            'RDC': RDC,
            'estado': 'PASA' if RDC <= 1.0 else 'FALLA',
            'estado_limite': estado_limite,
            'clasificacion': clasificacion['patin_flexion'],
            'ecuaciones_ref': [ecuacion_ref, 'F2-5', 'F2-6']
        }
        
        return resultados

    # Falta implementar la sección F3


    # Función para la implementación de la sección F6 para secciones W (IR)
    def _verificar_flexion_eje_debil(self) -> Dict:
        """
        F6: Miembros en forma de I flexionados respecto al eje débil
        Ecuaciones F6-1, F6-2 del AISC 360
        """
        clasificacion = self.clasificar_seccion()

        b = self.perfil.bf
        tf = self.perfil.tf
        rel = clasificacion['relaciones']
        lambda_pf = rel['lambda_p_f_flex']
        lambda_rf = rel['lambda_r_f_flex']
        E = self.perfil.E
        Fy = self.perfil.Fy
        Sy = self.perfil.Sy
        Zy = self.perfil.Zy
        lambda1 = rel['lambda_f']
        Fcr = (0.70*E) / ((b/tf)**2) # Ecuación F6-4

        if clasificacion['patin_flexion'] == 'compacta':
            # F6.1: Secciones compactas (Ecuación F6-1)
            Mp = Fy * Zy
            Mn = Mp
            estado_limite = "fluencia"
            ecuacion_ref = "F6-1"
        elif clasificacion['patin_flexion'] == 'no_compacta':
            # F6.2: Secciones no compactas/esbeltas (Ecuación F6-2)
            Mp = Fy * Zy
            Mn = Mp - (Mp - 0.70*Sy*Sy)*((lambda1 - lambda_pf)/(lambda_rf - lambda_pf))
            estado_limite = "no_compacta"
            ecuacion_ref = "F6-2"
        else:
            # F6.3: Secciones esbeltas (Ecuación F6-3)
            # Para secciones no compactas, usar módulo elástico
            Mn = Fcr * Sy
            estado_limite = "esbelta"
            ecuacion_ref = "F6-3"
        
        # Factor de resistencia LRFD
        phi_b = 0.9
        Mb = phi_b * Mn
        
        # Relación demanda/capacidad
        RDC = abs(self.cargas.Muy) / Mb
        
        resultados = {
            'Mn': Mn,
            'Mb': Mb,
            'Muy_aplicada': self.cargas.Muy,
            'RDC': RDC,
            'estado': 'PASA' if RDC <= 1.0 else 'FALLA',
            'estado_limite': estado_limite,
            'clasificacion': clasificacion['patin_flexion'],
            'ecuaciones_ref': [ecuacion_ref]
        }
        
        return resultados
    
    def verificar_interaccion_flexo_compresion(self, resultados_previos: Dict) -> Dict:
        """
        Capítulo H: Interacción de Fuerzas
        Ecuaciones H1-1a y H1-1b del AISC 360
        """
        # Obtener capacidades individuales
        if resultados_previos['compresion'] is None:
            return {'estado': 'ERROR', 'nota': 'Se requiere verificación de compresión'}
        
        Pc = resultados_previos['compresion']['Pc']
        
        # Capacidades de flexión
        Mcx = 0
        Mcy = 0
        
        if resultados_previos['flexion_eje_fuerte']:
            Mcx = resultados_previos['flexion_eje_fuerte']['Mb']
        
        if resultados_previos['flexion_eje_debil']:
            Mcy = resultados_previos['flexion_eje_debil']['Mb']
        
        # Cargas aplicadas
        Pr = abs(self.cargas.Pu)  # Carga axial requerida
        Mrx = abs(self.cargas.Mux)  # Momento requerido eje fuerte
        Mry = abs(self.cargas.Muy)  # Momento requerido eje débil
        
        # Determinar ecuación aplicable
        if (Pr / Pc) >= 0.2:
            # Ecuación H1-1a
            interaccion = (Pr / Pc) + (8.0/9.0) * ((Mrx / Mcx) + (Mry / Mcy))
            ecuacion_aplicada = "H1-1a"
        else:
            # Ecuación H1-1b
            interaccion = (Pr / (2 * Pc)) + ((Mrx / Mcx) + (Mry / Mcy))
            ecuacion_aplicada = "H1-1b"
        
        # Estado de la verificación
        estado = 'PASA' if interaccion <= 1.0 else 'FALLA'
        
        resultados = {
            'interaccion': interaccion,
            'ecuacion_aplicada': ecuacion_aplicada,
            'Pr_Pc': Pr / Pc if Pc > 0 else 0,
            'Mrx_Mcx': Mrx / Mcx if Mcx > 0 else 0,
            'Mry_Mcy': Mry / Mcy if Mcy > 0 else 0,
            'Pr': Pr,
            'Pc': Pc,
            'Mrx': Mrx,
            'Mcx': Mcx,
            'Mry': Mry,
            'Mcy': Mcy,
            'estado': estado,
            'ecuaciones_ref': [ecuacion_aplicada]
        }
        
        return resultados

def imprimir_resultados(resultados: Dict, nombre_seccion: str = "Perfil-W"):
    """
    Imprimir resultados de validación formateados
    """
    print(f"\n{'='*70}")
    print(f"RESULTADOS DE VALIDACIÓN AISC PARA {nombre_seccion}")
    print(f"{'='*70}")
    
    # Clasificación de la sección
    if 'clasificacion_seccion' in resultados:
        print(f"\nCLASIFICACIÓN DE LA SECCIÓN:")
        clasificacion = resultados['clasificacion_seccion']
        print(f"  Patín (Compresión):     {clasificacion['patin_compresion']}")
        print(f"  Patín (Flexión):        {clasificacion['patin_flexion']}")
        print(f"  Alma (Flexión):         {clasificacion['alma_flexion']}")
        
        relaciones = clasificacion['relaciones']
        print(f"\nRELACIONES ANCHO-ESPESOR:")
        print(f"  λ patín:                {relaciones['lambda_f']:.2f}")
        print(f"  λ alma:                 {relaciones['lambda_w']:.2f}")
        print(f"  λp patín (comp):        {relaciones['lambda_p_f_comp']:.2f}")
        print(f"  λr patín (comp):        {relaciones['lambda_r_f_comp']:.2f}")
    
    # Verificación por tensión
    if resultados['tension']:
        print(f"\nVERIFICACIÓN POR TENSIÓN (Capítulo D):")
        t = resultados['tension']
        print(f"  Carga Aplicada (Pu):    {t['Pu_aplicada']:.1f} kgf")
        print(f"  Capacidad (φPn):        {t['Pt_gobernante']:.1f} kgf")
        print(f"  RDC:                    {t['RDC']:.3f}")
        print(f"  Estado:                 {t['estado']}")
        print(f"  Modo Gobernante:        {t['modo_gobernante']}")
        print(f"  Ecuaciones:             {', '.join(t['ecuaciones_ref'])}")
    
    # Verificación por compresión
    if resultados['compresion']:
        print(f"\nVERIFICACIÓN POR COMPRESIÓN (Capítulo E):")
        c = resultados['compresion']
        if 'RDC' in c:
            print(f"  Carga Aplicada (Pu):    {c['Pu_aplicada']:.1f} kgf")
            print(f"  Fe:                     {c['Fe']:.1f} kgf")
            print(f"  Fcr:                    {c['Fcr']:.1f} kgf")
            print(f"  Pn:                     {c['Pn']:.1f} kgf")
            print(f"  Capacidad (φPn):        {c['Pc']:.1f} kgf")
            print(f"  RDC:                    {c['RDC']:.3f}")
            print(f"  Estado:                 {c['estado']}")
            print(f"  KL_r_x:                 {c['KL_r_x']:.1f} cm")
            print(f"  KL_r_y:                 {c['KL_r_y']:.1f} cm")
            print(f"  KL/r Gobernante:        {c['KL_r_gobernante']:.1f}")
            print(f"  Modo de Pandeo:         {c['modo_pandeo']}")
            if 'tipo_analisis' in c:
                print(f"  Tipo de Análisis:       {c['tipo_analisis']}")
                if c['tipo_analisis'] == 'elementos_esbeltos':
                    print(f"  Área Efectiva (Ae):     {c['Ae']:.2f} cm²")
                    print(f"  Fy Modificado:          {c['Fy_mod']:.1f} kgf/cm²")
            print(f"  Ecuaciones:             {', '.join(c['ecuaciones_ref'])}")
        else:
            print(f"  Estado:                 {c['estado']}")
    
    # Verificaciones por flexión
    if resultados['flexion_eje_fuerte']:
        print(f"\nVERIFICACIÓN POR FLEXIÓN - EJE FUERTE (Capítulo F):")
        f = resultados['flexion_eje_fuerte']
        print(f"  Momento Aplicado (Mux): {f['Mux_aplicada']:.1f} kgf-cm")
        print(f"  Capacidad Nominal (Mn): {f['Mn']:.1f} kgf-cm")
        #print(f"  Esfuerzo Critico (Fcr): {f['Fcr']:.1f} kgf-cm")
        print(f"  Capacidad (φMn):        {f['Mb']:.1f} kgf-cm")
        print(f"  RDC:                    {f['RDC']:.3f}")
        print(f"  Estado:                 {f['estado']}")
        print(f"  Estado Límite:          {f['estado_limite']}")
        print(f"  Lp:                     {f['Lp']:.2f} cm")
        print(f"  Lr:                     {f['Lr']:.2f} cm")
        print(f"  Lt:                     {f['Lt']:.2f} cm")
        print(f"  rts:                    {f['rts']:.2f} cm")
        print(f"  Ecuaciones:             {', '.join(f['ecuaciones_ref'])}")
    
    if resultados['flexion_eje_debil']:
        print(f"\nVERIFICACIÓN POR FLEXIÓN - EJE DÉBIL (Capítulo F):")
        f = resultados['flexion_eje_debil']
        print(f"  Momento Aplicado (Muy): {f['Muy_aplicada']:.1f} kgf-cm")
        print(f"  Capacidad (φMn):        {f['Mb']:.1f} kgf-cm")
        print(f"  RDC:                    {f['RDC']:.3f}")
        print(f"  Estado:                 {f['estado']}")
        print(f"  Estado Límite:          {f['estado_limite']}")
        print(f"  Ecuaciones:             {', '.join(f['ecuaciones_ref'])}")
    
    # Verificación de interacción flexo-compresión
    if resultados['interaccion_flexo_compresion']:
        print(f"\nVERIFICACIÓN DE INTERACCIÓN FLEXO-COMPRESIÓN (Capítulo H):")
        i = resultados['interaccion_flexo_compresion']
        if 'interaccion' in i:
            print(f"  Valor de Interacción:   {i['interaccion']:.3f}")
            print(f"  Estado:                 {i['estado']}")
            print(f"  Ecuación Aplicada:      {i['ecuacion_aplicada']}")
            print(f"  Pr/Pc:                  {i['Pr_Pc']:.3f}")
            print(f"  Mrx/Mcx:                {i['Mrx_Mcx']:.3f}")
            print(f"  Mry/Mcy:                {i['Mry_Mcy']:.3f}")
            print(f"  Ecuaciones:             {', '.join(i['ecuaciones_ref'])}")
        else:
            print(f"  Estado:                 {i['estado']}")
            print(f"  Nota:                   {i['nota']}")
    
    print(f"\n{'='*70}")
