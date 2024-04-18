# ALGORITMO BÁSICO DE VENTANA DE TRANSACCIÓN -- TECH CASH CLUB

"""
    CONCEPTO: la idea es calcular un porcentaje de descuento de un producto x en base a una puja o transacción temporal, 
    con fecha de inicio, y fecha de cierre, en el que se van apuntando consumidores, pero con la peculariedad de que suman
    su fuerza de compra hasta el cierre para obtener un descuento individual mayor que si realizaran la compra en solitario.

    ESQUEMA DEL ALGORITMO: podemos considerar que el descuento crece de forma no lineal en función del número de participantes
    para hacerlo más atractivo a medida que se unan más personas. 

    1.Definición de Parámetros iniciales:
        - Fecha de inicio y fecha de cierre de la transacción o puja. 
        - Lista de consumidores que se irán uniendo. 
        - Fórmula para calcular el descuento basada en el número de socios o consumidores. 
    2.Registro de Consumidores:
        - Los socios o consumidores se pueden registrar durante el periodo de puja o transacción.  
        - Almacenamos el tiempo de cada registro para asegurarnos de que se respetan las fechas de inicio y cierre. 
    3.Cálculo del Descuento:
        - El descuento podría calcularse como un porcentaje que aumenta de forma cuadrática, cúbica o cualquier otra 
          fórmula matemática en función del número de participantes. 
    4.Aplicación del Descuento:
        - Al finalizar la puja conjunta, se calcula el desuento total y se aplica a todos los consumidores o socios registrados.     








"""

import datetime

class Transaccion:

    def __init__(self, fecha_inicio, fecha_fin):

        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.socios = []

    def agregar_socio(self, id_socio):

        if self.fecha_inicio <= datetime.datetime.now() <= self.fecha_fin:

            self.socios.append(id_socio)
            print(f" Socio {id_socio} agregado. Total de socios: {len(self.socios)} ")
        else:
            print("La puja está cerrada o aún no ha comenzado.")

    def calcular_descuento(self):
        numero_de_socios = len(self.socios)
        #Ejemplo de fórmula de descuento

        descuento = min(30, numero_de_socios ** 2 * 0.1) # Descuento aumenta de manera cuadrática, máximo del 30%

        return descuento