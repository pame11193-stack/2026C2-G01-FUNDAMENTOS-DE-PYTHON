"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total"""
    return sum(ventas)
def calcular_promedio(lista):
    """Retorna el promedio de ventas de una lista"""
    return sum(lista) / len (lista)
def calcular_porcentaje(total,meta, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{porcentaje:.2f}%"
    return porcentaje
def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcentaje(total, meta)
    if porcentaje_sede >= 100:
        mensaje_sede = "Meta alcanzada."
    elif porcentaje_sede >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atencion."
    else:
        mensaje_sede = "Meta no alcanzada, requiere atencion."
    return mensaje_sede
    
print("cantidad de sedes:",len (sedes))
#print("tipo de variable sedes:",type (sedes))
#print("tipo de variable sedes[0]:",type (sedes))
#print("Datos por sede:",sedes[0].keys)
#print("Primera sede:", sedes[0]['nombre'])
for sede in sedes:
    sede_demo = sedes[0]
    ventas = sede_demo["ventas"]
    meta = sede_demo["meta"]

    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_porcentaje(total_sede,meta, True)
    estado = calcular_clasificacion(total_sede, meta)

    print(porcentaje_sede)

